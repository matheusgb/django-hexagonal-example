from typing import List
from uuid import UUID, uuid4
from datetime import datetime
from saude.ports.outbound.i_professional_repository import IProfessionalRepository
from saude.dtos.input.professional_input import CreateProfessionalInputDTO, UpdateProfessionalInputDTO
from saude.dtos.output.professional_output import ProfessionalOutputDTO
from saude.domain.entities.professional_entity import ProfessionalEntity


class ProfessionalRepository(IProfessionalRepository):

    def create_professional(self, professional: CreateProfessionalInputDTO) -> ProfessionalOutputDTO:
        professional_entity = ProfessionalEntity(
            id=uuid4(),
            name=professional.name,
            social_name=professional.social_name,
            profession=professional.profession,
            address=professional.address,
            phone_number=professional.phone_number,
            email=professional.email,
        )

        professional_entity.save()

        created_professional = ProfessionalOutputDTO(
            id=professional_entity.id,
            name=professional_entity.name,
            social_name=professional_entity.social_name,
            profession=professional_entity.profession,
            address=professional_entity.address,
            phone_number=professional_entity.phone_number,
            email=professional_entity.email,
            created_at=professional_entity.created_at,
            updated_at=professional_entity.updated_at
        )
        return created_professional

    def update_professional(self, professional_id: UUID, professional: UpdateProfessionalInputDTO) -> ProfessionalOutputDTO:
        pass

    def list_professional(self, professional_id: UUID) -> ProfessionalOutputDTO:
        pass

    def list_all_professionals(self) -> List[ProfessionalOutputDTO]:
        pass

    def delete_professional(self, professional_id: UUID) -> ProfessionalOutputDTO:
        pass
