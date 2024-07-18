# pylint: disable=E1102

from typing import List, Any
import yaml
from app.src.core.interface import IParameterConfig

class FileParameterConfig(IParameterConfig):
    def __init__(self, file_path):
        """
        Inicializa uma nova instância da classe FileParameterConfig.

        Args:
            file_path (str): O caminho para o arquivo.
        """
        self.__file_path: str = file_path

    def __load_config_yaml(self) -> Any:
        """
        Carrega o arquivo de configuração YAML e retorna os dados parseados.
        Retorna:
            dict: Os dados parseados do arquivo de configuração YAML.

        Lança:
            FileNotFoundError: Se o arquivo de configuração não for encontrado.
            yaml.YAMLError: Se houver um erro ao parsear o arquivo YAML.
        """
        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                return yaml.safe_load(file)
        except FileNotFoundError as error:
            raise FileNotFoundError(
                f"Arquivo de configuração '{self.__file_path}' não encontrado.") from error
        except yaml.YAMLError as error:
            raise yaml.YAMLError(f"Erro ao parsear o arquivo YAML '{self.__file_path}'.") from error

    def get_valid_tables_name(self) -> List[str]:
        """
        Recupera os nomes das tabelas válidas do arquivo de configuração
        Retorna:
            Um dicionário contendo os nomes das tabelas válidas.
        
        Raises:
            KeyError: Se a chave 'tables_to_watch' não for encontrada no arquivo de configuração.
        """
        data: Any = self.__load_config_yaml()
        if "tables_to_watch" not in data:
            raise KeyError("A chave 'tables_to_watch' não foi encontrada "
                           "no arquivo de configuração.")
        return data["tables_to_watch"]
    