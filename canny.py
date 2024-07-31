import cv2


def showImage(title, img):
    cv2.imshow(title, img)
    cv2.waitKey(0)

# importing the original image
img = cv2.imread('output\page_1.jpg')


# Setting parameter values
t_lower = 100  # Lower Threshold
t_upper = 150  # Upper threshold

# Applying the Canny Edge filter
edge = cv2.Canny(img, t_lower, t_upper)

showImage('original', img)
showImage('edge', edge)






cv2.destroyAllWindows()
