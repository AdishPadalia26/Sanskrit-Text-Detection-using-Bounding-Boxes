import cv2
import numpy as np

# importing the original image
img = cv2.imread('output\page_1.jpg')
# img = cv2.resize(img, [400, 300])
cv2.imshow('Original Image', img)
cv2.waitKey(0)


# Converting to grayscale image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('GrayScale Image', gray)
cv2.waitKey(0)


# normalizedImg = np.zeros((800, 800))
# normalizedImg = cv2.normalize(gray,  normalizedImg, 0, 255, cv2.NORM_MINMAX)
# cv2.imshow('Normalised Image', normalizedImg)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


contours,_=cv2.findContours(gray, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
# # print(len(contours))


# print(len(contours))
# contours = contours[0] if len(contours) == 2 else contours[1]

# l=[]
contours = contours[0] if len(contours) == 2 else contours[1]

# Going through every contours found in the image.
for cnt in contours:

    approx = cv2.approxPolyDP(cnt, 0.009 * cv2.arcLength(cnt, True), True)

    # draws boundary of contours.
    cv2.drawContours(img, [approx], 0, (0, 0, 255), 5)


# cv2.imwrite("grayscale.jpg",gray)
# print(min(l))
# print(max(l))
# print(sum(l)/len(l))
cv2.imshow("Image after thresholding", img)
cv2.waitKey(0)
