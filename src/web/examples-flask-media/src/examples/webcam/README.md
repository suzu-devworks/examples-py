# Live streaming webcams

## Table of Contents <!-- omit in toc -->

- [Live streaming webcams](#live-streaming-webcams)
  - [Webcam streaming example for MJPEG](#webcam-streaming-example-for-mjpeg)
    - [Composition](#composition)
    - [MJPEG over HTTP](#mjpeg-over-http)
    - [マルチパート応答](#マルチパート応答)

## Webcam streaming example for MJPEG

- [source](./mjpeg/)

### Composition

```mermaid
flowchart LR
  subgraph Node1[tools/webcam1.sh]
    N1U1[📹 ffmpeg]
  end

  subgraph Node2[flask]
    N2U1(cv2.VideoCapture)
    N2U2[/🖼️ image/jpeg/]
    N2U1 --> N2U2
  end
  Node1 --"udp:5501"--> Node2

  subgraph Node3[browser]
    subgraph HTML
      IMG{{📹 img}}
    end
  end
  Node2 --"http:5500"--> Node3

classDef NodeStyle padding:1rem,fill:#ccc,color:#333,stroke:#fff
class Node1,Node2,Node3 NodeStyle

classDef HTMLeStyle padding:1rem,fill:#fff,color:#33e
class HTML,IMG HTMLeStyle

classDef ComponentStyle padding:1rem,fill:#666,color:#ccc
class N1U1,N2U1,N2U2 ComponentStyle

```

### MJPEG over HTTP

JPEG を `multipart/x-mixed-replace` により HTTP で返し、動画としてレンダリングさせるものを MJPEG over HTTP と呼ぶことがあります。単に MJPEG や Motion JPEG と呼ぶこともあるようです。

### マルチパート応答

`Content-Type: multipart/x-mixed-replace: boundary=frame`

multipart/x-mixed-replace は、 HTTP応答によりサーバーが任意のタイミングで複数の文書を返し、 紙芝居的にレンダリングを切り替えさせるMIMEタイプです。
boundary （区切り文字）は必須パラメータで、指定された文字列の前に `--` を付けてパートを区切ります。
