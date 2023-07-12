import pandas as pd
import streamlit as st
from PIL import Image
import altair as at
import csv
st.set_page_config(layout="wide")
hide = """
         <style>
         #MainMenu {visibility: hidden;}
         footer {visibility: hidden;}
         header {visibility: hidden;}
         </style>
         """
st.markdown(hide,unsafe_allow_html=True)
img = Image.open("farm.jpg")
st.write("\n\n\n\n")
st.write("\n\n\n\n")

with open("ma.css") as f:
    st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)
st.markdown(
    """
    <style>
    .title {
        font-size: 120px;
        text-align: center;
        color: #FAF0D7;
    }
    .tit
{
        background-color: rgba(0, 0, 0, 0.5);
        border-radius: 20px;
        font-size: 25px;
        color: black;
        text-align: center;
        margin-top: 150px;
         font-family: 'PT Serif', serif;
         color: white;}
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("<h1 class='title'>MAJESTIC AGRO</h1>", unsafe_allow_html=True)
st.markdown("<h4 class='tit'>'Crop recommendation is a valuable guide for farmers, providing them with expert advice on selecting the most suitable crops to cultivate based on factors like climate, soil conditions, and market demand. This guidance empowers farmers to make informed decisions about crop selection, optimizing yield, profitability, and sustainability. With precise crop recommendations, farmers can maximize resource utilization, minimize environmental impact, and enhance their agricultural practices, ultimately contributing to food security and sustainable farming for a brighter future.'</h2>",unsafe_allow_html=True)