import streamlit as st
import os
padding_top = 0

global uploaded_file
global name_file
    
st.markdown(
    """
    <style>
    
    
    body {
        background-color: white;
    }
    
    
    .reportview-container .main .block-container{{
        padding-top: {padding_top}rem
    }}
        
        
    #MainMenu {visibility: hidden;}
    .stDeployButton {display:none;}
    footer {visibility: hidden;}
    #stDecoration {display:none;}
        
                
    .block-container{
        padding-top: 0px;
        }

    </style>
    """,
    
    unsafe_allow_html=True
)


def get_image_path(img):
    file_path = f"static/uploads/{img.name}"
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "wb") as img_file:
        img_file.write(img.getbuffer())
    return file_path , img.name


#? save file and display it...
def check_img(uploaded_file):
    if uploaded_file is not None:
        bytes_data , file_name = get_image_path(uploaded_file)
        return file_name  




def predict(image_path):
    import cv2
    import numpy as np
    import streamlit as st
    import tensorflow as tf
    from tensorflow.keras.preprocessing import image
    from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2,preprocess_input as mobilenet_v2_preprocess_input

    model = tf.keras.models.load_model('static/dataSet/mdl_wt.hdf5') #? Orignal

    map_dict = {0: 'Dog',1: 'Horse',2: 'Elephant',3: 'Butterfly',4: 'Chicken',5: 'Cat'}

    uploaded_file = image_path
    
    if uploaded_file is not None:
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)

        opencv_image = cv2.imdecode(file_bytes, 1)

        opencv_image = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2RGB)

        resized = cv2.resize(opencv_image,(224,224))


        resized = mobilenet_v2_preprocess_input(resized)
        img_reshape = resized[np.newaxis,...]

        prediction = model.predict(img_reshape).argmax()

        print("Predicted Label for the image is {}".format(map_dict [prediction]))            

    return format(map_dict [prediction])




# process the whole classification here get result , upload it to file , fetch the result form it for later use

uploaded_file = st.file_uploader("Upload a file", type=["jpg", "jpeg", "png", "gif", "pdf"] )

name_file = check_img(uploaded_file)

animal = predict(uploaded_file)



with open("image_Name.txt", "w") as file:
    file.write(name_file)
    
with open("animal_Name.txt", "w") as file:
    file.write(animal)