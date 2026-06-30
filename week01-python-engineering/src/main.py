from config import BASE_DIR
from logger import get_logger

# 初始化日志工具
logger = get_logger()

if __name__ == "__main__":
    # 打印启动日志
    logger.info("Project started")
    # 打印项目路径，确认配置没有问题
    logger.info(f"Project base directory: {BASE_DIR}")