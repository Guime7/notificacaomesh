# pylint: disable=W0718:broad-exception-caught
# pylint: disable=W0613:unused-argument
# pylint: disable=W0611:unused-import

import os
import json
from typing import Dict, Any
from app.src.entrypoint.notification_app import NotificationApp
from app.src.core.models.datamesh_notification import DatameshNotification

def lambda_handler(event: Dict[str, Any], context: Any):
    try:
        queue_url: str = os.environ.get('SQS_QUEUE_URL')
        notification_app: NotificationApp = NotificationApp(queue_url)

        record: DatameshNotification = event
        codigo_identificador_evento: str = record['codigo_identificador_evento']

        notification_app.processar(record)

        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Processamento realizado com sucesso!',
                'codigo_identificador_evento': codigo_identificador_evento
            })
        }
    except Exception as error:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'message': 'Erro ao processar a mensagem',
                'codigo_identificador_evento': record.get('codigo_identificador_evento', 'N/A'),
                'error': str(error)
            })
        }
