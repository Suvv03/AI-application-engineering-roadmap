from config import RAW_DATA_DIR
from file_loader import load_raw_documents
from logger import get_logger

# 初始化日志工具
logger = get_logger()

if __name__ == "__main__":
    logger.info("Project started")
    
    # 批量读取 raw 目录下的所有文档
    docs = load_raw_documents(RAW_DATA_DIR)
    # 打印读取到的文件总数
    logger.info(f"Loaded {len(docs)} documents")
    
    # 逐个打印文件名和字数，确认读取正常
    for doc in docs:
        logger.info(f"读取文件：{doc['source_file']}，字数：{len(doc['text'])}")