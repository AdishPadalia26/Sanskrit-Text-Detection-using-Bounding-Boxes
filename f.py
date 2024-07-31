import cv2
import numpy as np


def showImage(title, img):
    cv2.imshow(title, img)
    cv2.waitKey(0)


# importing the original image
img = cv2.imread('output\page_1.jpg')



# # Converting to grayscale image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
showImage("gray",gray)

gray=cv2.bitwise_not(gray)
showImage("Inverted",gray)

_,threshold_img = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY)
showImage("threshold",threshold_img)

canny = cv2.Canny(threshold_img, 122, 124)  # Canny
# Finding Contours
contours, hierarchy = cv2.findContours(
    canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for c in contours:
    x, y, w, h = cv2.boundingRect(c)
    # Draw the bounding box rectangle
    cv2.rectangle(canny, (x, y), (x + w, y + h), (0, 255, 0), 3)

# cv2.drawContours(canny, contours, -1, 255, 6)
showImage("Contours", canny)


# Get mask for floodfill
h, w = canny.shape[:2]
print(h," ",w)
mask = np.zeros((h+2, w+2), np.uint8)
showImage("Mask",mask)

cv2.floodFill(canny, mask, (0, 0), 123)
showImage("Flood Fill",canny)


canny = cv2.inRange(canny, 122, 124)

showImage("Canny", canny)






# print(img.shape," ",canny.shape)

# # cv2.findContours

# # # Overlay the mask image on the original image using bitwise operations
# # result_image = cv2.bitwise_and(img, canny)

# # # Display the result
# # showImage('Contours on Original Image', result_image)


# # # print("Number of Contours found = " + str(len(contours)))
# # # # biggest_contour=min(contours,key=cv2.contourArea)
# # # # cv2.drawContours(img,contours,-1,(0,0,255),2)
# # # for c in contours:
# # #     x, y, w, h = cv2.boundingRect(c)
# # #     # Draw the bounding box rectangle
# # #     cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)


# # # # (cv2.boundingRect(cv2.drawContours(img,contours,-1,(0,0,255),4))
# # # # )
# # # # for i, c in enumerate(contours):
# # # #     areaContour = cv2.contourArea(c)
# # # #     # l.append(areaContour)
# # # #     if areaContour < 15 or areaContour > 220:
# # # #         continue
    
# # # #     print("Hi")
# # # #     x, y, w, h = cv2.boundingRect(c)
# # # #     # Draw the bounding box rectangle
# # # #     cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
# # # #     # x,y,w,h = cv2.boundingRect(i)
# # # #     # cv2.rectangle(image, (x, y), (x + w, y + h), (255,0,0), 4)
# # # #     # print("Hi")





# # # cv2.imshow('Contours with Bounding Boxes', img)
# # # cv2.waitKey(0)
# # # cv2.destroyAllWindows()


# # Convert the flood fill mask to a binary image
# # ret, binary_mask = cv2.threshold(canny, , 255, cv2.THRESH_BINARY)

# # Find contours in the binary mask
# contours, _ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# # Create a blank mask image
# mask_image = np.zeros_like(img)

# # Draw contours on the mask image
# cv2.drawContours(mask_image, contours, -1,(255, 255, 0), thickness=cv2.FILLED)

# # Overlay the mask image on the original image using bitwise operations
# result_image = cv2.bitwise_and(img, mask_image)

# # Display the result
# showImage('Contours on Original Image', result_image)
