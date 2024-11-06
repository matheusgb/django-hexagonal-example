from rest_framework import viewsets, status
from rest_framework.response import Response
from saude.dtos.input.professional_input import CreateProfessionalInputDTO, UpdateProfessionalInputDTO
from saude.dtos.output.professional_output import ProfessionalOutputDTO
from saude.application.professional_service import ProfessionalService
from saude.dtos.output.professional_serializer import ProfessionalOutputSerializer


class ProfessionalController(viewsets.ViewSet):
    def __init__(self):
        self.repository = ProfessionalService()

    def create_professional(self, request):
        pass

    def update_professional(self, request):
        pass

    def list_professional(self, request):
        pass

    def list_all_professionals(self, request, pk=None):
        pass

    def delete_professional(self, request, pk=None):
        pass
