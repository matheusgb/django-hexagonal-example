from typing import Optional


class ProfessionalOutputDTO():
    name: str
    social_name: Optional[str] = None
    profession: Optional[str] = None
    address: str
    phone_number: Optional[str] = None
    email: str
