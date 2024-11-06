from rest_framework import serializers
from saude.domain.entities.professional_entity import ProfessionalEntity


class ProfessionalOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfessionalEntity
        fields = ['id', 'name', 'social_name', 'profession',
                  'address', 'phone_number', 'email', 'created_at', 'updated_at']

    social_name = serializers.CharField(required=False, allow_null=True)
    profession = serializers.CharField(required=False, allow_null=True)
    phone_number = serializers.CharField(required=False, allow_null=True)
