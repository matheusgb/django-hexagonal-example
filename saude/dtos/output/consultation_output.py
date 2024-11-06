import datetime
from uuid import UUID


class ConsultationOutputDTO():
    id: UUID
    scheduled_date: datetime.datetime
    professional: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
