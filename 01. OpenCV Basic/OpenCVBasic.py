import cv2
import sys
import matplotlib.pyplot as plt
ESC = 27
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
while True:
    if cv2.waitKey() in [ESC, ord('x')]:
        break

cv2.destroyAllWindows()


"""
matplotlib를 이용한 영상출력
cv2.imread() : BGR 순서
matplotlib : RGB 순서 >> cv2.cvtColor() 함수를 사용해서 변경해줌

plt.imshow()에서 cmap='gray' 출력해 grayscale 이미지 출력
"""

imgBGR = cv2.imread('cat.bmp')
imgGray = cv2.imread('cat_gray.jpg')
imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)

plt.axis('off')
plt.imshow(imgRGB)
plt.show()

# 두 개의 영상을 함께 출력
# 121 : 창 1개에 2개의 영상칸 그 중에 1번째 영상칸 선택
plt.subplot(121), plt.axis('off'), plt.imshow(imgRGB)
plt.subplot(122), plt.axis('off'), plt.imshow(imgGray, cmap='gray')
plt.show()