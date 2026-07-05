from config import RAW_DATA_DIR, OUTPUT_JSON, CHUNK_SIZE, CHUNK_OVERLAP
from file_loader import load_raw_documents
from text_cleaner import clean_text
from chunker import create_chunks_for_document
from json_writer import save_chunks_to_json
from logger import get_logger

logger = get_logger()

if __name__ == "__main__":
    logger.info("项目启动：开始文档预处理流水线")
    
    # 1. 读取原始文档
    docs = load_raw_documents(RAW_DATA_DIR)
    logger.info(f"读取完成，共 {len(docs)} 个文档")
    
    all_chunks = []
    
    # 2. 逐篇清洗 + 切块
    for doc in docs:
        doc["text"] = clean_text(doc["text"])
        chunks = create_chunks_for_document(doc, CHUNK_SIZE, CHUNK_OVERLAP)
        all_chunks.extend(chunks)
        logger.info(f"处理完成：{doc['source_file']}，生成 {len(chunks)} 个切块")
    
    # 3. 保存结果到JSON文件
    save_chunks_to_json(all_chunks, OUTPUT_JSON)
    logger.info(f"全部处理完成，共 {len(all_chunks)} 个切块，已保存到 {OUTPUT_JSON}")