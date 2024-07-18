import boto3
from mypy_boto3_sqs import SQSClient
from app.src.core.models.datamesh_notification import DatameshNotification
from app.src.dataprovider.file_parameter_config import FileParameterConfig
from app.src.dataprovider.sqs_publisher import SQSPublisher

# Importa as classes necessárias
from app.src.core.application.use_cases.handler_event_use_case import HandlerEventUseCase

class NotificationApp():
    def __init__(self, queue_url) -> None:
        """
        Inicializa a classe Notification.

        Este método configura os componentes necessários para lidar com notificações.

        Args:
            None

        Returns:
            None
        """

        # Cliente do SQS
        sqs_client: SQSClient = boto3.client("sqs", region_name="sa-east-1")
        self.__publisher: SQSPublisher = SQSPublisher(
            client=sqs_client,
            queue_url=queue_url)

        # Configuração de parâmetros (atualmente arquivo)
        self.__parameter_config: FileParameterConfig = FileParameterConfig(
            file_path="app/config.yaml")

        # UseCase - tratamento de eventos
        self.__handler_event: HandlerEventUseCase = HandlerEventUseCase(
            parameter_config=self.__parameter_config,
            publisher=self.__publisher
        )

    def processar(self, record: DatameshNotification) -> None:
        """
        Processa o evento recebido.

        Args:
            record (DatameshNotification): O registro a ser processado.

        Returns:
            None
        """
        self.__handler_event.handle(record)
