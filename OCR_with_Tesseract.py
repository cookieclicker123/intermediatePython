from PIL import Image, ImageFilter
import pytesseract
import cv2
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'

def preprocess_image(image_path):
    image = cv2.imread(image_path)
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Increase contrast (optional)
    alpha = 1.5  # Contrast control (1.0-3.0)
    beta = 0     # Brightness control (lower increases brightness)
    contrasted_image = cv2.convertScaleAbs(grayscale_image, alpha=alpha, beta=beta)

    # Apply thresholding to make the text stand out
    ret, threshold_image = cv2.threshold(contrasted_image, 127, 255, cv2.THRESH_BINARY)

    # Apply blur to reduce noise (optional)
    blur = cv2.medianBlur(threshold_image, 3)

    cv2.imwrite("/tmp/preprocessed_image.png", blur)
    return Image.open("/tmp/preprocessed_image.png")


# Test with an example image
processed_image = preprocess_image("/Users/seb/Documents/intermediatePython/white.png")
processed_image.show()

def extract_text(image):
    # Extract text using pytesseract
    text = pytesseract.image_to_string(image)

    return text

# Extract text from the preprocessed image
extracted_text = extract_text(processed_image)
print("Extracted Text:")
print(extracted_text)



