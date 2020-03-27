import cv2
import numpy as np


def getEyes(num, img):
    ret, th = cv2.threshold(img, 230, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(th, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    count = 0
    for cnr in range(len(contours)):
        cnt = contours[cnr]
        perimeter = cv2.arcLength(cnt, True)
        area = cv2.contourArea(cnt)
        if perimeter == 0 or area == 0:
            continue
        factor = 4 * np.pi * area / perimeter ** 2
        if factor > 0.5 and area > 10:
            #cv2.drawContours(img, [cnt], -1, (0, 0, 255), 3)
            count += 1
    cv2.imshow('die %s' % num, img)
    print('Found %s eyes on die %s' % (count, num))


def test5():
    img = cv2.imread("./dobbelstenen.png")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    grayBlur = cv2.GaussianBlur(gray, (3, 3), 0)
    ret, th = cv2.threshold(grayBlur, 5, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(th, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    num = 0
    for cnr in range(len(contours)):
        cnt = contours[cnr]

        num += 1
        x, y, w, h = cv2.boundingRect(cnt)
        die = grayBlur[y:y + h, x:x + w]
        getEyes(num, die)


test5()

k = cv2.waitKey(0)
print(k)
cv2.destroyAllWindows()
