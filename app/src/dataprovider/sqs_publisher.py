from mypy_boto3_sqs import SQSClient
from mypy_boto3_sqs.type_defs import SendMessageResultTypeDef
from botocore.exceptions import ClientError
from app.src.core.interface import IPublisher
from app.src.core.models.adapter_event_publish import AdapterEventPublish

class SQSPublisher(IPublisher):
    def __init__(self, client: SQSClient, queue_url: str) -> None:
        """
        Inicializa a classe SQSPublisher.

        Este método configura os componentes necessários para publicar mensagens no SQS.

        Args:
            client (SQSClient): Cliente do SQS.
            queue_url (str): URL da fila do SQS.

        Returns:
            None
        """
        self.__client: SQSClient = client
        self.__queue_url: str = queue_url

    def publish_event(self, message: AdapterEventPublish) -> SendMessageResultTypeDef:
        """
        Publica um evento na fila SQS.

        Args:
            message (AdapterEventPublish): A mensagem a ser publicada na fila.

        Returns:
            SendMessageResultTypeDef: O resultado da operação de envio de mensagem.
        
        Lança:
            ClientError: Se houver um erro ao enviar a mensagem.
        """
        try:
            response: SendMessageResultTypeDef = self.__client.send_message(
                QueueUrl=self.__queue_url,
                MessageBody=str(message)
            )
            return response
        except ClientError as error:
            raise error
