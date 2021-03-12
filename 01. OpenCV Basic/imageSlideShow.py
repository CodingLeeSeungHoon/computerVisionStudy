import cv2
import sys
import glob

"""
. >> 현재 폴더
\\ >> 하위   
.\\images\\*.jpg >> 현재 폴더 아래의 images 폴더에서 jpg 확장자로 끝나는 모든 것을 의미
"""
ESC = 27
img_files = glob.glob('.\\images\\*.jpg')

for f in img_files:
    print(f)

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.setWindowProperty('image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

cnt = len(img_files)
idx = 0

while True:
    img = cv2.imread(img_files[idx])
    cv2.imshow('image', img)

    if cv2.waitKey(10000) == ESC:
        break

    idx += 1
    if idx >= cnt:
        idx = 0

cv2.destroyAllWindows()