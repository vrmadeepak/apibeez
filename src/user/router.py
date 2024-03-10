from fastapi import APIRouter, status, HTTPException, Depends
from fastapi.responses import JSONResponse

from src.database import get_db
from sqlalchemy.orm import Session

from src.user.schemas import SendOtpRequest, VerifyOtpRequest
from src.user.service import send_otp, verify_otp

user_router = APIRouter()


@user_router.post(
    "/otp/send",
    summary="Send OTP to email",
)
def send_user_otp(payload: SendOtpRequest, db: Session = Depends(get_db)):
    """
    Send an otp to the user and store the referral code if valid
    """
    content, error = send_otp(payload.email, payload.referral_code, db)
    if error:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    
    return JSONResponse(
        content=content, status_code=status.HTTP_200_OK
    )


@user_router.post("/otp/verify")
def verify_user_otp(payload: VerifyOtpRequest, db: Session = Depends(get_db)):
    content, error = verify_otp(payload.email, payload.otp, db)
    if error:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return JSONResponse(content=content, status_code=status.HTTP_200_OK)
