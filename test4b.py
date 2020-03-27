import cv2
import numpy as np


def test4():
    img = cv2.imread("./bouten_moeren.jpg")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    grayBlur = cv2.GaussianBlur(gray, (25, 25), 0)
    ret, th = cv2.threshold(grayBlur, 180, 255, cv2.THRESH_BINARY_INV)
    contours, hierarchy = cv2.findContours(th, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    hierarchy = hierarchy[0]
    for cnr in range(len(contours)):
        cnt = contours[cnr]
        area = cv2.contourArea(cnt)
        if area < 500:
            continue
        perimeter = cv2.arcLength(cnt, True)
        factor = 4 * np.pi * area / perimeter ** 2
        holes = 0
        child = hierarchy[cnr][2]
        while child >= 0:
            holes += cv2.contourArea(contours[child])
            child = hierarchy[child][0]

        if holes > 0:
            cv2.drawContours(img, [cnt], -1, (255, 0, 0), 3)
            print("Nut", factor, holes, )
        elif factor > 0.8:
            cv2.drawContours(img, [cnt], -1, (0, 255, 255), 3)
            print("Standing Bold", factor, holes)
        elif factor < 0.5:
            cv2.drawContours(img, [cnt], -1, (0, 255, 0), 3)
            print("Standing Nut", factor, holes)
        else:
            cv2.drawContours(img, [cnt], -1, (0, 0, 255), 3)
            print("Bold", factor, holes)

    cv2.imshow('frame', img)


test4()

k = cv2.waitKey(0)
print(k)
cv2.destroyAllWindows()
