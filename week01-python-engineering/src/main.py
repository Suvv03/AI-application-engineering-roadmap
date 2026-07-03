from config import RAW_DATA_DIR, CHUNK_SIZE, CHUNK_OVERLAP
from file_loader import load_raw_documents
from text_cleaner import clean_text
from chunker import create_chunks_for_document
from logger import get_logger

logger = get_logger()

if __name__ == "__main__":
    logger.info("Project started")
    
    # 1. 批量读取原始文档
    docs = load_raw_documents(RAW_DATA_DIR)
    logger.info(f"Loaded {len(docs)} documents")
    
    all_chunks = []
    # 2. 逐篇清洗 + 切块
    for doc in docs:
        before_len = len(doc["text"])
        doc["text"] = clean_text(doc["text"])
        after_len = len(doc["text"])
        logger.info(f"清洗完成：{doc['source_file']} | 字符数 {before_len} → {after_len}")
        
        # 生成切块
        chunks = create_chunks_for_document(doc, CHUNK_SIZE, CHUNK_OVERLAP)
        all_chunks.extend(chunks)
        logger.info(f"生成切块：{doc['source_file']} | 共 {len(chunks)} 个chunk")
    
    # 3. 输出总切块数
    logger.info(f"全部文档处理完成，总切块数：{len(all_chunks)}")