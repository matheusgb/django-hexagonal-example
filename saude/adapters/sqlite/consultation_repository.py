from typing import List
from saude.dtos.input.consultation_input import CreateConsultationInputDTO, UpdateConsultationInputDTO
from saude.dtos.output.consultation_output import ConsultationOutputDTO
from saude.ports.outbound.i_consultation_repository import IConsultationRepository


class ConsultationRepository(IConsultationRepository):

    def create_consultation(self, consultation: CreateConsultationInputDTO) -> ConsultationOutputDTO:
        pass

    def update_consultation(self, consultation: UpdateConsultationInputDTO) -> ConsultationOutputDTO:
        pass

    def list_consultation(self) -> ConsultationOutputDTO:
        pass

    def list_all_consultations(self) -> List[ConsultationOutputDTO]:
        pass

    def delete_consultation(self) -> ConsultationOutputDTO:
        pass
