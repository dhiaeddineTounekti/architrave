import os
from uuid import uuid4

from pymongo_inmemory import MongoClient
import pytest
from mongoengine import connect, disconnect
from src.index import create_app

from src.model.documentStatusSchema import Status

DATABASE_NAME = "test"
CUSTOMER_1 = uuid4()
CUSTOMER_2 = uuid4()


@pytest.fixture(scope="module", autouse=True)
def prepare_db():
    client = MongoClient()
    db = client[DATABASE_NAME]
    db["document_status"].insert_many([
        {"customerId": f"{CUSTOMER_1}", "documentId": 1, "ingestionStatus": f"{Status.FAILED}",
         "extractionStatus": f"{Status.FAILED}"},
        {"customerId": f"{CUSTOMER_1}", "documentId": 2, "ingestionStatus": f"{Status.SUCCEEDED}",
         "extractionStatus": f"{Status.FAILED}"},
        {"customerId": f"{CUSTOMER_1}", "documentId": 3, "ingestionStatus": f"{Status.SUCCEEDED}",
         "extractionStatus": f"{Status.SUCCEEDED}"},
        {"customerId": f"{CUSTOMER_1}", "documentId": 4, "ingestionStatus": f"{Status.FAILED}",
         "extractionStatus": f"{Status.SUCCEEDED}"},
        {"customerId": f"{CUSTOMER_2}", "documentId": 1, "ingestionStatus": f"{Status.FAILED}",
         "extractionStatus": f"{Status.FAILED}"},
        {"customerId": f"{CUSTOMER_2}", "documentId": 2, "ingestionStatus": f"{Status.SUCCEEDED}",
         "extractionStatus": f"{Status.FAILED}"},
        {"customerId": f"{CUSTOMER_2}", "documentId": 3, "ingestionStatus": f"{Status.FAILED}",
         "extractionStatus": f"{Status.SUCCEEDED}"},
        {"customerId": f"{CUSTOMER_2}", "documentId": 4, "ingestionStatus": f"{Status.SUCCEEDED}",
         "extractionStatus": f"{Status.SUCCEEDED}"},
    ])
    db["document"].insert_many([
        {"customerId": f"{CUSTOMER_1}", "documentId": 1, "mimeType": "application/pdf"},
        {"customerId": f"{CUSTOMER_1}", "documentId": 2, "mimeType": "application/pdf"},
        {"customerId": f"{CUSTOMER_1}", "documentId": 3, "mimeType": "application/text"},
        {"customerId": f"{CUSTOMER_1}", "documentId": 4, "mimeType": "application/text"},
        {"customerId": f"{CUSTOMER_2}", "documentId": 1, "mimeType": "application/pdf"},
        {"customerId": f"{CUSTOMER_2}", "documentId": 2, "mimeType": "application/pdf"},
        {"customerId": f"{CUSTOMER_2}", "documentId": 3, "mimeType": "application/text"},
        {"customerId": f"{CUSTOMER_2}", "documentId": 4, "mimeType": "application/text"},
    ])

    yield

    client.drop_database(DATABASE_NAME)
    client.close()


@pytest.fixture(scope="module")
def connect_to_db():
    connect(DATABASE_NAME)

    yield

    disconnect()


@pytest.fixture(scope="module")
def client():
    os.environ["DB_URLS"] = f"mongodb://localhost:27017/{DATABASE_NAME}"
    app = create_app()
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client
