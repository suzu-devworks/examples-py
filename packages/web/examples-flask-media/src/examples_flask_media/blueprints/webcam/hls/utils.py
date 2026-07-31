def get_video_mimetype(suffix: str) -> str:
    values = {
        ".m3u8": "application/vnd.apple.mpegurl",
        ".ts": "video/MP2T",
        ".m4s": "video/iso.segment",
    }
    return values[suffix]
