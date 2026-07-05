from fastapi import APIRouter
 
router = APIRouter()
 
 
@router.get("/documents")
def list_documents_placeholder():
    return {"message": "documents router works"}