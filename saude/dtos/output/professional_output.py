from typing import Optional
from uuid import UUID
import datetime
from saude.domain.entities.professional_entity import ProfessionalEntity


class ProfessionalOutputDTO(ProfessionalEntity):
    id: UUID
    name: str
    social_name: Optional[str] = None
    profession: Optional[str] = None
    address: str
    phone_number: Optional[str] = None
    email: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
