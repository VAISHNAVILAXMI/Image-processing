import cv2

import numpy as np  # Import numpy
import imutils
# Read input image
img = cv2.imread('images1.jpeg')

#Translation
height, width = img.shape[:2]
quarter_height, quarter_width = height / 4, width / 4
T = np.float32([[1, 0, quarter_width], [0, 1, quarter_height]])
img_translation = cv2.warpAffine(img, T, (width, height))
cv2.imshow('Translation', img_translation)
cv2.waitKey(0)
cv2.destroyAllWindows()
Rotated_image = imutils.rotate(img, angle=45) 
cv2.imshow("Rotated", Rotated_image) 
cv2.waitKey(0)
cv2.destroyAllWindows()
resized_image = cv2.resize(img, (200, 500))
cv2.imshow("Scaling",resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
