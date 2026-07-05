import json
from pathlib import Path


def save_chunks_to_json(chunks: list, output_path: Path):
    """
    将切块列表保存为JSON文件
    - 自动创建上级目录，避免目录不存在报错
    - 关闭ASCII转义，保证中文正常显示
    - 缩进格式化，方便人眼阅读
    """
    # 自动创建输出目录，已存在也不会报错
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as f:
        json.dump(chunks, f, ensure_ascii=False, indent=2)