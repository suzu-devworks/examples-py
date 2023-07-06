import asyncio
from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import Any

import cv2

# *** asyncio will be slower　***

FILE_PATH = "/workspaces/examples-py-web/temp/input.mp4"
VIDEO_SLICE_SECONDS = 10


reading: bool = False
framerate: int = 10


async def read_frames(queue: asyncio.Queue[Any]) -> None:
    global reading
    global framerate

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

    framerate = fps

    reading = True
    read_count = 0
    split_count = 0

    while reading:
        if not cap.isOpened():
            break

        success, frame = cap.read()
        if not success:
            break

        read_count += 1

        if size:
            frame = cv2.resize(frame, size, interpolation=cv2.INTER_LINEAR)

        queue.put_nowait(frame)

        break_frame_count = framerate * VIDEO_SLICE_SECONDS
        if read_count % break_frame_count == 0:
            split_count += 1
            print(f"put! {read_count} -> {split_count} qsize={queue.qsize()}")
            await asyncio.sleep(0)
            pass

    cap.release()

    split_count += 1
    print(f"put! {read_count} -> {split_count} qsize={queue.qsize()}")

    reading = False
    print(f"end read! {FILE_PATH}")
    return


async def record_frames(queue: asyncio.Queue[Any]) -> None:
    fourcc = cv2.VideoWriter.fourcc(*"vp90")
    split_count = 0

    while True:
        if queue.empty() and (not reading):
            break

        if queue.empty():
            await asyncio.sleep(0)
            continue

        split_count += 1

        frames = []
        break_frame_count = framerate * VIDEO_SLICE_SECONDS
        for _ in range(break_frame_count):
            if queue.empty():
                break
            frame = queue.get_nowait()
            frames.append(frame)

        print(f"get! {len(frames)} -> {split_count} qsize={queue.qsize()}")
        await asyncio.sleep(0)

        if len(frames) == 0:
            continue

        h, w, _ = frames[0].shape
        size = (w, h)
        print(f"> size = {size}")

        with NamedTemporaryFile(suffix=".webm", dir="./", delete=False) as fp:
            filename = fp.name
            chunks = cv2.VideoWriter(filename, fourcc, framerate, size)

            for frame in frames:
                chunks.write(frame)

            chunks.release()

            new_filename = f"chunk_{split_count:04}.webm"
            Path(new_filename).unlink(missing_ok=True)
            Path(filename).rename(new_filename)
            print(f"write! {len(frames)} {new_filename}")
            pass

    queue.task_done()
    print("end write!")
    return


async def main() -> None:
    global reading
    frames: asyncio.Queue[Any] = asyncio.Queue()

    try:
        async with asyncio.TaskGroup() as tasks:
            tasks.create_task(read_frames(frames))
            tasks.create_task(record_frames(frames))

    except* Exception as e:
        for _e in e.exceptions:
            print(_e)


if __name__ == "__main__":
    asyncio.run(main())
