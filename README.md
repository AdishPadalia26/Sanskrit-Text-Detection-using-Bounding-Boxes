# Sanskrit Text Detection using Bounding Boxes

A Python-based toolkit for automatic detection of Sanskrit text regions in PDF files. This project extracts text lines, draws bounding boxes, exports cropped line images, and serializes annotation data to JSON for downstream processing or model training.

---

## Features

- **PDF to Image Conversion:** Converts input PDF pages to high-quality JPG images using PyMuPDF.
- **Robust Contour and Bounding Box Extraction:** Uses OpenCV for noise removal, thresholding, contour detection, and bounding box calculation.
- **Non-Maximum Suppression & Adaptive Box Merging:** Merges overlapping or nearby boxes via custom algorithms and OpenCV NMS.
- **Export Cropped Line Images:** Each detected line is saved as a separate image.
- **Structured JSON Annotation:** Exports coordinates for each bounding box in a multi-point format (top_left, bottom_right, etc.).
- **Visual Verification:** Overlays rectangles on the original page image for quick verification.
- **Customizable Pipeline:** Easily adapt page numbers, margin sizes, thresholds, etc.

---

## Project Structure

```
Sanskrit-Text-Detection-using-Bounding-Boxes/
├── main.py           # PDF-to-image conversion
├── finalImage.py     # Detection, merging, visualization, export (core logic)
├── f.py / faltu.py   # Experiments with contours, NMS, and visualization
├── output/           # Output images and intermediate Python scripts
│   ├── page_1.jpg    # Sample page images (from main.py)
│   ├── bounding_box_*.jpg   # Cropped line images (from finalImage.py)
│   └── *.py          # Snippets exploring specific pipelines
├── savedata_5.json   # JSON annotation for bounding boxes
├── Final5.jpg        # Final image with overlayed bounding boxes
└── README.md
```

---

## How It Works – Step-by-Step

### 1. PDF to Image Conversion (`main.py`)
- Loads a specified PDF using PyMuPDF (`fitz`).
- Iterates through each page, rendering it as a NumPy array.
- Converts each page to BGR (OpenCV standard) and saves as JPG in `output/`.

### 2. Preprocessing and Contour Detection (`finalImage.py`)
- Reads the desired page image.
- Converts to grayscale, inverts image, then applies binary thresholding for noise removal.
- Detects external contours, filtering by hierarchy to focus on main regions.

### 3. Bounding Box Calculation and Merging
- For each contour, computes bounding rectangles.
- Adds a configurable margin to each box before merging.
- Custom overlap and merging logic combines adjacent/overlapping boxes, using a combination of heuristics and OpenCV’s NMS where relevant.

### 4. Export Cropped Line Images & JSON Annotation
- Each final box is used to crop the original image; regions are saved as `bounding_box_{i}.jpg` in a specified folder.
- Coordinates for each bounding box are serialized to JSON in the format:
  ```json
  {
    "box1": {
      "top_left": [x1, y1],
      "top_right": [x2, y1],
      "bottom_left": [x1, y2],
      "bottom_right": [x2, y2]
    },
    ...
  }
  ```
- The JSON output is saved as `savedata_5.json`.

### 5. Visualization
- The final image with all bounding boxes is saved as `Final5.jpg` and displayed with rectangles for fast inspection.

---

## Example Usage

### PDF to Image
```sh
python main.py  # Converts Sanskrit_Text.pdf to JPGs in output/
```

### Detect and Export
Edit `finalImage.py` to specify the desired page (e.g., `'output/page_5.jpg'`).
```sh
python finalImage.py  # Detects, merges, saves boxes and cropped lines, exports JSON
```

---

## Output Samples

- `output/page_5.jpg` – Source image for detection
- `page_5/bounding_box_1.jpg`, etc. – Cropped text lines
- `Final5.jpg` – Verification image
- `savedata_5.json` – All box coordinates for further use

---

## Algorithms & Unique Approaches

- **Image Preprocessing:** Grayscale conversion, inversion, and thresholding optimize contour quality.
- **Box Merging:** Custom logic expands boxes by a margin and merges overlaps, ensuring lines are not split by minor noise.
- **NMS Integration:** Uses OpenCV’s NMS for merging candidate regions, reducing false positives.
- **Flexible Experimentation:** `f.py`, `faltu.py`, and scripts in `output/` demonstrate alternative detection strategies (e.g., Canny edge, flood-fill, area filtering).

---

## Dependencies

- [PyMuPDF (fitz)](https://pymupdf.readthedocs.io/en/latest/) – PDF handling
- [opencv-python](https://opencv.org/) – Core image processing
- [numpy](https://numpy.org/) – Array and math ops
- [Pillow (PIL)](https://python-pillow.org/) – Optional image handling
- [json] – Built-in serialization

Install via:
```sh
pip install pymupdf opencv-python numpy pillow
```
Or:
```sh
pip install -r requirements.txt
```

---

## Roadmap & Future Work

- Integrate OCR (Tesseract, EasyOCR) for text recognition
- Support non-PDF image formats (PNG, TIFF)
- Add batch processing for entire folders
- Enhance box merging with deep learning models (EAST, CRAFT, IndicOCR)
- Build web UI with Flask/FastAPI for interactive annotation

---

## Contributing

Contributions welcome! Please fork, create a feature branch, and submit a PR.

---

## License

MIT License

---

## Author

Adish Padalia  
GitHub: [AdishPadalia26](https://github.com/AdishPadalia26)  
Email: padaliaadish@gmail.com

---
