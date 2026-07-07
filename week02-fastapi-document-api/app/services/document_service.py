from datetime import datetime
from pathlib import Path
from uuid import uuid4
from fastapi import UploadFile
 
from app.core.config import RAW_DATA_DIR, PROCESSED_DATA_DIR, DB_PATH
from app.services.storage_service import add_document
 
 
async def save_uploaded_file_only(file: UploadFile) -> dict:
    filename = Path(file.filename or "uploaded.txt").name
 
    if not filename.lower().endswith(".txt"):
        raise ValueError("Only .txt files are supported in Week 02.")
 
    contents = await file.read()
    if not contents:
        raise ValueError("Uploaded file is empty.")
 
    doc_id = uuid4().hex[:12]
    stored_filename = f"{doc_id}_{filename}"
    raw_path = RAW_DATA_DIR / stored_filename
    raw_path.write_bytes(contents)
 
    record = {
        "doc_id": doc_id,
        "filename": filename,
        "content_type": file.content_type,
        "raw_path": str(raw_path),
        "chunk_path": str(PROCESSED_DATA_DIR / f"{doc_id}_chunks.json"),
        "chunk_count": 0,
        "created_at": datetime.now().isoformat(timespec="seconds")
    }
    add_document(record, DB_PATH)
    return record