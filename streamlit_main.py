#Build Stramlit App
import streamlit as st
from PIL import Image
import os

from main import *
st.title("Holi Style Your  Image")
hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)
#st.write('Available Style Images:')
image1 = Image.open('images/style-images/holi_style_1.jpg')
image2= Image.open('images/style-images/holi_style_2.jpg')
image3 = Image.open('images/style-images/holi_style_3.jpg')
image4 = Image.open('images/style-images/holi_style_4.jpg')

#display the reference images
st.write('Holi Style Reference Images:')
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.header("Holy Style1")
    st.image(image1, use_column_width=True)
with col2:
    st.header("Holy Style2")
    st.image(image2, use_column_width=True)
with col3:
    st.header("Holy Style3")
    st.image(image3, use_column_width=True)
with col4:
    st.header("Holy Style4")
    st.image(image4, use_column_width=True)



styleOption = st.selectbox( 'Pick your model style', ('style_1', 'style_2', 'style_3','style_4'))
st.write('You selected:', styleOption)

upload_img = st.file_uploader("Upload your image here (png or jpeg or jpg)", type=['png', 'jpg','jpeg'])

if upload_img is not None:
    input_image = Image.open( upload_img )
     
    input_image.save("images/content-images/userinput.png")
    st.image(input_image, caption='Your Image', use_column_width=True)

    output_image_path = 'images/output-images/output-userimage-' + str(styleOption) + '.png'

    

    if st.button('Create Style Transfer Image'):
        compute_style('images/content-images/userinput.png','images/style-images/holi_'+str(styleOption)+'.jpg',output_image_path)
        st.image(output_image_path, caption='Output', use_column_width=True)
    else:
        st.write('Click Button to Run Model!!!')

