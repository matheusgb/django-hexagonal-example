from abc import ABC, abstractmethod
from typing import List
from saude.dtos.input.consultation_input import CreateConsultationInputDTO, UpdateConsultationInputDTO
from saude.dtos.output.consultation_output import ConsultationOutputDTO
from uuid import UUID


class IConsultationService(ABC):

    @abstractmethod
    def create_consultation(self, consultation: CreateConsultationInputDTO) -> ConsultationOutputDTO:
        pass

    @abstractmethod
    def update_consultation(self, consultation_id: UUID, consultation: UpdateConsultationInputDTO) -> ConsultationOutputDTO:
        pass

    @abstractmethod
    def list_consultation(self, consultation_id: UUID) -> ConsultationOutputDTO:
        pass

    @abstractmethod
    def list_all_consultations(self) -> List[ConsultationOutputDTO]:
        pass

    @abstractmethod
    def delete_consultation(self, consultation_id: UUID) -> ConsultationOutputDTO:
        pass
