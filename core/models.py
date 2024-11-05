import uuid
from django.db import models
from django.core.validators import RegexValidator


class QuerySet(models.QuerySet):
    def active(self):
        return self.filter(deleted=False)


class Professional(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True
    )
    name = models.CharField(max_length=100)
    social_name = models.CharField(
        max_length=100,
        blank=True
    )
    profession = models.CharField(
        max_length=100,
        blank=True
    )
    address = models.TextField(max_length=400)
    phone_number = models.CharField(
        max_length=15,
        validators=[RegexValidator(
            r'^\d+$', 'Somente números são permitidos.')],
        blank=True,
    )
    email = models.EmailField(
        max_length=254,
        unique=True,
        blank=False,
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

    def __str__(self):
        return self.name


class Consultation(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True
    )
    scheduled_date = models.DateField()
    professional = models.ForeignKey(
        Professional,
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

    def __str__(self):
        return self.name
