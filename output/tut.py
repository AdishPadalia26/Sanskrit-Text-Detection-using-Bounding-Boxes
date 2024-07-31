import cv2

# Let's load a simple image with 3 black squares
image = cv2.imread('output\page_1.jpg')
# Grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Hello", gray)
cv2.waitKey(0)


thresh_image = cv2.threshold(
    gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
cv2.imshow("Hello", thresh_image)
cv2.waitKey(0)

_, threshold = cv2.threshold(gray, 110, 255, cv2.THRESH_BINARY)

# contours,hierarchy = cv2.findContours(
#     thresh_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# # print(len(contours))
# l=[]
# for i, c in enumerate(contours):
#     areaContour = cv2.contourArea(c)
#     # l.append(areaContour)
#     if areaContour < 190 or areaContour > 220:
#         continue
#     # x,y,w,h = cv2.boundingRect(i)
#     # cv2.rectangle(image, (x, y), (x + w, y + h), (255,0,0), 4)
#     # print("Hi")
#     cv2.drawContours(image,contours,i,(255,10,255),4)


# Detecting contours in image.
contours, _ = cv2.findContours(threshold, cv2.RETR_TREE,
                               cv2.CHAIN_APPROX_SIMPLE)

contours = contours[0] if len(contours) == 2 else contours[1]

# Going through every contours found in the image.
for cnt in contours:

    approx = cv2.approxPolyDP(cnt, 0.009 * cv2.arcLength(cnt, True), True)

    # draws boundary of contours.
    cv2.drawContours(image, [approx], 0, (0, 0, 255), 5)
# print(min(l))
# print(max(l))
# print(sum(l)/len(l))
cv2.imshow('Bounding Box', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
