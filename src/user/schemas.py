from typing import Union

from pydantic import BaseModel, Field, EmailStr

class SendOtpRequest(BaseModel):
    email: EmailStr
    referral_code: Union[str, None] = Field(default=None, min_length=1)

    class Config:
        json_schema_extra = {
            "examples": [
                {
                    "email": "abc@mail.co",
                    "referral_code": "PXAWL27LS83P"
                },
                {
                    "email": "abc@mail.co"
                },

            ]
        }

class VerifyOtpRequest(SendOtpRequest):
    otp: str = Field(max_length=6, min_length=6)

    class Config:
        json_schema_extra = {
            "examples": [
                {
                    "email": "abc@mail.co",
                    "otp": "123456"
                }
            ]
        }
