import streamlit as st
import os
from dotenv import load_dotenv
import google.genai as genai
load_dotenv()

API_KEY = os.getenv("API_KEY")

client = genai.Client(api_key=API_KEY)


#1. AI Cover Letter Generator
#Create a Streamlit app that:
#- Takes job title and resume summary as input
#- Uses google-generativeai gemini-pro model
#- Prompts Gemini: &quot;Write a cover letter for [job_title] using these resume points:
#[summary]&quot;
#- Displays the output below a submit button

st.title('AI Cover Gnerator')

Job_title = st.text_input("Enter Job Title:")

summary= st.text_input("Enter Resume Summary:")

prompt = f"Write a cover letter for {Job_title} using these resume points: {summary}"

if st.button("Generate Cover Letter"):
    response = client.models.generate_content(
        model = "gemini-2.5-flash",
        contents = prompt)
    st.write(response.text)