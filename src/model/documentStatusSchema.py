from mongoengine import Document, StringField, IntField, EnumField
from enum import Enum


class Status(Enum):
    FAILED = "FAILED"
    SUCCEEDED = "SUCCEEDED"
    STARTED = "STARTED"

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_


class DocumentStatusSchema(Document):
    customerId = StringField(required=True)
    documentId = IntField(required=True)
    documentContentHash = StringField()
    documentMetadataHash = StringField()
    ingestionStatus = EnumField(Status)
    extractionStatus = EnumField(Status)
    logs = StringField()

    meta = {
        'collection': 'document_status',
        'indexes': [
            'ingestionStatus',
            'extractionStatus',
        ]
    }
