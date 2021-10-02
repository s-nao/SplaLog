import cv2


def is_death(img_th):
    if (cv2.countNonZero(img_th)/ img_th.size  * 100) <= 30:
        return "death"
    else:
        return "alive"
