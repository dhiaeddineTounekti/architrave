from tests.conftest import CUSTOMER_1


def test_document_summary(client):
    result = client.get('/document_summary')
    assert result.status_code == 200


def test_documents_failed_ingestion(client):
    result = client.get(f'/{CUSTOMER_1}/documents/ingestionStatus/failed')
    assert result.status_code == 200
    assert result.json == [1, 4]


def test_documents_failed_extraction(client):
    result = client.get(f'/{CUSTOMER_1}/documents/extractionStatus/failed')
    assert result.status_code == 200
    assert result.json == [1, 2]
