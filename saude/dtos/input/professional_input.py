from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class CreateProfessionalInputDTO(BaseModel):
    name: str
    social_name: Optional[str] = None
    profession: Optional[str] = None
    address: str
    phone_number: Optional[str] = Field(
        None, regex=r'^\+?(\d{1,4})?[\s.-]?(\(?\d{1,3}\)?[\s.-]?)?[\d\s.-]{3,}$')
    email: EmailStr


class UpdateProfessionalInputDTO(BaseModel):
    name: Optional[str] = None
    social_name: Optional[str] = None
    profession: Optional[str] = None
    address: Optional[str] = None
    phone_number: Optional[str] = Field(
        None, regex=r'^\+?(\d{1,4})?[\s.-]?(\(?\d{1,3}\)?[\s.-]?)?[\d\s.-]{3,}$')
    email: Optional[EmailStr] = None
