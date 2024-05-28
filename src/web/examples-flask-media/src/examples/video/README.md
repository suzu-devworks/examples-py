# Video streaming

## Table of Contents <!-- omit in toc -->

- [Video streaming](#video-streaming)
  - [Video chunk streaming example](#video-chunk-streaming-example)
    - [Composition](#composition)
    - [206 Partial Content](#206-partial-content)

## Video chunk streaming example

- [source](./chunks/)


### Composition

```mermaid
flowchart LR
  subgraph Node1[Server]
    direction TB
    subgraph Node2[flask]
      N2U1(BufferedReader)
    end
    N1U1[(🖼️ input.mp4)]
    N2U1 --> N1U1
  end

  subgraph Node3[browser]
    subgraph HTML
      IMG{{📹 video}}
    end
  end
  Node1 --"http:5500"--> Node3

classDef NodeStyle padding:1rem,fill:#ccc,color:#333,stroke:#fff
class Node2,Node3 NodeStyle

classDef HTMLeStyle padding:1rem,fill:#fff,color:#33e
class HTML,IMG HTMLeStyle

classDef ComponentStyle padding:1rem,fill:#666,color:#ccc
class N1U1,N2U1 ComponentStyle

```

### 206 Partial Content

video タグで動画をホストする場合、レスポンスコード 200 では早送りなどの操作ができない場合があり、206 を強要する場合があるようです。

- [&lt;video&gt; - mdn](https://developer.mozilla.org/ja/docs/Web/HTML/Element/video)
- [206 Partial Content - mdn](https://developer.mozilla.org/ja/docs/Web/HTTP/Status/206)
