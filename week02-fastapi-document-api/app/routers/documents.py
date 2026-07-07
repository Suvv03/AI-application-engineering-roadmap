from fastapi import APIRouter, File, HTTPException, UploadFile
 
from app.schemas.document_schema import UploadResponse, DocumentListResponse
from app.services.document_service import save_uploaded_file_only
from app.services.storage_service import load_documents
from app.core.config import DB_PATH
 
router = APIRouter()
 
 
@router.post("/upload", response_model=UploadResponse)
async def upload_document(file: UploadFile = File(...)):
    try:
        record = await save_uploaded_file_only(file)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))
 
    return {
        "doc_id": record["doc_id"],
        "filename": record["filename"],
        "chunk_count": record["chunk_count"],
        "message": "File uploaded successfully. Preprocessing will be added on Day 4."
    }
 
 
@router.get("/documents", response_model=DocumentListResponse)
def list_documents():
    documents = load_documents(DB_PATH)
    return {"documents": documents, "total": len(documents)}