import uuid
from datetime import datetime
from typing import Optional, Any

from fastapi_users import schemas
from pydantic import EmailStr, validator


class UserRead(schemas.BaseUser[int]):
    name: str
    reg_at: Optional[datetime] = None
    role: str
    pass


class UserCreate(schemas.BaseUserCreate):
    name: str
    email: EmailStr
    password: str
    rpassword: str

    @validator("rpassword")
    def validate_password_repeat(cls, rpassword, values):
        if "password" in values and rpassword != values["password"]:
            raise ValueError("Passwords do not match")
        return rpassword


class UserUpdate(schemas.BaseUserUpdate):
    pass
