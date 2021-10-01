## 構築時エラー


### opencvをpipenvでインストール後のエラー

**エラー内容**
``` $shell
Traceback (most recent call last):
  File "/Users/****/repositories/SplaLog/src/main.py", line 1, in <module>
    import cv2
  File "/Users/****/.local/share/virtualenvs/SplaLog-LfVzFE6D/lib/python3.9/site-packages/cv2/__init__.py", line 5, in <module>
    from .cv2 import *
ImportError: dlopen(/Users/****/.local/share/virtualenvs/SplaLog-LfVzFE6D/lib/python3.9/site-packages/cv2/cv2.cpython-39-darwin.so, 2): Library not loaded: /opt/homebrew/opt/ffmpeg/lib/libavcodec.58.dylib
  Referenced from: /Users/****/.local/share/virtualenvs/SplaLog-LfVzFE6D/lib/python3.9/site-packages/cv2/cv2.cpython-39-darwin.so
  Reason: image not found

```

**解決**

ソースコードからインストールもあったが、エラー内容を見る限り、

```
brew intall ffmpeg
```

### obsで取得したキャプチャーを入力値にしたい

1. obs-virtualcamをインストールする
```
brew install obs-virtualcam
```

2. コードないのvideo captureの項目を修正
```
例) 
修正前：video = cv2.VideoCapture("ファイル名")
修正後：video = cv2.VideoCapture(1) # 自分のPCはインカメがあるから1を指定する
```