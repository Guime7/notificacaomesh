# pylint: disable=W0719:broad-exception-raised

from typing import List
from mypy_boto3_sqs.type_defs import SendMessageResultTypeDef
from app.src.core.models.adapter_event_publish import AdapterEventPublish
from app.src.core.models.datamesh_notification import DatameshNotification
from app.src.core.interface import IParameterConfig, IPublisher

class HandlerEventUseCase():
    def __init__(self, parameter_config: IParameterConfig, publisher: IPublisher) -> None:
        """
        Inicializa a classe HandlerEventUseCase.

        Este método configura os componentes necessários para lidar com eventos.

        Args:
            parameter_config (ParameterConfig): Configuração de parâmetros.
            publisher (SqsPublisher): Publicador de mensagens.

        Returns:
            None
        """
        self.parameter_config: IParameterConfig = parameter_config
        self.publisher: IPublisher = publisher

    def handle(self, record: DatameshNotification) -> None:
        """
        Trata o evento recebido.

        Args:
            record (DatameshNotification): O registro a ser processado.

        Returns:
            None
        """
        #Recuperar configurações
        valid_tables: List[str] = self.parameter_config.get_valid_tables_name()

        #Verificar se a tabela é válida
        if f"{record['nome_base']}.{record['nome_tabela_evento']}" in valid_tables:
            #Adaptar evento
            data: AdapterEventPublish = self.__adapter_event(record)

            #Publicar evento
            response: SendMessageResultTypeDef = self.publisher.publish_event(data)
            if response["ResponseMetadata"]["HTTPStatusCode"] != 200:
                raise Exception("Erro ao publicar evento na fila.")

    def __adapter_event(self, record: DatameshNotification) -> AdapterEventPublish:
        """
        Adapta o evento recebido para o padrão da esteira de dados que é uma
        variação do BatchCreatePartition da AWS.

        Args:
            record (DatameshNotification): O registro a ser processado.

        Returns:
            AdapterEventPublish: O evento adaptado.
        """
        data: AdapterEventPublish = {
            "DatabaseName": str(record["nome_base"]),
            "TableName": str(record["nome_tabela_evento"]),
            "PartitionInputList": [
                {
                    "Values": [str(value.strip()) 
                            for value in
                            record["codigo_particao"].strip("[]").split(",")]
                }
            ]
        }

        return data
        