from dataclasses import dataclass

@dataclass
class Document:
    customerId: str
    documentId: int
    documentPath: str
    documentFileName: str
    mimeType: str
    lastUpdatedAt: str
    uploadedAt: str
    uploadedByUserId: str
