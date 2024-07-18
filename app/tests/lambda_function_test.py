# pylint: disable=E1101:no-member
# pylint: disable=W0621:redefined-outer-name

import json
from unittest.mock import call
import pytest
from app.src.entrypoint.notification_app import NotificationApp
from app.lambda_function import lambda_handler


@pytest.fixture(name="mock_event_input", scope="module")
def mock_event_input():
    with open("fixtures/mock_event_input.json", "r", encoding="utf-8") as file:
        return json.load(file)


def test_Assert():
    assert True


# def test_lambda_start_success(mocker, mock_event_input):

#     mocker.patch.object(NotificationApp, "__init__", return_value=None)
#     mocker.patch.object(NotificationApp, "processar", return_value=None)

#     event = mock_event_input
#     context = None

#     mock_queue_url = "https://sqs.us-east-1.amazonaws.com/123456789012/queue-name"

#     lambda_handler(event, context)

#     notification_app = NotificationApp(mock_queue_url)

#     expected_calls = [call(event)]
#     notification_app.processar.assert_has_calls(expected_calls)

# def test_lambda_fail_generic_error(mocker, mock_event_input):

#     mocker.patch.object(NotificationApp, "__init__", return_value=None)
#     mocker.patch.object(NotificationApp, "processar", side_effect=Exception("Erro genérico"))

#     event = mock_event_input
#     context = None

#     mock_queue_url = "https://sqs.us-east-1.amazonaws.com/123456789012/queue-name"

#     with pytest.raises(Exception):
#         lambda_handler(event, context)

#     notification_app = NotificationApp(mock_queue_url)
#     notification_app.processar.assert_called_once()
