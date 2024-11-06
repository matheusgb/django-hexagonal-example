from rest_framework import serializers
from saude.domain.entities.consultation_entity import ConsultationEntity


class ConsultationOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsultationEntity
        fields = ['id', 'scheduled_date', 'professional', 'created_at',
                  'updated_at']
