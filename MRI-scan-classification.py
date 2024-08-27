# Import necessary libraries
import cv2
import numpy as np
import torch
import streamlit as st
from PIL import Image
from ultralytics import YOLOv10

# Load the pre-trained YOLO model (ensure the model file is in the correct path)
model_path = "best.pt"
model = YOLOv10(model_path)
# model = torch.hub.load('ultralytics/yolov10', 'custom', path='best.pt')

# Define a function to make predictions on the input image
def predict(image):
    # Run the YOLO model on the input image
    results = model.predict(source = image, imgsz = 640, conf = 0.25)
    # annotated_img = results.plot()
    # annotated_img[:, :, ::-1]
    # results = model(image, size=640, conf=0.25)
    
    # Plot the results (annotated image with detections)
    annotated_img = results.render()[0]
    return annotated_img

# Streamlit app setup
st.title("Brain Tumor Detection Using YOLOv5")
st.write("Upload an MRI scan of the brain, and the YOLOv5 model will detect and annotate any tumors.")

# File uploader for input image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Read the image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    
    # Run detection
    st.write("Detecting...")
    annotated_img = predict(np.array(image))
    
    # Display the annotated image
    st.image(annotated_img, caption='Annotated Image.', use_column_width=True)
