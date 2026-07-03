def chunk_text(text: str, chunk_size: int, overlap: int):
    """
    按固定长度切分文本，保留重叠上下文
    参数：
        text: 待切分的文本内容
        chunk_size: 每个切块的最大字符数
        overlap: 相邻切块的重叠字符数
    返回：包含text、char_start、char_end的切块列表
    """
    # 重叠不能大于等于切块大小，否则会进入死循环
    if overlap >= chunk_size:
        raise ValueError("overlap must be smaller than chunk_size")

    chunks = []
    start = 0
    text_length = len(text)

    # 循环切分，直到覆盖全文
    while start < text_length:
        # 计算当前切块的结束位置，末尾不超出文本总长度
        end = min(start + chunk_size, text_length)
        # 去除切块首尾空白，避免空切块
        chunk = text[start:end].strip()
        if chunk:
            chunks.append({
                "text": chunk,
                "char_start": start,
                "char_end": end
            })
        # 滑动窗口：每次前进 chunk_size - overlap 的距离
        start += chunk_size - overlap

    return chunks


def create_chunks_for_document(document: dict, chunk_size: int, overlap: int):
    """
    为单篇文档生成带元数据的完整切块列表
    给每个切块加上唯一ID、来源文件名，方便后续溯源
    """
    raw_chunks = chunk_text(document["text"], chunk_size, overlap)
    results = []
    # 给每个切块编号，生成格式为 文件名_0001 的唯一ID
    for idx, chunk in enumerate(raw_chunks, start=1):
        results.append({
            "chunk_id": f"{document['source_file']}_{idx:04d}",
            "source_file": document["source_file"],
            **chunk
        })
    return results