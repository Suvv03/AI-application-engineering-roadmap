"""Qdrant collection management helpers."""

from qdrant_client import QdrantClient, models

from config import COLLECTION_NAME, EMBEDDING_DIM, QDRANT_URL


class QdrantService:
    """Manage the Qdrant collection used by the vector-search project."""

    def __init__(self) -> None:
        self.client = QdrantClient(url=QDRANT_URL)

    def create_collection(self, reset: bool = False) -> None:
        """Create the collection, optionally replacing an existing one."""
        exists = self.client.collection_exists(collection_name=COLLECTION_NAME)

        if exists and reset:
            self.client.delete_collection(collection_name=COLLECTION_NAME)
            exists = False

        if not exists:
            self.client.create_collection(
                collection_name=COLLECTION_NAME,
                vectors_config=models.VectorParams(
                    size=EMBEDDING_DIM,
                    distance=models.Distance.COSINE,
                ),
            )
            print(f"已创建 Collection：{COLLECTION_NAME}")
        else:
            print(f"Collection 已存在：{COLLECTION_NAME}")

    def count_points(self) -> int:
        """Return the exact number of points stored in the collection."""
        result = self.client.count(collection_name=COLLECTION_NAME, exact=True)
        return result.count
