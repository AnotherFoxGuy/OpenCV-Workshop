import cv2
import numpy as np


def test1():
    img = cv2.imread("./tek1.png")
    # cv2.imshow('logo', img)

    # Convert BGR to HSV
    # hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    # Threshold the HSV image to get only blue colors
    # maskR = cv2.inRange(hsv, np.array([0, 50, 50]), np.array([40, 255, 255]))

    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(imgray, 127, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cnt = contours[0]
    M = cv2.moments(cnt)

    hull = cv2.convexHull(cnt)

    cv2.imshow('frame', img)
    cv2.imshow('imgray', imgray)
    (x, y), radius = cv2.minEnclosingCircle(cnt)
    img = cv2.circle(img, (int(x), int(y)), 2, (0, 255, 0), 2)
    cv2.imshow('drawContours', cv2.drawContours(img, hull, -1, (50, 255, 255), 3))

    k = cv2.waitKey(0)
    print(k)
    cv2.destroyAllWindows()


test1()

# cap = cv2.VideoCapture(0)
#
# while (1):
#
#     # Take each frame
#     _, frame = cap.read()
#
#     # Convert BGR to HSV
#     hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#
#     # define range of blue color in HSV
#     lower_blue = np.array([110, 50, 50])
#     upper_blue = np.array([130, 255, 255])
#
#     # Threshold the HSV image to get only blue colors
#     mask = cv2.inRange(hsv, lower_blue, upper_blue)
#
#     # Bitwise-AND mask and original image
#     res = cv2.bitwise_and(frame, frame, mask=mask)
#
#     cv2.imshow('frame', frame)
#     cv2.imshow('mask', mask)
#     cv2.imshow('res', res)
#     k = cv2.waitKey(5) & 0xFF
#     if k == 27:
#         break
#
# cv2.destroyAllWindows()
