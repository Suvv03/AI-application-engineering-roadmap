import re
 
 
def remove_extra_spaces(text: str) -> str:
    text = re.sub(r"[ ]+", " ", text)
    return text
 
 
def remove_extra_blank_lines(text: str) -> str:
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text
 
 
def clean_text(text: str) -> str:
    text = remove_extra_spaces(text)
    text = remove_extra_blank_lines(text)
    return text.strip()
 
 
def chunk_text(text: str, chunk_size: int, overlap: int):
    if overlap >= chunk_size:
        raise ValueError("overlap must be smaller than chunk_size")
 
    chunks = []
    start = 0
    text_length = len(text)
 
    while start < text_length:
        end = min(start + chunk_size, text_length)
        chunk = text[start:end].strip()
        if chunk:
            chunks.append({
                "text": chunk,
                "char_start": start,
                "char_end": end
            })
        start += chunk_size - overlap
 
    return chunks
 
 
def create_chunks_for_document(document: dict, chunk_size: int, overlap: int):
    raw_chunks = chunk_text(document["text"], chunk_size, overlap)
    results = []
    for idx, chunk in enumerate(raw_chunks, start=1):
        results.append({
            "chunk_id": f"{document['source_file']}_{idx:04d}",
            "source_file": document["source_file"],
            **chunk
        })
    return results