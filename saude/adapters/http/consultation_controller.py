from rest_framework import viewsets, status
from rest_framework.response import Response
from saude.dtos.input.consultation_input import CreateConsultationInputDTO, UpdateConsultationInputDTO
from saude.dtos.output.consultation_output import ConsultationOutputDTO
from saude.application.consultation_service import ConsultationService
from saude.dtos.output.consultation_serializer import ConsultationOutputSerializer


class ConsultationController(viewsets.ViewSet):
    def __init__(self):
        self.repository = ConsultationService()

    def create_consultation(self, request):
        pass

    def update_consultation(self, request):
        pass

    def list_consultation(self, request):
        pass

    def list_all_consultations(self, request):
        pass

    def delete_consultation(self, request):
        pass
