from abc import ABC, abstractmethod
from typing import List
from saude.dtos.input.professional_input import ProfessionalInputDTO
from saude.dtos.output.professional_output import ProfessionalOutputDTO


class IProfessionalRepository(ABC):

    @abstractmethod
    def create_professional(self, professional: ProfessionalInputDTO) -> ProfessionalOutputDTO:
        pass

    @abstractmethod
    def update_professional(self, professional: ProfessionalInputDTO) -> ProfessionalOutputDTO:
        pass

    @abstractmethod
    def list_professional(self, professional: ProfessionalInputDTO) -> ProfessionalOutputDTO:
        pass

    @abstractmethod
    def list_all_professionals(self) -> List[ProfessionalOutputDTO]:
        pass

    @abstractmethod
    def delete_professional(self, professional: ProfessionalInputDTO) -> ProfessionalOutputDTO:
        pass
