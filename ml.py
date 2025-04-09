import streamlit as st
from PIL import Image
import pytesseract

# If you're on Windows, uncomment and set your Tesseract path here:
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text(image):
    try:
        text = pytesseract.image_to_string(image)
        return text
    except Exception as e:
        st.error(f"Error: {e}")
        return None

# Streamlit app layout
st.title("Image to Text (OCR)")

# File uploader widget
uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg", "bmp", "tiff"])

if uploaded_file is not None:
    # Open the image
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Image", use_column_width=True)

    # Extract text
    if st.button("Extract Text"):
        text = extract_text(img)
        if text:
            st.subheader("Extracted Text:")
            st.text_area("Text", text, height=200)
