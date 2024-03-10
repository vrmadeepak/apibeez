import uuid
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, func, Enum as EnumColumn, Sequence
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from src.database.service import Base

from enum import Enum


class OtpStatusEnum(Enum):
    FAIL = "fail"
    SENT = "sent"
    SUCCESS = "success"

class AccountStatusEnum(Enum):
    LOCKED = "locked"
    ACTIVE = "active"
    RETRY = "retry"

class OTP(Base):
    __tablename__ = "otps"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, index=True, nullable=False)
    otp = Column(String, nullable=False)
    otp_status = Column(EnumColumn(OtpStatusEnum), nullable=False)
    resend_attempts = Column(Integer, default=None)
    verification_attempts = Column(Integer, default=None)
    account_status = Column(EnumColumn(AccountStatusEnum))
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    uuid = Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    last_accessed = Column(DateTime, server_default=func.now(), nullable=False)
    referral_code = Column(String, unique=True, index=True, nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)

