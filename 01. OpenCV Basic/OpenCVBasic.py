import cv2
import sys

"""
grayscale data : numpy.uint8 (1Byte)
truecolor data : tuple / numpy.ndarray (3Bytes)
>> (Red, Green, Blue) : (255, 255, 255)
"""

print('Hello, OpenCV', cv2.__version__)
img = cv2.imread('cat.bmp', flags=cv2.IMREAD_GRAYSCALE)
cv2.imwrite('cat_gray.jpg', img)

if img is None:
    print('Image load failed!')
    sys.exit()

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', img)
cv2.waitKey()

cv2.destroyAllWindows()