import numpy as np
import cv2

src = cv2.imread('images/airplane.bmp', cv2.IMREAD_COLOR)
mask = cv2.imread('images/mask_plane.bmp', cv2.IMREAD_GRAYSCALE)
dst = cv2.imread('images/field.bmp', cv2.IMREAD_COLOR)

# src와 dst는 type이 같아야 함. src == dst == cv2.IMREAD_COLOR
# mask는 무조건 cv2.IMREAD_GRAYSCALE

cv2.copyTo(src, mask, dst)
# dst[mask > 0] = src[mask > 0] // 위의 코드와 같은 기능


cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.imshow('mask', mask)

cv2.waitKey()
cv2.destroyAllWindows()


# alpha channel 있는 값은 cv2.IMREAD_UNCHANGED로 불러온다. 4채널
src2 = cv2.imread('images/opencv-logo-white.png', cv2.IMREAD_UNCHANGED)
mask2 = src2[:, :, -1]  # alpha channel values
src2 = src2[:, :, 0:3]  # except alpha channel values, RGB

h, w = src2.shape[:2]
crop = dst[0:h, 0:w]

cv2.copyTo(src2, mask2, crop)

cv2.imshow('src2', src2)
cv2.imshow('mask2', mask2)
cv2.imshow('dst', dst)
cv2.imshow('crop', crop)

cv2.waitKey()
cv2.destroyAllWindows()
