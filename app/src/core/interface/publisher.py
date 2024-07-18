from abc import ABC, abstractmethod
from mypy_boto3_sqs.type_defs import SendMessageResultTypeDef
from app.src.core.models.adapter_event_publish import AdapterEventPublish

class IPublisher(ABC):
    @abstractmethod
    def publish_event(self, message: AdapterEventPublish) -> SendMessageResultTypeDef:
        """
        Publica um evento na fila.

        Args:
            message (AdapterEventPublish): A mensagem a ser publicada.
            
        Returns:
            SendMessageResultTypeDef: O resultado da publicação do evento.
        """
