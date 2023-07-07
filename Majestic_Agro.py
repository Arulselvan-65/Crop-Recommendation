import streamlit as st
from PIL import Image
hide = """
         <style>
         #MainMenu {visibility: hidden;}
         footer {visibility: hidden;}
         header {visibility: hidden;}
         </style>
         """
st.markdown(hide,unsafe_allow_html=True)

with open("ma.css") as f:
    st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)

img = Image.open("Majestic Agro.png")
st.image(img,width=800)