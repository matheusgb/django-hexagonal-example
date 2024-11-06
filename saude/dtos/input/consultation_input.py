from uuid import UUID
from pydantic import BaseModel
import datetime
from typing import Optional


class CreateConsultationInputDTO(BaseModel):
    scheduled_date: datetime.datetime
    professional: UUID


class UpdateConsultationInputDTO(BaseModel):
    scheduled_date: Optional[datetime.datetime] = None
    professional: Optional[UUID] = None
