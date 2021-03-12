import cv2
import numpy as np

img = np.full((400, 400, 3), 255, dtype=np.uint8)

"""
draw line
cv2.line(image, pt1, pt2, color, thickness=1, lineType=None, shift=None)
"""
cv2.line(img, (50, 50), (200, 50), (0, 0, 255), 5)
cv2.line(img, (50, 60), (150, 160), (0, 255, 255), 5)


"""
draw rectangle
cv2.rectangle(image, (x, y, w, h), color, thickness)
cv2.rectangle(image, end-pt1, end-pt2, color, thickness)
"""
cv2.rectangle(img, (50, 200, 150, 100), (0, 255, 0), 2)
cv2.rectangle(img, (70, 220), (180, 280), (0, 128, 0), -1)


"""
draw circles
cv2.circle(img, center, radius, color, thickness, lineType)
"""
cv2.circle(img, (300, 100), 30, (255, 255, 0), -1, cv2.LINE_AA)
cv2.circle(img, (300, 100), 60, (255, 0, 0), 3, cv2.LINE_AA)


"""
draw polylines
cv2.polylines(img, pts, isClosed, color, thickness, lineType)
pts = numpy.ndarray 리스트
isClosed = True or False
"""
pts = np.array([[250, 200], [300, 200], [350, 300], [250, 300]])
cv2.polylines(img, [pts], True, (255, 0, 255), 3, lineType=cv2.LINE_AA)

"""
put text
cv2.putText(img, text, org, fontFace, fontScale, color, thickness, lineType, bottomLeftOrigin)
"""

text = 'Hello? OpenCV ' + cv2.__version__
cv2.putText(img, text, (50, 350), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 1, cv2.LINE_AA)
cv2.imshow('img', img)

cv2.waitKey()
cv2.destroyAllWindows()