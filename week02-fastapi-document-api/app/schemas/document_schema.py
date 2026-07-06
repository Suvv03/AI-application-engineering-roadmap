from pydantic import BaseModel
from typing import Optional
 
 
class DocumentResponse(BaseModel):
    doc_id: str
    filename: str
    content_type: Optional[str] = None
    raw_path: str
    chunk_path: str
    chunk_count: int
    created_at: str
 
 
class UploadResponse(BaseModel):
    doc_id: str
    filename: str
    chunk_count: int
    message: str
 
 
class DocumentListResponse(BaseModel):
    documents: list[DocumentResponse]
    total: int
 
 
class DeleteResponse(BaseModel):
    doc_id: str
    message: str
 
 
class ErrorResponse(BaseModel):
    detail: str