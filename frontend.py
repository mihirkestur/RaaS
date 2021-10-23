import streamlit as st
import os
import cv2
st.set_page_config(page_title='Upload Image', layout = 'centered', initial_sidebar_state = 'auto')
st.title("RaaS: Recipe as a service")
take_pic = st.button("Take Picture")
FRAME_WINDOW = st.image([])
camera = cv2.VideoCapture(0)
image_file = st.file_uploader("Upload A File",type=['png','jpeg','jpg'])
if image_file is not None:
    file_details = {"FileName":image_file.name,"FileType":image_file.type}
    filetype = {image_file.type}
    if filetype == {'image/png'} or filetype == {'image/jpeg'} or filetype == {'image/jpg'}:
	    st.image(image_file)
	    if st.button("Save file"):
		    with open(os.path.join("./",image_file.name),"wb") as f: 
		      f.write(image_file.getbuffer())         
		    st.success("File Saved!")
    else:
        st.write("No Preview Available!")
        if st.button("Save file"):
            with open(os.path.join("./",image_file.name),"wb") as f: 
                f.write(image_file.getbuffer())         
            st.success("File Saved!")
if(take_pic):
    _, frame = camera.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    FRAME_WINDOW.image(frame)
    cv2.imwrite("test.jpg", frame)