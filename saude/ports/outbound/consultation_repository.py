from abc import ABC, abstractmethod
from typing import List
from saude.dtos.input.consultation_input import ConsultationInputDTO
from saude.dtos.output.consultation_output import ConsultationOutputDTO


class IConsultationRepository(ABC):

    @abstractmethod
    def create_consultation(self, consultation: ConsultationInputDTO) -> ConsultationOutputDTO:
        pass

    @abstractmethod
    def update_consultation(self, consultation: ConsultationInputDTO) -> ConsultationOutputDTO:
        pass

    @abstractmethod
    def list_consultation(self, consultation: ConsultationInputDTO) -> ConsultationOutputDTO:
        pass

    @abstractmethod
    def list_all_consultations(self) -> List[ConsultationOutputDTO]:
        pass

    @abstractmethod
    def delete_consultation(self, consultation: ConsultationInputDTO) -> ConsultationOutputDTO:
        pass
