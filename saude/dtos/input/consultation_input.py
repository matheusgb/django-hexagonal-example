from pydantic import BaseModel
import datetime


class ConsultationInputDTO(BaseModel):
    scheduled_date: datetime.datetime
    professional: str
