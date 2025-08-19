import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from backend.graph import run_chat_graph

st.title("Car Listing Task")

user_text = st.text_area("Enter car description here:")
user_image = st.file_uploader("Upload car image", type=["jpg", "jpeg", "png"])

if st.button("Submit"):
    if not user_text:
        st.warning("Please enter car details!")
    elif not user_image:
        st.warning("Please upload an image!")
    else:
        image_bytes = user_image.read()

    try:
        respnonse = run_chat_graph(user_text, image_bytes)
        st.success("Car details extracted successfully!")
        st.json(respnonse)
    except Exception as e:
        st.error(f"An error occurred: {e}")
        st.stop()