from config import RAW_DATA_DIR
from file_loader import load_raw_documents
from text_cleaner import clean_text
from logger import get_logger

logger = get_logger()

if __name__ == "__main__":
    logger.info("Project started")
    
    # 1. 批量读取原始文档
    docs = load_raw_documents(RAW_DATA_DIR)
    logger.info(f"Loaded {len(docs)} documents")
    
    # 2. 逐篇清洗文本，并打印清洗前后长度
    for doc in docs:
        before_len = len(doc["text"])
        doc["text"] = clean_text(doc["text"])
        after_len = len(doc["text"])
        logger.info(f"清洗完成：{doc['source_file']} | 字符数 {before_len} → {after_len}")