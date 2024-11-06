from abc import ABC, abstractmethod
from typing import List
from saude.dtos.input.professional_input import CreateProfessionalInputDTO, UpdateProfessionalInputDTO
from saude.dtos.output.professional_output import ProfessionalOutputDTO


class IProfessionalRepository(ABC):

    @abstractmethod
    def create_professional(self, professional: CreateProfessionalInputDTO) -> ProfessionalOutputDTO:
        pass

    @abstractmethod
    def update_professional(self, professional: UpdateProfessionalInputDTO) -> ProfessionalOutputDTO:
        pass

    @abstractmethod
    def list_professional(self) -> ProfessionalOutputDTO:
        pass

    @abstractmethod
    def list_all_professionals(self) -> List[ProfessionalOutputDTO]:
        pass

    @abstractmethod
    def delete_professional(self) -> ProfessionalOutputDTO:
        pass
