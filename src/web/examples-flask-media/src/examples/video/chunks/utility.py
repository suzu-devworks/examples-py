import re


def parse_range_header(range_header: str | None) -> tuple[int, int | None]:
    byte1, byte2 = 0, None
    if range_header:
        match = re.search(r"(\d+)-(\d*)", range_header)
        if match:
            groups = match.groups()

            if groups[0]:
                byte1 = int(groups[0])
            if groups[1]:
                byte2 = int(groups[1])

    return byte1, byte2


def format_range_header(start: int, length: int, file_size: int) -> str:
    return "bytes {0}-{1}/{2}".format(start, start + length - 1, file_size)
