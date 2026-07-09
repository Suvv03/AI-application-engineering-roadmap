from fastapi import APIRouter, File, HTTPException, UploadFile
 
from app.schemas.document_schema import UploadResponse, DocumentListResponse
from app.services.document_service import process_uploaded_file
from app.services.storage_service import load_documents
from app.core.config import DB_PATH
 
from app.schemas.document_schema import DocumentResponse
from app.services.storage_service import get_document_by_id
from app.schemas.document_schema import DeleteResponse
from app.services.document_service import delete_document_and_files

router = APIRouter()
 
 
@router.post("/upload", response_model=UploadResponse)
async def upload_document(file: UploadFile = File(...)):
    try:
        record = await process_uploaded_file(file)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))
 
    return {
        "doc_id": record["doc_id"],
        "filename": record["filename"],
        "chunk_count": record["chunk_count"],
        "message": "File uploaded and preprocessed successfully."
    }
 
@router.get("/documents/{doc_id}", response_model=DocumentResponse)
def get_document(doc_id: str):
    document = get_document_by_id(doc_id, DB_PATH)
    if document is None:
        raise HTTPException(status_code=404, detail="Document not found.")
    return document
 
@router.get("/documents", response_model=DocumentListResponse)
def list_documents():
    documents = load_documents(DB_PATH)
    return {"documents": documents, "total": len(documents)}

@router.delete("/documents/{doc_id}", response_model=DeleteResponse)
def delete_document(doc_id: str):
    deleted = delete_document_and_files(doc_id)
    if deleted is None:
        raise HTTPException(status_code=404, detail="Document not found.")
    return {
        "doc_id": doc_id,
        "message": "Document deleted successfully."
    }