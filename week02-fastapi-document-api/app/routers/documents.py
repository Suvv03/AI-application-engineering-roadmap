from fastapi import APIRouter
from app.schemas.document_schema import DocumentListResponse
 
router = APIRouter()
 
 
@router.get("/documents", response_model=DocumentListResponse)
def list_documents_placeholder():
    return {"documents": [], "total": 0}