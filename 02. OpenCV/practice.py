import cv2
import sys

img1 = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('cat.bmp', cv2.IMREAD_COLOR)

if img1 is None or img2 is None:
    print('Image load failed!')
    sys.exit()

print(type(img1))
print(img1.shape)
print(img2.shape)

print(img1.dtype)
print(img2.dtype)

if img1.ndim == 2:
    print('img1 is a grayscale image')

h, w = img1.shape
print('w x h = {} X {}'.format(w, h))

h, w = img2.shape[:2]
print('w x h = {} X {}'.format(w, h))

x = 20
y = 10

p1 = img1[y, x]
print(p1)

p2 = img2[y, x]
print(p2)

# too slow! Don't do that // C언어에서는 가능하지만, Python은 굉장히 느림
"""
for y in range(h):
    for x in range(w):
        img1[y, x] = 0
        img2[y, x] = (0, 255, 255) # yellow
"""

img1[:, :] = 0
img2[:, :] = (0, 255, 255)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)

cv2.waitKey()
cv2.destroyAllWindows()