import json
from datetime import datetime
from pathlib import Path
from uuid import uuid4
from fastapi import UploadFile
 
from app.core.config import (
    CHUNK_OVERLAP,
    CHUNK_SIZE,
    DB_PATH,
    PROCESSED_DATA_DIR,
    RAW_DATA_DIR,
)
from app.services.preprocessing import clean_text, create_chunks_for_document
from app.services.storage_service import add_document
from app.services.storage_service import remove_document_by_id
 

 
def decode_text(contents: bytes) -> str:
    try:
        return contents.decode("utf-8")
    except UnicodeDecodeError:
        return contents.decode("gbk", errors="ignore")
 
 
async def process_uploaded_file(file: UploadFile) -> dict:
    filename = Path(file.filename or "uploaded.txt").name
 
    if not filename.lower().endswith(".txt"):
        raise ValueError("Only .txt files are supported in Week 02.")
 
    contents = await file.read()
    if not contents:
        raise ValueError("Uploaded file is empty.")
 
    doc_id = uuid4().hex[:12]
    stored_filename = f"{doc_id}_{filename}"
    raw_path = RAW_DATA_DIR / stored_filename
    chunk_path = PROCESSED_DATA_DIR / f"{doc_id}_chunks.json"
 
    raw_path.write_bytes(contents)
 
    text = decode_text(contents)
    cleaned_text = clean_text(text)
    document = {
        "source_file": filename,
        "text": cleaned_text
    }
    chunks = create_chunks_for_document(document, CHUNK_SIZE, CHUNK_OVERLAP)
 
    for chunk in chunks:
        chunk["doc_id"] = doc_id
 
    chunk_path.write_text(
        json.dumps(chunks, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )
 
    record = {
        "doc_id": doc_id,
        "filename": filename,
        "content_type": file.content_type,
        "raw_path": str(raw_path),
        "chunk_path": str(chunk_path),
        "chunk_count": len(chunks),
        "created_at": datetime.now().isoformat(timespec="seconds")
    }
    add_document(record, DB_PATH)
    return record


def delete_document_and_files(doc_id: str) -> dict | None:
    record = remove_document_by_id(doc_id, DB_PATH)
    if record is None:
        return None
 
    for path_key in ["raw_path", "chunk_path"]:
        path = Path(record[path_key])
        if path.exists():
            path.unlink()
 
    return record