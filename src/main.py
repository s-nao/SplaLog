import cv2
import numpy as np

import logging

# 動画を読込み
# カメラ等でストリーム再生の場合は引数に0等のデバイスIDを記述する
video = cv2.VideoCapture('../resource/video/test_data2.mp4')

icon_width = 48
icon_height = 56

allies_positions = [
    {"x": 360, "y": 19},
    {"x": 415, "y": 19},
    {"x": 474, "y": 19},
    {"x": 531, "y": 19}
]

enemy_positions = [
    {"x": 700, "y": 19},
    {"x": 755, "y": 19},
    {"x": 814, "y": 19},
    {"x": 871, "y": 19}
]


def is_death(img_th):
    if (cv2.countNonZero(img_th)/ img_th.size  * 100) <= 30:
        return "death"
    else:
        return "alive"

def main():
    while video.isOpened():
        # フレームを読込み
        ret, frame = video.read()

        # フレームが読み込めなかった場合は終了（動画が終わると読み込めなくなる）
        if not ret:
            break

        # -----------------
        # 画像処理を記述する
        # -----------------
        allies_frames = []

        enemy_frames = []
        enemy_frames_hsv = []

        # 味方のフレーム取得
        allies_frames = logging.detect_frame(frame, allies_positions, True)
        enemy_frames = logging.detect_frame(frame, enemy_positions, True)

        # フレームの描画
        # count = 0
        # for (frame,frame_hsv) in zip(enemy_frames,enemy_frames_hsv):
        #     cv2.imshow('frame:{%d}' % count, frame)
        #     cv2.imshow('frame_hsv:{%d}' % count, frame_hsv)
        #     count+=1
        #
        #     ret1,img_th=cv2.threshold(frame_hsv,0,255,cv2.THRESH_OTSU)
        #     print((cv2.countNonZero(img_th)/ img_th.size  * 100))
        #
        #     break

        # cv2.imshow('frame', enemy_frames[1])
        # cv2.imshow('frame_hsv', enemy_frames_hsv[1])
        #
        #
        # ret1,img_th=cv2.threshold(enemy_frames_hsv[1],0,255,cv2.THRESH_OTSU)
        # print((cv2.countNonZero(img_th)/ img_th.size  * 100) )
        # print(is_death(img_th))
        #

        cv2.imshow("frame", frame)

        # qキーの押下で処理を中止
        key = cv2.waitKey(1)
        if key == ord('q'):
            break


if __name__ == "__main__":
    main()

    # メモリの解放
    video.release()
    cv2.destroyAllWindows()
