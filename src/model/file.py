from mongoengine import Document, StringField, IntField

class Document(Document):
    customerId= StringField(required=True)
    documentId= IntField(required=True)
    documentPath= StringField(required=True)
    documentFileName= StringField(required=True)
    mimeType= StringField(required=True)
    lastUpdatedAt= StringField()
    uploadedAt= StringField(required=True)
    uploadedByUserId= StringField(required=True)
