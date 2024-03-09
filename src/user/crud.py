from sqlalchemy.orm import Session

from models import OTP, OtpStatusEnum
from schemas import SendOtpSchema, VerifyOtpSchema


def get_otp(db: Session, email: str):
    return db.query(OTP).filter(OTP.email == email).order_by(OTP.id.desc()).first()

def create_otp(db: Session, email: str, otp: str, otp_status: OtpStatusEnum):
    db_otp = OTP(email=email, otp=otp, otp_status=otp_status)
    db.add(db_otp)
    db.commit()
    db.refresh(db_otp)
    return db_otp

# def update_otp(db: Session, email)