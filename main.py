import os
import fitz
import cv2
import numpy as np

# Specify the path to the PDF file
pdf_path = "Sanskrit_Text.pdf"

# Create a directory to save the JPG images
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

# Open the PDF file
pdf = fitz.open(pdf_path)
total_pages = len(pdf)

# Iterate over each page of the PDF
for page_number in range(total_pages):
    # Get the page from the PDF
    page = pdf[page_number]

    # Render the page as an image using PyMuPDF
    pix = page.get_pixmap()
    img = np.frombuffer(pix.samples, dtype=np.uint8).reshape(
        pix.height, pix.width, pix.n)

    # Convert the image to BGR color space
    img_bgr = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    # Save the image as JPG file
    output_path = os.path.join(output_dir, f"page_{page_number + 1}.jpg")
    cv2.imwrite(output_path, img_bgr)
