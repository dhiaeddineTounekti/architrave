from mongoengine import Document, StringField, IntField


class DocumentStatus(Document):
    customerId= StringField(required=True)
    documentId= IntField(required=True)
    documentContentHash= StringField()
    documentMetadataHash= StringField()
    IngestionStatus= StringField()
    extractionStatus= StringField()
    logs= StringField()