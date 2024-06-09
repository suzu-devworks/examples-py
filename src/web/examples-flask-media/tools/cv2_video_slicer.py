import cv2

FILE_PATH = "/workspaces/examples-py-web/temp/input.mp4"
VIDEO_SLICE_SECONDS = 10


def main() -> None:
    cap = cv2.VideoCapture(FILE_PATH)
    if cap.isOpened():
        print(f"Open! {FILE_PATH}")

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    frame_total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f"> org = {width}x{height}")
    print(f"> fps = {fps}")
    print(f"> frame_count = {frame_total}")

    w = 640
    h = int(height * (w / width))
    size = (w, h)
    print(f"> size = {w}x{h}")

    fourcc = cv2.VideoWriter.fourcc(*"vp90")

    split_count = 0
    success = True

    while cap.isOpened():
        frames = []
        frame_count = 0

        split_count += 1

        while cap.isOpened():
            success, frame = cap.read()
            if not success:
                break

            break_frame_count = fps * VIDEO_SLICE_SECONDS
            if break_frame_count < frame_count:
                break

            if size:
                frame = cv2.resize(frame, size, interpolation=cv2.INTER_LINEAR)

            frames.append(frame)
            frame_count += 1

        if len(frames) == 0:
            break

        print(f"read! {len(frames)}")

        new_filename = f"chunks_{split_count:04}.webm"
        chunks = cv2.VideoWriter(new_filename, fourcc, fps, size)

        for frame in frames:
            chunks.write(frame)

        chunks.release()

        print(f"write! {len(frames)} {new_filename}")
        pass

    cap.release()

    print("end!")
    return


if __name__ == "__main__":
    main()
