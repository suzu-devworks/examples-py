#/usr/bin/sh

# ffmpeg -hide_banner -f avfoundation -pix_fmt:v yuyv422 -r 30 -s:v 1280x720 -i "0" \
#     -c:v hevc_videotoolbox -tag:v hvc1 -q:v 60 -an \
#     -flags +cgop -g 30 -filter:v yadif \
#     -threads 1 \
#     -f hls \
#     -hls_time 5 \
#     -hls_list_size 10 \
#     -hls_allow_cache 0 \
#     -hls_flags delete_segments \
#     -hls_segment_type mpegts \
#     -hls_segment_filename 'webcam-%3d.ts' \
#     playlist.m3u8

# spell-checker: words avfoundation mpegts videotoolbox yuyv cgop yadif

ffmpeg -hide_banner -f avfoundation -pix_fmt:v yuyv422 -r 30 -s:v 640x480 -i "0" \
    -c:v h264_videotoolbox -tag:v avc1 -q:v 60 -an \
    -flags +cgop -g 30 -filter:v yadif \
    -threads 1 \
    -f hls \
    -hls_time 5 \
    -hls_list_size 10 \
    -hls_allow_cache 0 \
    -hls_flags delete_segments \
    -hls_segment_type mpegts \
    -hls_segment_filename 'webcam-%3d.ts' \
    playlist.m3u8
