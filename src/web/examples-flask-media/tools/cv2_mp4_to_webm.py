from pathlib import Path

import cv2

FILE_PATH = "/workspaces/examples-py/temp/input.mp4"


def main() -> None:
    cap = cv2.VideoCapture(FILE_PATH)

    fps = int(cap.get(cv2.CAP_PROP_FPS))
    print(f"> fps = {fps}")

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    size = (width, height)
    print(f"> size = {width}x{height}")

    new_filename = f"{Path(FILE_PATH).stem}.webm"
    writer = cv2.VideoWriter(new_filename, cv2.VideoWriter.fourcc(*"VP90"), fps, size)
    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break

        writer.write(frame)

    cap.release()


if __name__ == "__main__":
    main()
