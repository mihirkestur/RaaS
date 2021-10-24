import streamlit as st
import os
import cv2
import search
import main
st.set_page_config(page_title='RaaS', layout = 'wide', initial_sidebar_state = 'auto')
m = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #F2DEDA;
    color:#F24E2B;
    border-color:#FFFFFF
}
div.stButton > button:hover {
    background-color: #F24E2B;
    color:#F2DEDA;
    }
div.sttext > text:first-child {
    color:#FFFFFF
}
</style>""", unsafe_allow_html=True)
st.title("RaaS: Recipes as a service")
take_pic = st.button("Take Picture")
image_file = st.file_uploader("Upload an image",type=['png','jpeg','jpg'])
def predict():
    return main.recognize_food('./test.jpg')
    
if image_file is not None:
    file_details = {"FileName":image_file.name,"FileType":image_file.type}
    filetype = {image_file.type}
    if filetype == {'image/png'} or filetype == {'image/jpeg'} or filetype == {'image/jpg'}:
        st.image(image_file)
        with open(os.path.join("./","test.jpg"),"w") as f: 
            f.write(image_file.getbuffer())         
            st.success("File Saved!")
            
    else:
        st.write("No Preview Available!")
        if st.button("Save file"):
            with open(os.path.join("./","test.jpg"),"w") as f: 
                f.write(image_file.getbuffer())         
            st.success("File Saved!")
if(take_pic):
    FRAME_WINDOW = st.image([])
    camera = cv2.VideoCapture(0)
    _, frame = camera.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    FRAME_WINDOW.image(frame)
    cv2.imwrite("test.jpg", frame)

if(st.button("RaaS it")):
    
    ingredients = predict()
    recipes = search.get_recipes(ingredients)
    for i in recipes[:10]:
        st.text("**----------------------------------**")
        st.write("**Recipe name: **", str(i["recipe"]))
        st.write("**Prep time: **", str(i["preptime"]))
        st.write("**Cook time: **",  str(i["cooktime"]))