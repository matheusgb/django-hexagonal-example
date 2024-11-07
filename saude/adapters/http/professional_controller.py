from rest_framework import viewsets, status
from rest_framework.response import Response
from pydantic import ValidationError
from rest_framework.decorators import action
from saude.dtos.input.professional_input import CreateProfessionalInputDTO, UpdateProfessionalInputDTO
from saude.dtos.output.professional_output import ProfessionalOutputDTO
from saude.application.professional_service import ProfessionalService
from saude.dtos.output.professional_serializer import ProfessionalOutputSerializer
from saude.adapters.sqlite.professional_repository import ProfessionalRepository
from saude.application.i_professional_service import IProfessionalService


class ProfessionalController(viewsets.ViewSet):
    service = None or ProfessionalService(ProfessionalRepository())

    @action(detail=False, methods=['post'])
    def create_professional(self, request):
        try:
            professional = CreateProfessionalInputDTO(**request.data)
        except ValidationError as e:
            return Response({"error": e.errors()}, status=status.HTTP_400_BAD_REQUEST)

        created_professional = self.service.create_professional(professional)

        serializer = ProfessionalOutputSerializer(created_professional)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update_professional(self, request, id=None):
        pass

    @action(detail=False, methods=['get'])
    def list_professional(self, request, id=None):
        pass

    @action(detail=False, methods=['get'])
    def list_all_professionals(self, request):
        professionals = self.service.list_all_professionals()
        serializer = ProfessionalOutputSerializer(professionals, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete_professional(self, request, id=None):
        pass
