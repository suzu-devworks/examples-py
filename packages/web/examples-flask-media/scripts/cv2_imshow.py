import cv2

URL = "udp://127.0.0.1:5001?pkt_size=1316"


def main() -> None:
    video = cv2.VideoCapture(URL)

    while True:
        ret, frame = video.read()
        cv2.imshow("frame", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    video.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
