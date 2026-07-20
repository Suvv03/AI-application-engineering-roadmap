import json

import numpy as np

from config import (
    CHUNKS_PATH,
    EMBEDDINGS_PATH,
    EMBEDDING_META_PATH,
    MODEL_NAME,
)
from data_loader import load_chunks
from embedding_service import EmbeddingService


def main() -> None:
    chunks = load_chunks(CHUNKS_PATH)
    texts = [chunk["text"] for chunk in chunks]

    print(f"准备向量化 {len(texts)} 个 chunks")

    embedding_service = EmbeddingService()
    embeddings = embedding_service.encode_documents(texts)

    if len(embeddings) != len(chunks):
        raise ValueError("向量数量与 chunk 数量不一致")

    EMBEDDINGS_PATH.parent.mkdir(parents=True, exist_ok=True)

    np.save(EMBEDDINGS_PATH, embeddings)

    metadata = {
        "model_name": MODEL_NAME,
        "chunk_count": len(chunks),
        "embedding_count": len(embeddings),
        "embedding_dimension": int(embeddings.shape[1]),
        "normalized": True,
    }

    with EMBEDDING_META_PATH.open("w", encoding="utf-8") as file:
        json.dump(metadata, file, ensure_ascii=False, indent=2)

    print(f"向量形状：{embeddings.shape}")
    print(f"向量已保存：{EMBEDDINGS_PATH}")
    print(f"元数据已保存：{EMBEDDING_META_PATH}")


if __name__ == "__main__":
    main()
