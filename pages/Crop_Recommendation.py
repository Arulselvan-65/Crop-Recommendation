import streamlit as st
import pandas as pd
import csv
import altair as at
import plotly.express as px
hide = """
         <style>
         #MainMenu {visibility: hidden;}
         footer {visibility: hidden;}
         header {visibility: hidden;}
         </style>
         """

st.markdown(hide,unsafe_allow_html=True)
st.markdown(
    """
    <style>
    .tit {
        font-size: 50px;
        text-align: center;
        padding-top: 1px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
st.markdown("<h1 class='tit'>Crop Recommendation</h1>", unsafe_allow_html=True)
