"""
cv2_video_mp4_to_webm.py

Usage:
    python ./scripts/cv2_video_mp4_to_webm.py /path/to/video.mp4
"""

import argparse
from pathlib import Path

import cv2


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Convert mp4 to webm")
    p.add_argument("input", type=Path, help="Path to input video file")
    return p.parse_args()


def main() -> None:
    args = parse_args()
    input_path: Path = args.input

    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    cap = cv2.VideoCapture(str(input_path))
    if not cap.isOpened():
        raise RuntimeError(f"Failed to open video: {input_path}")
    print(f"Open! {input_path}")

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) or 0
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) or 0
    size = (width, height)
    fps = cap.get(cv2.CAP_PROP_FPS) or 0.0
    print(f"> size = {width}x{height}")
    print(f"> fps = {fps}")

    if width == 0 or height == 0:
        raise RuntimeError("Could not read video dimensions from input file")

    if fps == 0.0:
        fps = 30.0
        print("> fps unknown, falling back to 30.0")

    new_filename = f"{Path(input_path).stem}.webm"
    writer = cv2.VideoWriter(new_filename, cv2.VideoWriter.fourcc(*"vp90"), fps, size)
    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break

        writer.write(frame)

    cap.release()


if __name__ == "__main__":
    main()
