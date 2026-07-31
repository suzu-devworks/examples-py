import threading
import time
from datetime import datetime
from logging import getLogger

import cv2

logger = getLogger(__name__)


class VideoCamera:
    url: str
    video: cv2.VideoCapture
    framerate: int
    running: bool = False
    thread: threading.Thread | None = None
    image: cv2.typing.MatLike | None = None
    timestamp: datetime | None = None

    def __init__(self, url: str) -> None:
        self.url = url
        self.video = cv2.VideoCapture()

    def __del__(self) -> None:
        self.stop()

        if self.thread is not None:
            self.thread.join()
            self.thread = None

        if self.video is not None:
            self.video.release()

    def start(self, framerate: int = 30) -> None:
        if self.running:
            logger.warn(f"already running: {self.url}")
            return

        self.framerate = framerate

        self.video.open(self.url)
        if not self.video.isOpened():
            logger.warn(f"not opened: {self.url}")
            return

        logger.info(f"open: {self.url}")

        self.running = True
        self.thread = threading.Thread(target=self._read_frame)
        self.thread.start()

    def stop(self) -> None:
        self.running = False
        logger.debug(f"stop request: {self.url}")

    def _read_frame(self) -> None:
        logger.debug("read start")
        while self.running:
            success, image = self.video.read()
            if not success:
                logger.warn(f"read failed: {self.url}")
                self.stop()
                break

            self.timestamp = datetime.now()
            self.image = image if success else None
            # time.sleep(.1)  # 0.1s to use less CPU
            time.sleep(1 / self.framerate)

        logger.debug("read end")

    def get_frame(self) -> bytes | None:
        if (not self.running) or (self.image is None):
            return None

        image = self.image.copy()

        if self.timestamp is not None:
            self._set_datetime(image, f"{(self.timestamp.strftime('%H:%M:%S'))}")

        _, jpeg = cv2.imencode(".jpg", image)
        return jpeg.tobytes()

    def get_gray_frame(self) -> bytes | None:
        if (not self.running) or (self.image is None):
            self.stop()
            return None

        image = self.image
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        if self.timestamp is not None:
            self._set_datetime(gray, f"{(self.timestamp.strftime('%H:%M:%S'))}")

        _, jpeg = cv2.imencode(".jpg", gray)
        return jpeg.tobytes()

    def _set_datetime(self, image: cv2.typing.MatLike, text: str) -> None:
        cv2.putText(
            image,
            text,
            org=(10, 40),
            fontFace=cv2.FONT_HERSHEY_SIMPLEX,
            fontScale=1.0,
            color=(255, 255, 255),
            thickness=2,
            lineType=cv2.LINE_4,
        )
