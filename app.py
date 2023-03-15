# importing libaries
import streamlit as st
import requests, os
from dotenv import load_dotenv
import streamlit as st
from PIL import Image


load_dotenv()
## Title of the streamlit app
st.write('# Birdie :bird: ')
st.write(""" Hey :wave: 

Birdie is a web app that recognises your favourite birds and names then.

Drop the link to a bird and let's name it :smiley: 

""")

# Load the values from .env
key = os.environ['KEY']
endpoint = os.environ['ENDPOINT']
project_id = os.environ['PROJECT_ID']
iteration_id = os.environ['ITERATION_ID']

# Create the full URL
constructed_url = endpoint+'/customvision/v3.0/Prediction/'+project_id+'/classify/iterations/'+iteration_id+'/image'

# Set up the header information, which includes our prediction key
headers = {
    'Prediction-Key': key,
    'Content-Type': 'application/json'
    
}

# Get the Url of the test images
img_url = 'https://assets.churchofjesuschrist.org/23/24/2324ae68dedecdab4b205ffa03be9da6915a4910/blue_jay.jpeg'
#'https://www.gannett-cdn.com/authoring/2020/02/02/NCOD/ghows-OH-8241158c-0783-483d-9bc8-ce075e601777-10de8de6.jpeg'
# 'https://www.gannett-cdn.com/authoring/2017/01/07/NFDD/ghows-FD-409d5ddb-f237-376e-e053-0100007f1388-5e110c8a.jpeg'
# 'https://www.gannett-cdn.com/authoring/2009/06/29/NCDT/ghows-MO-93e41979-4424-40e8-9231-f0fb425c8418-2ac59cee.jpeg'
# 'https://assets.churchofjesuschrist.org/23/24/2324ae68dedecdab4b205ffa03be9da6915a4910/blue_jay.jpeg'


with st.sidebar:
    inp_url = st.text_input("Enter the bird URL", img_url, key=1)

# Two columns to show translation and input text
t1, t2 = st.columns(2)




bird_text = ''
with t1:
    st.markdown('#### Upload an image')
    
    image = Image.open(requests.get(inp_url, stream=True).raw)
    st.image(image,
                 use_column_width=True)
    if st.button('Upload', key=23):
        # Create the body of the request with the text to be translated
        body = { "Url": img_url }
        print(inp_url)
        # Make the call using post
        image_request = requests.post(constructed_url, headers=headers, json=body)#, json=body)
        # Retrieve the JSON response
        image_response = image_request.json()
        # Retrieve the translation
        print(image_response)
        bird_text = image_response['predictions'][0]['tagName']
        bird_prob = image_response['predictions'][0]['probability']


with t2:
    st.markdown('#### Bird Name')
    if bird_text != '':
        st.markdown(f'<p style="font-size:16px;padding:8.75px;"> </p>', unsafe_allow_html=True)
        st.markdown(f'<p style="background-color:#D4F1F4;padding:10px;font-size:16px;border-radius:2%;">{bird_text}</p>', unsafe_allow_html=True)
        st.markdown(f'<p style="background-color:#D4F1F4;padding:10px;font-size:16px;border-radius:2%;"> Confidence: {bird_prob}</p>', unsafe_allow_html=True)

