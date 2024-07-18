# pylint: disable=C0301:line-too-long

from typing import TypedDict

class DatameshNotification(TypedDict):
    """
    Tipo que define a estrutura de uma notificação Datamesh.
    """
    codigo_identificador_evento: str  # Identificador do evento original
    codigo_identificador_evento_tratada: str  # Identificador do evento tratado via plataforma de notificação
    nome_escopo: str  # Para todos os eventos com exceção de DataLoad preenchimento igual a "aws.glue"
    nome_acao: str  # Opções DataLoad, BatchCreatePartition, CreatePartition e outros de criação da tabela não relevantes para o escopo
    descricao_carga: str  # Apenas no DataLoad quando especificado
    nome_base: str  # Nome do database
    nome_tabela_evento: str  # Nome da tabela
    nome_particao: str  # Nome da partição, preenchido apenas no DataLoad
    codigo_particao: str  # Valores da partição, vem sempre como string, em caso de partição composta é separado por vírgula "[2023, 5, 1]"
    data_hora_processamento: str  # Data e hora do processamento no catálogo de dados
