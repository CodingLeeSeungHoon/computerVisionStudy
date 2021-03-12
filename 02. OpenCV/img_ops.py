import numpy as np
import cv2

# new image creates
"""
np.empty((shape), dtype=np.uint8)
np.zeros((shape), dtype=np.uint8) 0으로 모두 채움
np.ones((shape), dtype=np.uint8) 1로 모두 채움
np.full((shape), fill_value, dtype=np.uint8) fill_value로 모두 채움

- shape = (height, width) or (height, width, channel)
- fill_value = int or (B, G, R)
"""
img1 = np.empty((240, 320), dtype=np.uint8)  # grayscale image
img2 = np.zeros((240, 320, 3), dtype=np.uint8)  # color image
img3 = np.ones((240, 320), dtype=np.uint8) * 255  # white
img4 = np.full((240, 320, 3), 128, dtype=np.uint8)  # yellow

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)
cv2.imshow('img4', img4)

cv2.waitKey()
cv2.destroyAllWindows()

"""
extract part of image
슬라이싱만으로는 완전한 분리가 불가능 .copy() 함수를 사용해 완전 분리 가능
슬라이싱으로 떼어낸 부분에 특정 연산을 처리하면, 본 이미지에도 적용됨.
img6를 검정 화면으로 만들면, img5의 일부분에도 검정 화면으로 바뀜.
img7은 .copy()로 완전 복사했기 때문에 바뀌지 않음
"""
img5 = cv2.imread('cat.bmp')
img6 = img5[40:400, 30:150]
img7 = img5[40:400, 30:150].copy()

img6.fill(0)

cv2.circle(img6, (50, 50), 20, (0, 0, 255), 2)

cv2.imshow('img5', img5)
cv2.imshow('img6', img6)
cv2.imshow('img7', img7)

cv2.waitKey()
cv2.destroyAllWindows()