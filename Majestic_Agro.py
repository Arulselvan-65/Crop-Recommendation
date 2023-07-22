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
try:
    def on_location (self, **kwargs):
        for k,v in kwargs.items():
            if k == "speed":
                    break
            if k == "lat":
                    self.lat1 = f"{str(v)}"
            if k == "lon":
                    self.lon1 = f"{str(v)}"
        if self.lon1 != " " and self.lat1 != " ":
                gps.stop()
        api = "2af0b7632c24e579e006a7757b110960"
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={10.827022052142183}&lon={77.06067873809651}&appid={api}"
        self.x = url.json ()
        if self.x ["cod"] != "404":
            temp = round (self.x ["main"] ["temp"] - 273.15)
            humi = self.x ["main"] ["humidity"]
            weather = self.x ["weather"] [0] ["main"]
            feels = round (self.x ["main"] ["feels_like"] - 273.15)
            wind = round (self.x ["wind"] ["speed"] * 18 / 5)
            id1 = str (self.x ["weather"] [0] ["id"])
            if id1 == "800":
                self.scr1.ids.img_src.source = "sunny"
            if "200" <= id1 <= "232":
                self.scr1.ids.img_src.source = "thunder"
            if "300" <= id1 <= "321" or "500" <= id1 <= "531":
                self.scr1.ids.img_src.source = "rain"
            if "600" <= id1 <= "622":
                self.scr1.ids.img_src.source = "snow"
            if "701" <= id1 <= "781":
                self.scr1.ids.img_src.source = "fog"
            if "801" <= id1 <= "804":
                self.scr1.ids.img_src.source = "clouds"
except:
    pass
st.markdown("<h1 class='title'>MAJESTIC AGRO</h1>", unsafe_allow_html=True)
st.markdown("<h4 class='tit'>'Crop recommendation is a valuable guide for farmers, providing them with expert advice on selecting the most suitable crops to cultivate based on factors like climate, soil conditions, and market demand. This guidance empowers farmers to make informed decisions about crop selection, optimizing yield, profitability, and sustainability. With precise crop recommendations, farmers can maximize resource utilization, minimize environmental impact, and enhance their agricultural practices, ultimately contributing to food security and sustainable farming for a brighter future.'</h2>",unsafe_allow_html=True)
