
# Python code to find the co-ordinates of
# the contours detected in an image.
import numpy as np
import cv2

# Reading image
font = cv2.FONT_HERSHEY_COMPLEX
img2 = cv2.imread('output\page_1.jpg', cv2.IMREAD_COLOR)

# Reading same image in another
# variable and converting to gray scale.
img = cv2.imread('output\page_1.jpg', cv2.IMREAD_GRAYSCALE)

# Converting image to a binary image
# ( black and white only image).
_, threshold = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY |cv2.THRESH_OTSU)

cv2.imshow("Image after thresholding", img)
cv2.waitKey(0)

contours, hierarchy = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

print(len(contours))
l=[]
for i, c in enumerate(contours):
    areaContour = cv2.contourArea(c)
    l.append(areaContour)
    if areaContour < 190 or areaContour > 220:
        continue
    # x,y,w,h = cv2.boundingRect(i)
    # cv2.rectangle(image, (x, y), (x + w, y + h), (255,0,0), 4)
    # print("Hi")
    cv2.drawContours(img,contours,i,(255,10,255),4)

print(min(l))
print(max(l))
cv2.imshow("Image after thresholding",img)
cv2.waitKey(0)


