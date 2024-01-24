# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import cv2
import cv2.aruco as aruco
import numpy as np
import os

id_1 = np.zeros((3, 3))


def findarucomarkers(img, markerSize=6, totalMarkers=250, draw=True):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thresh1 = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY + cv2.THRESHOTSU)[1]
    key = getattr(aruco, f'DICT{markerSize}X{markerSize}_{totalMarkers}')
    arucoDict = aruco.Dictionary_get(key)
    arucoParam = aruco.DetectorParameterscreate()
    bboxs, ids, rejected = aruco.detectMarkers(gray, arucoDict, parameters=arucoParam)
    # print(ids)
    if draw:
        aruco.drawDetectedMarkers(img, bboxs)
    return [bboxs, ids]


def augmentAruco(bbox, id, img, imgAug, drawID=True):
    tl = bbox[0][0][0], bbox[0][0][1]
    tr = bbox[0][1][0], bbox[0][1][1]
    br = bbox[0][2][0], bbox[0][2][1]
    bl = bbox[0][3][0], bbox[0][3][1]
    h, w, c = imgAug.shape
    pts1 = np.array([tl, tr, br, bl])
    pts2 = np.float32([[0, 0], [w, 0], [w, h], [0, h]])
    matrix,  = cv2.findHomography(pts2, pts1)
    imgOut = cv2.warpPerspective(imgAug, matrix, (img.shape[1], img.shape[0]))
    return imgOut


def main():
    cap = cv2.VideoCapture(0)
    # imgAug = cv.imread("test2.jpeg")
    while True:
        success, img = cap.read()
        findarucomarkers(img)
        arucoFound = findarucomarkers(img)
        # if len(arucoFound[0]) != 0:
        #     for bbox, ids in zip(arucoFound[0], arucoFound[1]):
        #         img = augmentAruco(bbox, id, img, imgAug)

        cv2.imshow("Image", img)
        cv2.waitKey(0)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
