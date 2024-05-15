from datetime import datetime
from logging import getLogger

import cv2

logger = getLogger(__name__)


class VideoCamera:
    url: str
    video: cv2.VideoCapture

    def __init__(self, url: str):
        self.url = url
        self.video = cv2.VideoCapture(self.url)
        if self.video.isOpened():
            logger.info(f"Open! {self.url}")

    def __del__(self) -> None:
        self.video.release()

    def set_datetime(self, image: cv2.typing.MatLike, text: str) -> None:
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

    def get_frame(self) -> bytes | None:
        success, image = self.video.read()
        if not success:
            logger.info(f"End! {self.url}")
            return None

        self.set_datetime(image, f"{(datetime.now().strftime("%H:%M:%S"))}")

        # spell-checker:words imencode
        # spell-checker:words tobytes
        _, jpeg = cv2.imencode(".jpg", image)
        return jpeg.tobytes()
