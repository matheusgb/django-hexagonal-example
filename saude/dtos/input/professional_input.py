from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class CreateProfessionalInputDTO(BaseModel):
    name: str = Field(..., max_length=100)
    social_name: Optional[str] = Field(None, max_length=100)
    profession: Optional[str] = Field(None, max_length=100)
    address: str = Field(..., max_length=100)
    phone_number: Optional[str] = Field(
        None, pattern=r'^\+?(\d{1,4})?[\s.-]?(\(?\d{1,3}\)?[\s.-]?)?[\d\s.-]{3,}$')
    email: EmailStr


class UpdateProfessionalInputDTO(BaseModel):
    name: Optional[str] = Field(None, max_length=100)
    social_name: Optional[str] = Field(None, max_length=100)
    profession: Optional[str] = Field(None, max_length=100)
    address: Optional[str] = Field(None, max_length=100)
    phone_number: Optional[str] = Field(
        None, pattern=r'^\+?(\d{1,4})?[\s.-]?(\(?\d{1,3}\)?[\s.-]?)?[\d\s.-]{3,}$')
    email: Optional[EmailStr] = None
