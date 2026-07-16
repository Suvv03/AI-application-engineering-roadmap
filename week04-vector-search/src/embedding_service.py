import numpy as np
from sentence_transformers import SentenceTransformer

from config import MODEL_NAME


class EmbeddingService:
    """Encode E5 queries and passages as normalized dense vectors."""

    def __init__(self, model_name: str = MODEL_NAME):
        print(f"正在加载 Embedding 模型：{model_name}")
        self.model = SentenceTransformer(model_name)

    def encode_documents(
        self,
        texts: list[str],
        batch_size: int = 32,
    ) -> np.ndarray:
        document_inputs = [f"passage: {text}" for text in texts]

        return self.model.encode(
            document_inputs,
            batch_size=batch_size,
            convert_to_numpy=True,
            normalize_embeddings=True,
            show_progress_bar=True,
        )

    def encode_query(self, query: str) -> np.ndarray:
        if not query.strip():
            raise ValueError("查询内容不能为空")

        return self.model.encode(
            f"query: {query}",
            convert_to_numpy=True,
            normalize_embeddings=True,
        )
