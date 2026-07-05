from fastapi import FastAPI
from app.routers import documents
 
app = FastAPI(
    title="Document Management API",
    version="0.1.0",
    description="A FastAPI service for document upload, preprocessing and management."
)
 
app.include_router(documents.router, tags=["documents"])
 
 
@app.get("/health")
def health_check():
    return {"status": "ok"}