from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

CHUNKS_PATH = DATA_DIR / "chunks.json"
EMBEDDINGS_PATH = DATA_DIR / "embeddings.npy"
EMBEDDING_META_PATH = DATA_DIR / "embedding_meta.json"

MODEL_NAME = "intfloat/multilingual-e5-small"
EMBEDDING_DIM = 384

QDRANT_URL = "http://localhost:6333"
COLLECTION_NAME = "research_chunks"
