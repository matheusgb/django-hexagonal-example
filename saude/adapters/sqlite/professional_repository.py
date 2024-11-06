from typing import List
from saude.ports.outbound.i_professional_repository import IProfessionalRepository
from saude.dtos.input.professional_input import CreateProfessionalInputDTO, UpdateProfessionalInputDTO
from saude.dtos.output.professional_output import ProfessionalOutputDTO
from uuid import UUID


class ProfessionalRepository(IProfessionalRepository):

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
