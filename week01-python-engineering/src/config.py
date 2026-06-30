from pathlib import Path

# 自动获取项目根目录，不用手动写死路径
BASE_DIR = Path(__file__).resolve().parent.parent

# 原始文档存放文件夹
RAW_DATA_DIR = BASE_DIR / "data" / "raw"
# 处理结果存放文件夹
PROCESSED_DATA_DIR = BASE_DIR / "data" / "processed"
# 最终输出的切块结果文件
OUTPUT_JSON = PROCESSED_DATA_DIR / "chunks.json"

# 文本切块参数
CHUNK_SIZE = 500    # 每个文本块的字符数
CHUNK_OVERLAP = 50  # 相邻块的重叠字符数