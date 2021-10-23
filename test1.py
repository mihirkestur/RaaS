import cv2
import streamlit as st
st.title("RaaS: Recipe as a service")
take_pic = st.button("Take Picture")
FRAME_WINDOW = st.image([])
camera = cv2.VideoCapture(0)

def take(frame):
    cv2.imwrite("test.jpg", frame)

while(1):
    _, frame = camera.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    FRAME_WINDOW.image(frame)