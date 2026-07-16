import numpy as np

from config import CHUNKS_PATH, EMBEDDING_DIM
from data_loader import load_chunks
from embedding_service import EmbeddingService


def main() -> None:
    chunks = load_chunks(CHUNKS_PATH)

    print(f"读取到 {len(chunks)} 个 chunks")
    print(f"测试 chunk：{chunks[0]['chunk_id']}")

    embedding_service = EmbeddingService()
    embeddings = embedding_service.encode_documents([chunks[0]["text"]])

    if embeddings.shape != (1, EMBEDDING_DIM):
        raise ValueError(
            f"向量维度不符合预期：{embeddings.shape}，期望为 (1, {EMBEDDING_DIM})"
        )

    print("向量数组形状：", embeddings.shape)
    print("单条向量维度：", embeddings[0].shape)
    print("向量前 10 个数值：", embeddings[0][:10])
    print("向量长度：", np.linalg.norm(embeddings[0]))


if __name__ == "__main__":
    main()
