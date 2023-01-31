import numpy as np
import cv2

img = cv2.imread("/content/Test 1.jpg")
cv2_imshow(img)
imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(imgGrey, 240, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

filtered = []
low = 1000
high = 100000
for contour in contours:
  area = cv2.contourArea(contour)
  if low<area and area<high:
    filtered.append(contour)

print(len(filtered))
