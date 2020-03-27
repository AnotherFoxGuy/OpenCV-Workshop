import cv2
import numpy as np


def test3a():
    img = cv2.imread("./tek1.png")
    # cv2.imshow('logo', img)

    # Convert BGR to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    # Threshold the HSV image to get only blue colors
    maskR = cv2.inRange(hsv, np.array([0, 50, 50]), np.array([40, 255, 255]))
    maskG = cv2.inRange(hsv, np.array([50, 50, 50]), np.array([70, 255, 255]))
    maskB = cv2.inRange(hsv, np.array([110, 50, 50]), np.array([130, 255, 255]))

    # Bitwise-AND mask and original image

    cv2.imshow('frame', img)
    cv2.imshow('hsv', hsv)
    cv2.imshow('resR', cv2.bitwise_and(img, img, mask=maskR))
    cv2.imshow('resG', cv2.bitwise_and(img, img, mask=maskG))
    cv2.imshow('resB', cv2.bitwise_and(img, img, mask=maskB))


test3a()

k = cv2.waitKey(0)
print(k)
cv2.destroyAllWindows()
