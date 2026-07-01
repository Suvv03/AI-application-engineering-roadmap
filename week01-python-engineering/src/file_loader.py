from pathlib import Path


def load_txt_file(file_path: Path) -> str:
    """读取单个txt文件，自动兼容utf-8和gbk编码，避免中文乱码"""
    try:
        # 优先用通用的utf-8编码读取
        return file_path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        # 读取失败则用gbk编码，并忽略无法识别的字符
        return file_path.read_text(encoding="gbk", errors="ignore")


def load_raw_documents(raw_dir: Path):
    """批量读取指定目录下所有txt文件，返回结构化的文档列表"""
    documents = []
    # 遍历目录里所有后缀为 .txt 的文件
    for file_path in raw_dir.glob("*.txt"):
        text = load_txt_file(file_path)
        # 每条记录保存「文件名 + 文件内容」，方便后续追溯来源
        documents.append({
            "source_file": file_path.name,
            "text": text
        })
    return documents