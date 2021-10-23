import cv2
import streamlit as st

open_cam = 0
st.title("RaaS: Recipe as a service")
if(st.button("Open Camera")):
    open_cam = 1
if(st.button("Close Camera")):
    open_cam = 0
take_pic = st.button("Take Picture")
FRAME_WINDOW = st.image([])
camera = cv2.VideoCapture(0)

while(open_cam):
    _, frame = camera.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    FRAME_WINDOW.image(frame)
    if(take_pic):
        cv2.imwrite("test.jpg", frame)
    