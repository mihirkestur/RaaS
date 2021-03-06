"""
Recognize food: fruit, vegetable
"""
import io
import os
from datetime import datetime
import streamlit as st
import cv2
from google.cloud import vision_v1p3beta1 as vision

def recognize_food(img_path):
    # Setup google authen client key
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'client_key.json'
    start_time = datetime.now()

    # Read image with opencv
    img = cv2.imread(img_path)

    # # Get image size
    height, width = img.shape[:2]
    #
    # # Scale image
    img = cv2.resize(img, (800, int((height * 800) / width)))
    #
    # # Save the image to temp file
    cv2.imwrite("./media/output.jpg", img)
    #
    # # Create new img path for google vision
    img_path = "./media/output.jpg"
    #
    # # Create google vision client
    client = vision.ImageAnnotatorClient()
    #
    # # Read image fileimage
    with io.open(img_path, 'rb') as image_file:
        content = image_file.read()
    #
    request = {
    "image": {
        "content": content
    },    
    }



    # Performs label detection on the image file
    response = client.annotate_image(request)


    labels = response.localized_object_annotations
    # objects =response.objects
    #image = vision.types.Image(content=content)
    #
    # # Recognize text
    #response = client.label_detection(image=image)
    #labels = response.label_annotations
    #

    print(labels,type(labels))
    ingredients=list()
    for label in labels:
        #if label in fruits or label in vegetables:
        #desc = label.description.lower()
        if(label.name not in ingredients):
            ingredients.append(label.name)
        
    print(ingredients)
    return ingredients

print('---------- Start FOOD Recognition --------')
#list_foods = load_food_name(FOOD_TYPE)
#print(list_foods)
# path = SOURCE_PATH+'.jpg'
# recognize_food(path)
# print('---------- End ----------')