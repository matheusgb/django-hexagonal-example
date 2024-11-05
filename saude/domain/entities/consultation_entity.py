import uuid
from django.db import models
from saude.domain.entities.professional_entity import ProfessionalEntity
from saude.domain.entities.etc.query_set import QuerySet


class ConsultationEntity(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True
    )
    scheduled_date = models.DateField()
    professional = models.ForeignKey(
        ProfessionalEntity,
        on_delete=models.CASCADE,
        related_name='consultations'
    )
    created_at = models.TimeField(
        auto_now_add=True
    )
    updated_at = models.TimeField(
        auto_now_add=True
    )
    deleted = models.BooleanField(
        default=False
    )
    deleted_at = models.TimeField(
        null=True,
        blank=True
    )

    objects = QuerySet.as_manager()
