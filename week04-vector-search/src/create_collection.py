"""Create the Qdrant collection for document embeddings."""

from qdrant_service import QdrantService


def main() -> None:
    service = QdrantService()
    service.create_collection(reset=False)
    print("Qdrant Collection 初始化完成")


if __name__ == "__main__":
    main()
