import cv2
import numpy as np
import os
# tuplify
import json

def tup(point):
    return (point[0], point[1])

# returns true if the two boxes overlap


def overlap(source, target):
    # unpack points
    tl1, br1 = source
    tl2, br2 = target

    # checks
    if (tl1[0] >= br2[0] or tl2[0] >= br1[0]):
        return False
    if (tl1[1] >= br2[1] or tl2[1] >= br1[1]):
        return False
    return True

# returns all overlapping boxes


def getAllOverlaps(boxes, bounds, index):
    overlaps = []
    for a in range(len(boxes)):
        if a != index:
            if overlap(bounds, boxes[a]):
                overlaps.append(a)
    return overlaps





def showImage(title, img):
    cv2.imshow(title, img)
    cv2.waitKey(0)


# importing the original image
img = cv2.imread('output\page_5.jpg')
original=img.copy()
showImage("Original", original)


# # Converting to grayscale image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
showImage("Gray scale Image",gray)

# Inverting the image
gray=cv2.bitwise_not(gray)
showImage("Inverted Image",gray)

# Thresholding the image for removal of noise
_,threshold_img = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY)
showImage("Thresholded Image",threshold_img)


# Finding contours in thresholded image
contours, hierarchy = cv2.findContours(threshold_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)





# go through the contours and save the box edges
boxes = []; # each element is [[top-left], [bottom-right]]
hierarchy = hierarchy[0]
for component in zip(contours, hierarchy):
    currentContour = component[0]
    currentHierarchy = component[1]
    x, y, w, h = cv2.boundingRect(currentContour)
    if currentHierarchy[3] < 0:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 1)
        boxes.append([[x, y], [x+w, y+h]])


showImage("Contours", img)


# go through the boxes and start merging
merge_margin = 8

finished = False
highlight = [[0, 0], [1, 1]]
points = [[[0, 0]]]
while not finished:
    # set end con
    finished = True

    # check progress
    print("Len Boxes: " + str(len(boxes)))


    # loop through boxes
    index = len(boxes) - 1
    while index >= 0:
        # grab current box
        curr = boxes[index]

        # add margin
        tl = curr[0][:]
        br = curr[1][:]
        tl[0] -= merge_margin
        tl[1] -= merge_margin
        br[0] += merge_margin
        br[1] += merge_margin

        # get matching boxes
        overlaps = getAllOverlaps(boxes, [tl, br], index)

        # check if empty
        if len(overlaps) > 0:
            # combine boxes
            # convert to a contour
            con = []
            overlaps.append(index)
            for ind in overlaps:
                tl, br = boxes[ind]
                con.append([tl])
                con.append([br])
            con = np.array(con)

            # get bounding rect
            x, y, w, h = cv2.boundingRect(con)

            # stop growing
            w -= 1
            h -= 1
            merged = [[x, y], [x+w, y+h]]

            # highlights
            highlight = merged[:]
            points = con

            # remove boxes from list
            overlaps.sort(reverse=True)
            for ind in overlaps:
                del boxes[ind]
            boxes.append(merged)

            # set flag
            finished = False
            break

        
        # increment
        index -= 1


# show final
copy = np.copy(original)
save_dir = "page_5"

i=0
j = {}

for box in boxes:

    sx = box[0][0]
    sy = box[0][1]
    ex = box[1][0]
    ey = box[1][1]
    w = ex-sx
    h = ey-sy

    f={}

    f["top_left"]=[ex-w,ey]
    f["top_right"] = [ex, ey]
    f["bottom_left"] = [sx, sy]
    f["bottom_right"] = [sx+w, sy]

    j[f"box{i+1}"] = f
    cv2.rectangle(copy, tup(box[0]), tup(box[1]), (0, 200, 0), 1)
    region = copy[box[0][1]:box[1][1], box[0][0]:box[1][0]]

    # Save the region as a separate image in the desired path
    save_path = os.path.join(save_dir, f'bounding_box_{i}.jpg')
    cv2.imwrite(save_path, region)
    i=i+1




# the json file to save the output data
save_file = open("savedata_5.json", "w")
json.dump(j, save_file, indent=6)
save_file.close()

# Displaying and saving the final image
cv2.imshow("Final", copy)
cv2.imwrite("Final5.jpg",copy)
cv2.waitKey(0)
cv2.destroyAllWindows()


