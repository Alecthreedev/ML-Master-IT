import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image

# CIFAR-10 class names
class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer',
               'dog', 'frog', 'horse', 'ship', 'truck']

# Load the trained model with error handling
try:
    model = load_model('cifar10_model.h5')
except TypeError as e:
    st.error(f"Error loading model: {e}")
    st.stop()

st.title("CIFAR-10 Image Classifier 🧠")
st.write("Upload a 32x32 RGB image to classify it.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    img = Image.open(uploaded_file).resize((32, 32)).convert('RGB')
    st.image(img, caption='Uploaded Image', use_container_width=True)

    # Preprocess image
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0

    # Predict
    predictions = model.predict(img_array)
    predicted_class = class_names[np.argmax(predictions)]

    st.markdown(f"### 🔍 Prediction: **{predicted_class}**")
