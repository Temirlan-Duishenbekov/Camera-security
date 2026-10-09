from turtle import width

import torch
import matplotlib.pyplot as plt
import numpy as np
import cv2


array = np.array([
            [
                [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
                [[19, 20, 21], [22, 23, 24], [25, 26, 27]],
                [[28, 29, 30], [31, 32, 33], [34, 35, 36]],
                [[37, 38, 39], [40, 41, 42], [43, 44, 45]]
            ],
    
            [
                [["1", "ggg", "hhh"], ["4", "iii", "jjj"], ["5", "kkk", "lll"]],
                [["6", "mmm", "nnn"], ["7", "ooo", "ppp"], ["8", "qqq", "rrr"]],
                [["9", "sss", "ttt"], ["10", "uuu", "vvv"], ["11", "www", "xxx"]],
                [["12", "yyy", "zzz"], ["13", "AAA", "BBB"], ["14", "CCC", "DDD"]],
                [["15", "EEE", "FFF"], ["16", "GGG", "HHH"], ["17", "III", "JJJ"]]
            ]
]) 

print(array.shape)

print(array[1, 1, 1, 1])



















cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        break
    hight = cap.get(int(4))
    width = cap.get(int(3))
    img = np.zeros(frame.shape, dtype=np.uint8)

    cv2.imshow("Frame", img.shape)
    if cv2.waitKey(1) == ord('q') or cv2.waitKey(1) == ord('Q'):
        break
cap.release()
cv2.destroyAllWindows()