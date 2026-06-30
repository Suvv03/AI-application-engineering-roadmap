import logging

def get_logger(name: str = "week01"):
    # 设置日志格式：时间 | 级别 | 信息内容
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s"
    )
    return logging.getLogger(name)