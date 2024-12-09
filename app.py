from dotenv import load_dotenv #install python .env to use this

load_dotenv() ##load all the environment variables from .env

import streamlit as st
import os
from PIL import Image
import google.generativeai as genai


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load gemini pro vision
model=genai.GenerativeModel('gemini-pro-vision')

def get_gemini_response(input, image, prompt):
    response

