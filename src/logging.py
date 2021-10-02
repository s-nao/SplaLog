import cv2
import numpy as np

from enumrators.battle_status import BattleStatus

icon_width = 48
icon_height = 56


def detect_frame(frame, positions, is_rendering=False):
    cut = lambda position: frame[position["y"]:position["y"] + icon_height,position["x"]:position["x"] + icon_height]

    if is_rendering:
        for position in positions:
            cv2.rectangle(frame,
                          (position["x"], position["y"]),
                          (position["x"]+icon_width, position["y"]+icon_height), (0, 0, 255), 1)

    return [cut(position) for position in positions]


def battle_status():
    """ function: battle_status
    戦況を返却する関数

    ALLIES_TURN
    ENEMY_TURN
    NONE

    :return:
    """
    pass

def is_pinch():
    pass


def which_pinch_team():
    pass


