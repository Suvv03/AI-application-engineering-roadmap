import re


def remove_extra_spaces(text: str) -> str:
    """压缩连续的多个空格，保留单个空格"""
    # 把连续出现的多个空格，替换成单个空格
    text = re.sub(r"[ ]+", " ", text)
    return text


def remove_extra_blank_lines(text: str) -> str:
    """压缩连续的多个空行，最多保留1个空行间隔"""
    # 把连续3个及以上的换行，替换成2个换行
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text


def clean_text(text: str) -> str:
    """文本清洗统一入口：依次执行所有清洗规则"""
    text = remove_extra_spaces(text)
    text = remove_extra_blank_lines(text)
    # 去掉文本首尾的空白字符（空格、换行、制表符）
    return text.strip()