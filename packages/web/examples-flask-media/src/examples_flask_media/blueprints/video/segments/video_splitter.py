import os


def get_chunk(
    file_path: str, byte1: int, byte2: int | None = None, chunk_size: int = 131072
) -> tuple[bytes, int, int, int]:
    file_size = os.stat(file_path).st_size
    start = 0

    if byte1 < file_size:
        start = byte1

    if byte2:
        length = byte2 + 1 - byte1
    elif start + chunk_size < file_size:
        length = chunk_size
    else:
        length = file_size - start

    with open(file_path, "rb") as f:
        f.seek(start)
        chunk = f.read(length)

    return chunk, start, length, file_size
