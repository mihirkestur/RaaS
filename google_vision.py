import io
import os

# Imports the Google Cloud client library
from google.cloud import vision

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="calm-edge-329917-ef2a3b693298.json"


# Instantiates a client
client = vision.ImageAnnotatorClient()

def return_ingredients(img_path):
    # The name of the image file to annotate
    file_name = os.path.abspath(img_path)

    # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    # image = vision.Image(content=content)


    request = {
    "image": {
        "content": content
    },    
    }



    # Performs label detection on the image file
    response = client.annotate_image(request)


    labels = response.localized_object_annotations
    # objects =response.objects
    # print(response)
    li=[]
    print('Labels:')
    for label in labels:
        # print(label.name)
        li.append(label.name)
    
    return li

# AIzaSyCVEGoZN3BZ8Wff3ZgtcbUAIKTJp9SVM5s

