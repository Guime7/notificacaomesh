from typing import List
from abc import ABC, abstractmethod

class IParameterConfig(ABC):

    @abstractmethod
    def get_valid_tables_name(self) -> List[str]:
        """
        Retorna uma lista de nomes de tabelas válidas.

        :return: Uma lista de strings representando os nomes de tabelas válidas.
        """
