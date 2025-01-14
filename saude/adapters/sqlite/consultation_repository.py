from typing import List
from saude.dtos.input.consultation_input import CreateConsultationInputDTO, UpdateConsultationInputDTO
from saude.dtos.output.consultation_output import ConsultationOutputDTO
from saude.ports.outbound.i_consultation_repository import IConsultationRepository
from uuid import UUID


class ConsultationRepository(IConsultationRepository):

    def create_consultation(self, consultation: CreateConsultationInputDTO) -> ConsultationOutputDTO:
        pass

    def update_consultation(self, consultation_id: UUID, consultation: UpdateConsultationInputDTO) -> ConsultationOutputDTO:
        pass

    def list_consultation(self, consultation_id: UUID) -> ConsultationOutputDTO:
        pass

    def list_all_consultations(self) -> List[ConsultationOutputDTO]:
        pass

    def delete_consultation(self, consultation_id: UUID) -> ConsultationOutputDTO:
        pass
