from typing import List
from saude.dtos.input.professional_input import CreateProfessionalInputDTO, UpdateProfessionalInputDTO
from saude.dtos.output.professional_output import ProfessionalOutputDTO
from saude.application.i_professional_service import IProfessionalService
from saude.ports.outbound.i_professional_repository import IProfessionalRepository
from uuid import UUID


class ProfessionalService(IProfessionalService):
    def __init__(self, repository: IProfessionalRepository):
        self.repository = repository

    def create_professional(self, professional: CreateProfessionalInputDTO) -> ProfessionalOutputDTO:
        pass

    def update_professional(self, professional_id: UUID, professional: UpdateProfessionalInputDTO) -> ProfessionalOutputDTO:
        pass

    def list_professional(self, professional_id: UUID) -> ProfessionalOutputDTO:
        pass

    def list_all_professionals(self) -> List[ProfessionalOutputDTO]:
        pass

    def delete_professional(self, professional_id: UUID) -> ProfessionalOutputDTO:
        pass
