#/usr/bin/sh

ffmpeg -hide_banner -re -f avfoundation -pix_fmt yuyv422 -r 30 -s 640x480 -i "0" \
    -c:v hevc_videotoolbox -tag:v hvc1 -q:v 60 -an \
    -f mpegts "udp://127.0.0.1:5501?pkt_size=1316"
