import json
from pathlib import Path
from typing import Optional
 
 
def load_documents(db_path: Path) -> list[dict]:
    if not db_path.exists():
        return []
    text = db_path.read_text(encoding="utf-8").strip()
    if not text:
        return []
    return json.loads(text)
 
 
def save_documents(documents: list[dict], db_path: Path) -> None:
    db_path.parent.mkdir(parents=True, exist_ok=True)
    db_path.write_text(
        json.dumps(documents, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )
 
 
def get_document_by_id(doc_id: str, db_path: Path) -> Optional[dict]:
    documents = load_documents(db_path)
    for document in documents:
        if document["doc_id"] == doc_id:
            return document
    return None
 
 
def add_document(record: dict, db_path: Path) -> None:
    documents = load_documents(db_path)
    documents.append(record)
    save_documents(documents, db_path)
 
 
def remove_document_by_id(doc_id: str, db_path: Path) -> Optional[dict]:
    documents = load_documents(db_path)
    target = None
    remaining = []
    for document in documents:
        if document["doc_id"] == doc_id:
            target = document
        else:
            remaining.append(document)
    if target is not None:
        save_documents(remaining, db_path)
    return target