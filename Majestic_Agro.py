import pandas as pd
import streamlit as st
from PIL import Image
import altair as at
import csv
from plyer import gps
st.set_page_config(layout="wide")
hide = """
         <style>
         #MainMenu {visibility: hidden;}
         footer {visibility: hidden;}
         header {visibility: hidden;}
         </style>
         """
st.markdown(hide,unsafe_allow_html=True)
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
gps.start ()
lat1 = " "
lon1 = " "
@kivy.clock.mainthread
def on_location (self, **kwargs):
    for k, v in kwargs.items ():
        if k == "speed":
            break
        if k == "lat":
            lat1 = f"{str (v)}"
        if k == "lon":
            lon1 = f"{str (v)}"
    if lon1 != " " and lat1 != " ":
        gps.stop ()

gps.configure (on_location=on_location)
st.write(f"{lat1}, {lon1}")
st.markdown("<h1 class='title'>MAJESTIC AGRO</h1>", unsafe_allow_html=True)
st.markdown("<h4 class='tit'>'Crop recommendation is a valuable guide for farmers, providing them with expert advice on selecting the most suitable crops to cultivate based on factors like climate, soil conditions, and market demand. This guidance empowers farmers to make informed decisions about crop selection, optimizing yield, profitability, and sustainability. With precise crop recommendations, farmers can maximize resource utilization, minimize environmental impact, and enhance their agricultural practices, ultimately contributing to food security and sustainable farming for a brighter future.'</h2>",unsafe_allow_html=True)
