#Build Stramlit App
import streamlit as st
from PIL import Image
import os
#from neural_style import neural_style
#from neural_style import * #check_paths, train, stylize, stylize_onnx_caffe2, main
from main import *
st.title("Holi Style Your  Image")

#st.write('Available Style Images:')

candy_image = Image.open('images/style-images/holi_style_1.jpg')
mosaic_image = Image.open('images/style-images/holi_style_2.jpg')
rain_princess_image = Image.open('images/style-images/holi_style_2.jpg')


#display the reference images
st.write('Holi Style Reference Images:')
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.header("Holy Style1")
    st.image(candy_image, use_column_width=True)
with col2:
    st.header("Holy Style2")
    st.image(mosaic_image, use_column_width=True)
with col3:
    st.header("Holy Style3")
    st.image(rain_princess_image, use_column_width=True)


#st.image(candy_image, caption='Candy Style Source Image', use_column_width=True)

#pick model
styleOption = st.selectbox( 'Pick your model style', ('style_1', 'style_2', 'style_3'))
st.write('You selected:', styleOption)

upload_img = st.file_uploader("Upload your image here (png or jpg)", type=['png', 'jpg'])

if upload_img is not None:
    input_image = Image.open( upload_img )
    #input_image = Image.open(user_image.read(), encoding="utf-8")

    #Want to replace input image so as not to take up space with each new one 
    input_image.save("images/content-images/userinput.png")
    st.image(input_image, caption='Your Image', use_column_width=True)

    #st.write( 'image name: ', user_image.name)
    #print(user_image.name)

    #input_img_name = str(user_image.name).replace(' ', '-')
    #rename file to that of input_img_name: 
    #os.system('mv images/content-images/' + str(user_image.name) + ' images/content-images/' + input_img_name )

    #print(input_img_name)

    
    #save one unique image per styleOption, doesn't clog up too much but also doesn't erase some recents
    output_image_path = 'images/output-images/output-userimage-' + str(styleOption) + '.png'

    

    if st.button('Create Style Transfer Image'):
        compute_style('images/content-images/userinput.png','images/style-images/holi_'+str(styleOption)+'.jpg',output_image_path)
        st.image(output_image_path, caption='Output', use_column_width=True)
    else:
        st.write('click button to run model')

#accept_multiple_files=True -> something could be added #restrict file type to png and jpg. On fully deployed webapp dont want a user uploading erroneous or malicious files, hence this restriction

#run once file is downloaded 
#if uploaded_file is not None:
