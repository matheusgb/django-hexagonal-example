import uuid
from django.db import models
from django.core.validators import RegexValidator
from saude.domain.entities.etc.query_set import QuerySet


class ProfessionalEntity(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True
    )
    name = models.CharField(max_length=100)
    social_name = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    profession = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    address = models.TextField(max_length=400)
    phone_number = models.CharField(
        max_length=15,
        validators=[RegexValidator(
            r'^\d+$', 'Somente números são permitidos.')],
        blank=True,
        null=True
    )
    email = models.EmailField(
        max_length=254,
        unique=True,
        blank=False,
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )
    deleted = models.BooleanField(
        default=False
    )
    deleted_at = models.DateTimeField(
        null=True,
        blank=True
    )

    objects = QuerySet.as_manager()

    def __str__(self):
        return self.name
