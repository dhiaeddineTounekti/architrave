from typing import List

from src.model.documentStatusSchema import DocumentStatusSchema, Status


def get_document_ids_with_extraction_status_by_customer_id(customer_id: str) -> List:
    return DocumentStatusSchema.objects(extractionStatus=f"{Status.FAILED}", customerId=customer_id).values_list("documentId")


def get_document_ids_with_failed_ingestion_status_by_customer_id(customer_id: str) -> List:
    return DocumentStatusSchema.objects(ingestionStatus=f"{Status.FAILED}", customerId=customer_id).values_list("documentId")
