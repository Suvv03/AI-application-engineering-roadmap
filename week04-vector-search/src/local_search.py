import numpy as np

from config import CHUNKS_PATH, EMBEDDINGS_PATH
from data_loader import load_chunks
from embedding_service import EmbeddingService


def search_local(query: str, top_k: int = 3) -> list[dict]:
    """Return the chunks most similar to a query using local NumPy search."""
    if not query.strip():
        raise ValueError("查询内容不能为空")

    if top_k < 1:
        raise ValueError("top_k 必须至少为 1")

    chunks = load_chunks(CHUNKS_PATH)

    if not EMBEDDINGS_PATH.exists():
        raise FileNotFoundError(
            f"找不到向量文件：{EMBEDDINGS_PATH}，请先运行 build_embeddings.py"
        )

    embeddings = np.load(EMBEDDINGS_PATH)

    if embeddings.ndim != 2:
        raise ValueError("embeddings.npy 必须是二维数组")

    if len(chunks) != len(embeddings):
        raise ValueError(
            "chunks 数量与 embeddings 数量不一致，请重新运行 build_embeddings.py"
        )

    embedding_service = EmbeddingService()
    query_embedding = embedding_service.encode_query(query)

    if embeddings.shape[1] != query_embedding.shape[0]:
        raise ValueError(
            "查询向量维度与文档向量维度不一致，请重新运行 build_embeddings.py"
        )

    # Vectors are normalized, so the dot product equals cosine similarity.
    scores = embeddings @ query_embedding
    actual_top_k = min(top_k, len(chunks))
    top_indices = np.argsort(scores)[::-1][:actual_top_k]

    results = []
    for rank, index in enumerate(top_indices, start=1):
        chunk = chunks[int(index)]
        results.append(
            {
                "rank": rank,
                "score": float(scores[index]),
                "chunk_id": chunk["chunk_id"],
                "source_file": chunk["source_file"],
                "text": chunk["text"],
            }
        )

    return results


def main() -> None:
    query = input("请输入检索问题：").strip()
    results = search_local(query=query, top_k=3)

    print("\n检索结果：")
    for result in results:
        print("\n" + "=" * 70)
        print(f"排名：{result['rank']}")
        print(f"相似度：{result['score']:.4f}")
        print(f"Chunk ID：{result['chunk_id']}")
        print(f"来源文件：{result['source_file']}")
        print(f"文本：{result['text'][:300]}")


if __name__ == "__main__":
    main()
