from typing import Union

from pydantic import BaseModel

class SendOtpSchema(BaseModel):
    email: str


class VerifyOtpSchema(SendOtpSchema):
    otp: str