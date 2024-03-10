import string
import random
from typing import List, Union

from sqlalchemy.orm import Session

from src.user import crud
from src.user.models import OtpStatusEnum

def create_user_otp(db: Session, email: str, otp: Union[str, None] = None):
    if not otp:
        otp = str(random.random())[2:8]

    otp_obj = crud.create_otp(db, email, otp, OtpStatusEnum.SENT)

def generate_referral_code(db: Session, length=8):
    while True:
        characters = string.ascii_uppercase + string.digits*2
        code = "BEE" + ''.join(random.choice(characters) for _ in range(length))

        if not crud.get_referral_code(db, code):
            return code

def send_otp(email: str, referral_code: Union[str, None], db: Session):
    content = {
        "message": "OTP sent",
        "first_time_user": False,
        "email": email,
        "referral_code": referral_code
    }
    error = None
    try:
        user = crud.get_user_by_email(db, email)
        print(">> user", user.email)
        if not user:
            content["first_time_user"] = True

        if referral_code and content["first_time_user"]:
            referral_code = crud.get_referral_code(db, referral_code)
            if not referral_code:
                return None, "referral code is not valid"
        
        user_otp = crud.get_latest_otp(db, email)
        if not user_otp:
            create_user_otp(db, email)
            return content, None
        
        # if user_otp.updated_at 
        create_user_otp(db, email, user_otp.otp)
        # print(">>> user-otp", user_otp.otp)
    except Exception as ex:
        error = ex.__str__()
        print(f"[SEND OTP] > Exception: {error}")

    return content, error

def verify_otp(email: str, otp: str, db: Session):
    content = {
        "message": "OTP verification successful",
        "user_id": None,
        "email": email,
        "referral_code": None,
        "is_referred": False
    }
    error = None
    try: 
        user_otp = crud.get_latest_otp(db, email)
        if not user_otp:
            error = "OTP does not exist. Request OTP."
            return None, error
        
        if user_otp.otp == otp:
            if user_otp.otp_status == OtpStatusEnum.SUCCESS:
                error = "OTP already verified. Request OTP."
            else:
                crud.update_otp_status(db, user_otp, OtpStatusEnum.SUCCESS)
                referral_code = generate_referral_code(db)
                user = crud.get_user_by_email(db, email)
                if not user:
                    user = crud.create_user(db, email, referral_code)
                    if not user:
                        raise ValueError("Failed to create user")
                content["user_id"] = user.id
                content["referral_code"] = user.referral_code
            
        else:
            crud.update_otp_status(db, user_otp, OtpStatusEnum.FAIL)
            error = "Incorrect OTP. Try again."
        
    except Exception as ex:
        error = ex.__str__()
        print(f"[VERIFY OTP] > Exception: {ex}")

    return content, error