import json
from pathlib import Path


REQUIRED_FIELDS = {
    "chunk_id",
    "source_file",
    "text",
    "char_start",
    "char_end",
}


def load_chunks(file_path: Path) -> list[dict]:
    """Load chunks and ensure the metadata needed for retrieval is present."""
    if not file_path.exists():
        raise FileNotFoundError(f"找不到 chunks 文件：{file_path}")

    with file_path.open("r", encoding="utf-8") as file:
        chunks = json.load(file)

    if not isinstance(chunks, list):
        raise ValueError("chunks.json 最外层必须是列表")

    for index, chunk in enumerate(chunks):
        if not isinstance(chunk, dict):
            raise ValueError(f"第 {index + 1} 个 chunk 必须是对象")

        missing_fields = REQUIRED_FIELDS - chunk.keys()
        if missing_fields:
            raise ValueError(f"第 {index + 1} 个 chunk 缺少字段：{missing_fields}")

        if not isinstance(chunk["text"], str) or not chunk["text"].strip():
            raise ValueError(f"第 {index + 1} 个 chunk 的 text 为空")

    return chunks
