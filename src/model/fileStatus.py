from dataclasses import dataclass

@dataclass
class DocumentStatus:
    customerId: str
    documentId: int
    documentContentHash: str
    documentMetadataHash: str
    IngestionStatus: str
    extractionStatus: str
    logs: str