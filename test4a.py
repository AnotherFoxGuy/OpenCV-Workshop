import cv2
import numpy as np


def test4a():
    img = cv2.imread("./bouten_moeren.jpg")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    grayBlur = cv2.GaussianBlur(gray, (25, 25), 0)
    ret, th = cv2.threshold(grayBlur, 180, 255, cv2.THRESH_BINARY_INV)
    contours, hierarchy = cv2.findContours(th, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 100:
            cv2.drawContours(img, [cnt], -1, (0, 255, 255), 3)
    cv2.imshow('frame', img)


test4a()

k = cv2.waitKey(0)
print(k)
cv2.destroyAllWindows()
