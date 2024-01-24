import threading
import time
import cv2
import cv2.aruco as aruco
import numpy as np
from pygame import mixer
import imutils
import random


mixer.init()


check = False


class ntm():
    def __init__(self, img):
        threading.Thread.__init__(self)
        print("huehue")
        self.find_aruco = threading.Thread(target=find_aruco, args=(img))
        self.find_aruco.daemon = True

    def run(self, img, img1):
        print("????????")
        find_aruco(self, img)
        find_aruco(self, img1)


id = []

dict = {0: '1_part.mp3', 1: '2_part.mp3', 2: '3_part.mp3', 3: '4_part.mp3', 4: '1.mp3', 5: '2.mp3', 6: '3.mp3', 7: '4.mp3'}


# def find_aruco(img, markersize=6, totalmarkers=250, draw=True):
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     # gray2 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
#     thresh1 = cv2.threshold(gray, 175, 255, cv2.THRESH_OTSU)[1]
#     #     thresh2 = cv2.threshold(gray2, 100, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
#     #     imgray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     key = getattr(aruco, f'DICT_{markersize}X{markersize}_{totalmarkers}')
#     arucodict = aruco.Dictionary_get(key)
#     arucoparam = aruco.DetectorParameters_create()
#     # bboxs, ids, rejected = aruco.detectMarkers(thresh1, arucodict, parameters=arucoparam)
#     bboxs, ids, rejected = aruco.detectMarkers(thresh1, arucodict, parameters=arucoparam)
#     #     bboxs1, ids1, rejected1 = aruco.detectMarkers(thresh2, arucodict, parameters=arucoparam)
#     # chnone(ids, ids1)
#     id = np.unique(ids)
#     # + np.unique(ids1)
#     print(id)
#     func(id, check)
#     # id.append(ids)
#     if draw:
#         aruco.drawDetectedMarkers(thresh1, bboxs)
#     # print("huehue")
#     cv2.imshow("threaded image", thresh1)


def find_aruco(img, img1, markersize=6, totalmarkers=250, draw=True):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    thresh1 = cv2.threshold(gray, 175, 255, cv2.THRESH_OTSU)[1]
    thresh2 = cv2.threshold(gray2, 175, 255, cv2.THRESH_OTSU)[1]
    #     imgray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    key = getattr(aruco, f'DICT_{markersize}X{markersize}_{totalmarkers}')
    arucodict = aruco.Dictionary_get(key)
    arucoparam = aruco.DetectorParameters_create()
    # bboxs, ids, rejected = aruco.detectMarkers(thresh1, arucodict, parameters=arucoparam)
    bboxs, ids, rejected = aruco.detectMarkers(thresh1, arucodict, parameters=arucoparam)
    bboxs1, ids1, rejected1 = aruco.detectMarkers(thresh2, arucodict, parameters=arucoparam)
    # chnone(ids, ids1)
    ids = [10] if ids is None else ids
    ids1 = [10] if ids1 is None else ids1
    id_0 = ids + ids1
    id = np.unique(id_0)
    # + np.unique(ids1)
    print(id)
    func(id, check)
    # id.append(ids)
    if draw:
        aruco.drawDetectedMarkers(thresh1, bboxs)
        aruco.drawDetectedMarkers(thresh2, bboxs1)
    # print("huehue")
    cv2.imshow("threaded image", thresh1)
    cv2.imshow("threaded image 2", thresh2)


count = 0


def one():
    mixer.music.play()


def check_all(id):
    a = id.size
    if a == 4:
        return True


def counter():
    global count
    count += 12.5
    print(count)



# def chnone(id):
#     id1 = np.arange(0, 8)
#     id = id1
#     np.random.shuffle(id1)
#     i = random.randint(0, 7)
#     k = random.randint(0, 7)
#     if id1[k] not in id and i != k:
#         mixer.music.load(dict[i])
#         mixer.music.play()
#     time.sleep(2)


def chnone(ids):
        # mixer.music.load('1.wav')
        id1 = np.arange(0, 8)
        id = id1
        if id[0] != [0] or id1[0] != [0]:
            mixer.music.play()
            counter()
            time.sleep(10)
            b = False
            mixer.music.load('2_part.mp3')
            return
        elif id[1] != [1] or id1[1] != [1]:
            one()
            counter()
            b = False
            mixer.music.load('3_part.mp3')
            return
        elif id[2] != [2] or id1[2] != [2]:
            one()
            counter()
            b = False
            mixer.music.load('4_part.mp3')
            return
        elif id[3] != [3] or id1[3] != [3]:
            one()
            counter()
            b = False
            # mixer.music.load('music/5_part.mp3')
            return
        elif id[4] != [4] or id1[4] != [4]:
            one()
            counter()
            b = False
            mixer.music.load('music/6_part.mp3')
            return
        elif id[5] != [5] or id1[5] != [5]:
            one()
            time.sleep(10)
            counter()
            b = False
            mixer.music.load('music/7_part.mp3')
            return
        elif id[6] != [6] or id1[6] != [6]:
            one()
            time.sleep(10)
            counter()
            b = False
            mixer.music.load('music/8_part.mp3')
            return
        elif id[7] != [7] or id1[7] != [7]:
            one()
            time.sleep(10)
            counter()
            b = False
            return


def func(id, check):
    if id.size == 0:
        print("No Markers Detected")
    if id.size != 8:
        print("True")
        check = True
        chnone(id)
    # if check:
    #
    #     print("Running")
    # else:
    #     print(" ??? ")
    return check


def main():
    cap = cv2.VideoCapture(0)
    cap1 = cv2.VideoCapture(0)
    while True:
        success, img = cap.read()
        success1, img1 = cap1.read()
        find_aruco(img, img1)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()
