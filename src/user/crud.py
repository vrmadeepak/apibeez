from sqlalchemy.orm import Session

from src.user.models import OTP, OtpStatusEnum, User


def update_otp_status(db: Session, user_otp: OTP, status: OtpStatusEnum):
    user_otp.otp_status = status
    db.commit()
    db.refresh(user_otp)

def get_latest_otp(db: Session, email: str):
    return db.query(OTP).filter(OTP.email == email).order_by(OTP.created_at.desc()).first()

def create_otp(db: Session, email: str, otp: str, otp_status: OtpStatusEnum):
    db_otp = OTP(email=email, otp=otp, otp_status=otp_status)
    db.add(db_otp)
    db.commit()
    db.refresh(db_otp)
    return db_otp

def get_referral_code(db: Session, code: str):
    return db.query(User).filter(User.referral_code == code).first()

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def get_user_by_email(db: Session, email):
    return db.query(User).filter_by(email=email,).first()

def create_user(db: Session, email: str, referral_code: str):
    db_user = User(email=email, referral_code=referral_code)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
# def update_otp(db: Session, email)