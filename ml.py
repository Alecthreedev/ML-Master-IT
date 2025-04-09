import pytesseract
from PIL import Image

# If you're on Windows, set the tesseract executable path like this:
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def image_to_text(image_path):
    try:
        # Open the image with PIL
        img = Image.open(image_path)

        # Use pytesseract to do OCR on the image
        text = pytesseract.image_to_string(img)

        print("Extracted Text:")
        print(text)
    except Exception as e:
        print("Error:", e)

# Example usage
image_to_text("example.png")
