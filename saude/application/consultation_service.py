from typing import List
from saude.dtos.input.consultation_input import CreateConsultationInputDTO, UpdateConsultationInputDTO
from saude.dtos.output.consultation_output import ConsultationOutputDTO
from saude.application.i_consultation_service import IConsultationService
from saude.ports.outbound.i_consultation_repository import IConsultationRepository


class ConsultationService(IConsultationService):
    def __init__(self, repository: IConsultationRepository):
        self.repository = repository

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
