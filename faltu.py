import cv2
import numpy as np


def showImage(title, img):
    cv2.imshow(title, img)
    cv2.waitKey(0)


# Create a list of bounding boxes
bounding_boxes = [
    # Example bounding box 1: top-left (100, 100), bottom-right (200, 200)
    [(100, 100), (200, 200)],
    # Example bounding box 2: top-left (150, 150), bottom-right (250, 250)
    [(150, 150), (250, 250)],
    # Example bounding box 3: top-left (300, 300), bottom-right (400, 400)
    [(300, 300), (400, 400)],
    # Example bounding box 4: top-left (350, 350), bottom-right (450, 450)
    [(350, 350), (450, 450)]
]

# Convert bounding box coordinates to the format required by OpenCV's NMSBoxes function
boxes = [cv2.boundingRect(np.array(box)) for box in bounding_boxes]
# Example scores for each bounding box (you can adjust according to your needs)
scores = [1.0, 1.0, 1.0, 1.0]

# Apply Non-Maximum Suppression (NMS)
indices = cv2.dnn.NMSBoxes(
    boxes, scores, score_threshold=0.5, nms_threshold=0.5)

# Merge nearby bounding boxes
merged_boxes = []
for idx in indices.flatten():
    x, y, w, h = boxes[idx]
    merged_boxes.append([(x, y), (x + w, y + h)])

# Draw merged bounding boxes on the image
img = np.zeros((500, 500, 3), dtype=np.uint8)  # Example black image
for box in merged_boxes:
    cv2.rectangle(img, box[0], box[1], (0, 255, 0), 2)

# Display the image with merged bounding boxes
showImage('Merged Bounding Boxes', img)
