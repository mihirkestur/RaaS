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
a:link, a:visited {
  background-color: #9A9483;
  color: white;
  padding: 15px 25px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
}

a:hover, a:active {
  background-color: #E5DCC3;
</style>""", unsafe_allow_html=True)
st.title("RaaS: Recipes as a service")
take_pic = st.button("Take Picture")
image_file = st.file_uploader("Upload an image",type=['png','jpeg','jpg'])
def predict():
    return main.recognize_food('./media/test.jpg')
    
if image_file is not None:
    filetype = {image_file.type}
    if filetype == {'image/png'} or filetype == {'image/jpeg'} or filetype == {'image/jpg'}:
        st.image(image_file)
        with open(os.path.join("./media","test.jpg"),"wb") as f: 
            f.write(image_file.getbuffer())         
            st.success("File Saved!")
            
    else:
        st.write("No Preview Available!")
        with open(os.path.join("./media","test.jpg"),"wb") as f: 
            f.write(image_file.getbuffer())         
        st.success("File Saved!")
if(take_pic):
    FRAME_WINDOW = st.image([])
    camera = cv2.VideoCapture(0)
    _, frame = camera.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    FRAME_WINDOW.image(frame)
    cv2.imwrite("./media/test.jpg", frame)

if(st.button("RaaS it")):
    
    ingredients = predict()
    recipes = search.get_recipes(ingredients)
    for i in recipes[:10]:
        st.text("**----------------------------------**")
        st.write("**Recipe name: **", str(i["recipe"]))
        link = f'[Link to Recepie]({str(i["URL"])})'
        st.markdown(link, unsafe_allow_html=True)
        st.write("**Prep time: **", str(i["preptime"]))
        st.write("**Cook time: **",  str(i["cooktime"]))

st.write("**------------------------------------------------------------**")

st.markdown("<p style='font-family:courier;'>Built by:</p>", unsafe_allow_html=True)
rahul = "<a id = 1 href='https://www.linkedin.com/in/rahulssrinivas/' target='_blank'>Rahul S Srinivas</a>"
santosh = "<a id = 1 href='https://github.com/santoshbishnoi' target='_blank'>Santosh Bishnoi</a>"
rohit = "<a id = 1 href='https://github.com/sir-rohitravindra' target='_blank'>Rohit Ravindra</a>"
mihir = "<a id = 1 href='https://github.com/mihirkestur' target='_blank'>Mihir M Kestur</a>"
st.markdown(rahul + santosh + rohit + mihir, unsafe_allow_html=True)