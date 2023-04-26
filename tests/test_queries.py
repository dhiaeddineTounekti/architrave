from src.model.documentStatusSchema import Status
from src.service.documentStatusQueries import get_document_ids_with_extraction_status_by_customer_id, \
    get_document_ids_with_failed_ingestion_status_by_customer_id
from src.service.documentQueries import get_documents_summary
from tests.conftest import CUSTOMER_1, CUSTOMER_2


def sorting_key(dictionary: dict):
    return dictionary["_id"]["customerId"], dictionary["_id"]["mimeType"]


def test_get_document_ids_with_extraction_status_by_customer_id(connect_to_db):
    document_ids = list(get_document_ids_with_extraction_status_by_customer_id(f"{CUSTOMER_1}"))
    assert document_ids == [1, 2]


def test_get_document_ids_with_failed_ingestion_status_by_customer_id(connect_to_db):
    document_ids = list(get_document_ids_with_failed_ingestion_status_by_customer_id(f"{CUSTOMER_1}"))
    assert document_ids == [1, 4]


def test_get_documents_sammury(connect_to_db):
    documents_sammury = sorted(list(get_documents_summary()), key=sorting_key)
    expected_result =  [
        {
            "_id": {
                "customerId": f"{CUSTOMER_1}",
                "mimeType": "application/pdf",
                "status": f"{Status.FAILED}"
            },
            "count": 1
        }, {
            "_id": {
                "customerId": f"{CUSTOMER_1}",
                "mimeType": "application/text",
                "status": f"{Status.SUCCEEDED}"
            },
            "count": 1
        }, {
            "_id": {
                "customerId": f"{CUSTOMER_2}",
                "mimeType": "application/pdf",
                "status": f"{Status.FAILED}"
            },
            "count": 1
        }, {
            "_id": {
                "customerId": f"{CUSTOMER_2}",
                "mimeType": "application/text",
                "status": f"{Status.SUCCEEDED}"
            },
            "count": 1
        }
    ]
    assert documents_sammury == sorted(expected_result, key=sorting_key)
