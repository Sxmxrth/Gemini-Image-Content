import os
import streamlit as st
import google.generativeai as genai
from PIL import Image
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")


def get_response(image, input):
    if input != "":
        response = model.generate_content(contents=[input, image])
    else:
        response = model.generate_content(image)
    return response.text


st.header("Gemini LLM application")

st.sidebar.header("Input Section")
st.sidebar.subheader("Enter the text you want to generate the image from")
input = st.sidebar.text_input("Input query")

upload = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if upload is not None:
    image = Image.open(upload)
    st.image(image, caption="Uploaded Image", width=300)

submit = st.button("Generate")

print(input)

if submit:
    response = get_response(image, input)
    st.header("Response")
    st.write(response)
