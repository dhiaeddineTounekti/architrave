from flask import Flask

from src.service.documentQueries import get_documents_summary
from src.service.documentStatusQueries import get_document_ids_with_extraction_status_by_customer_id, \
    get_document_ids_with_failed_ingestion_status_by_customer_id
from src.utils.dbConnector import connect_to_dbs
from src.utils.requestValidator import is_valid_customer_id


def create_app():
    app = Flask(__name__)
    connect_to_dbs()

    @app.route('/document_summary')
    def document_summary():
        return list(get_documents_summary()), 200

    @app.route('/<customer_id>/documents/ingestionStatus/failed')
    def documents_failed_ingestion(customer_id):
        if not is_valid_customer_id(customer_id):
            return "Invalid customerId", 400

        return list(get_document_ids_with_failed_ingestion_status_by_customer_id(customer_id)), 200

    @app.route('/<customer_id>/documents/extractionStatus/failed')
    def documents_failed_extraction(customer_id):
        if not is_valid_customer_id(customer_id):
            return "Invalid customerId", 400

        return list(get_document_ids_with_extraction_status_by_customer_id(customer_id)), 200

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='localhost', port=80)
