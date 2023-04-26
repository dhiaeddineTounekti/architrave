from typing import List

from src.model.documentStatusSchema import Status
from src.model.documentschema import DocumentSchema


def get_documents_summary() -> List:
    """
    Returns a list of dictionaries with the following structure:
    [
        {
            '_id': {
                'customerId': 'id1',
                'mimeType': 'application/pdf',
                'Status': 'SUCCEEDED'
            },
            'count': 1
        },
        {
            '_id': {
                'customerId': 'id2',
                'mimeType': 'application/pdf',
                'Status': 'FAILED'
            },
            'count': 1
        },...
    ]
    It is guaranteed that for every mimeType there will be a SUCCEEDED and a FAILED status
    Not every customer id will have stats about every mimeType in the database.
    If a customer id does not have stats for a mimeType, that means that the customer id has no documents of that mimeType. So the stats could be considered as 0.
    """
    pipeline = \
        [
            {
                # This lookup joins the document collection with the documentStatus collection on the customerId and documentId fields
                # and only include documents that either have both IngestionStatus and extractionStatus as SUCCEEDED or both as FAILED
                "$lookup": {
                    "from": "document_status",
                    "let": {
                        "documentCustomerId": "$customerId",
                        "documentDocumentId": "$documentId"
                    },
                    "pipeline": [
                        {
                            "$match": {
                                "$expr": {
                                    "$and": [
                                        {
                                            "$eq": [
                                                "$customerId",
                                                "$$documentCustomerId"
                                            ]
                                        },
                                        {
                                            "$eq": [
                                                "$documentId",
                                                "$$documentDocumentId"
                                            ]
                                        },
                                        {
                                            "$or": [
                                                {
                                                    "$and": [
                                                        {
                                                            "$eq": [
                                                                "$ingestionStatus",
                                                                f"{Status.SUCCEEDED}"
                                                            ]
                                                        },
                                                        {
                                                            "$eq": [
                                                                "$extractionStatus",
                                                                f"{Status.SUCCEEDED}"
                                                            ]
                                                        },

                                                    ]
                                                },
                                                {
                                                    "$and": [
                                                        {
                                                            "$eq": [
                                                                "$ingestionStatus",
                                                                f"{Status.FAILED}"
                                                            ]
                                                        },
                                                        {
                                                            "$eq": [
                                                                "$extractionStatus",
                                                                f"{Status.FAILED}"
                                                            ]
                                                        },

                                                    ]
                                                },

                                            ]
                                        }
                                    ]
                                }
                            }
                        }
                    ],
                    "as": "documentInfo",

                },

            },
            {
                "$unwind": "$documentInfo",

            },
            {
                "$group": {
                    "_id": {
                        "customerId": "$customerId",
                        "mimeType": "$mimeType",
                        "status": "$documentInfo.ingestionStatus",
                        # This is the same value as "$documentInfo.extractionStatus", no need to include both.

                    },
                    "count": {
                        "$sum": 1
                    }
                }
            },

        ]
    return DocumentSchema.objects.aggregate(pipeline)
