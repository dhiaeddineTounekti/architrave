from uuid import uuid4
from mongoengine import Document, StringField, IntField


class DocumentSchema(Document):
    customerId = StringField(required=True)
    documentId = IntField(required=True)
    documentPath = StringField(required=True)
    documentFileName = StringField(required=True)
    mimeType = StringField(required=True)
    lastUpdatedAt = StringField()
    uploadedAt = StringField(required=True)
    uploadedByUserId = StringField(required=True)

    meta = {
        'collection': 'document',
        'indexes': [
            ('customerId', 'documentId'),
        ]
    }
