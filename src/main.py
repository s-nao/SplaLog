import cv2

# 動画を読込み
# カメラ等でストリーム再生の場合は引数に0等のデバイスIDを記述する
video = cv2.VideoCapture('../resource/video/test_data.mp4')

icon_width = 48
icon_height = 56

allies_positions = [
    {"x": 360, "y": 19},
    {"x": 415, "y": 19},
    {"x": 474, "y": 19},
    {"x": 531, "y": 19}
]

while video.isOpened():
    # フレームを読込み
    ret, frame = video.read()

    # フレームが読み込めなかった場合は終了（動画が終わると読み込めなくなる）
    if not ret:
        break

    # -----------------
    # 画像処理を記述する
    # -----------------
    deframe = []

    for position in allies_positions :
        deframe.append(frame[position["y"]:position["y"]+icon_height, position["x"]:position["x"]+icon_height])
        cv2.rectangle(frame, (position["x"], position["y"]),
                      (position["x"]+icon_width, position["y"]+icon_height), (0, 0, 255), 1)

    print(deframe)

    # フレームの描画
    cv2.imshow('frame', deframe[1])

    # qキーの押下で処理を中止
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

# メモリの解放
video.release()
cv2.destroyAllWindows()
