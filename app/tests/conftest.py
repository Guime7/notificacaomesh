# pylint: disable=E1101:no-member
# pylint: disable=W0621:redefined-outer-name
# pylint: disable=W0613:unused-argument

import os
import boto3
import pytest
from moto import mock_aws


#definir python path using sys.path.append
import sys
import os
#add root to python path
sys.path.append(os.path.join(os.path.dirname(__name__), '..'))
print(sys.path)

@pytest.fixture(name="aws_credentials", scope="session")
def aws_credentials():
    """Mocked AWS Credentials for moto."""
    os.environ["AWS_ACCESS_KEY_ID"] = "testing"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "testing"
    os.environ["AWS_SECURITY_TOKEN"] = "testing"
    os.environ["AWS_SESSION_TOKEN"] = "testing"
    os.environ["AWS_DEFAULT_REGION"] = "sa-east-1"

@pytest.fixture(name="s3_client", scope="session")
def s3_client(aws_credentials):
    with mock_aws():
        yield boto3.client("logs")
        
