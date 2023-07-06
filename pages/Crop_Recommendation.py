import streamlit as st
import pickle
import numpy as np
import xgboost
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
    .cont{
        font-size: 50px;
        text-align: center;
        padding-top: 1px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)
st.markdown("<h1 class='tit'>Crop Recommendation</h1>", unsafe_allow_html=True)

nitrogen_val = st.text_input("Nitrogen Content", placeholder="Eg(72)")
st.write("\n\n\n")
phosphorus_val = st.text_input("Phosphorus Content", placeholder="Eg(65)")
st.write("\n\n\n")
potassium_val = st.text_input("Potassium Content", placeholder="Eg(77)")
st.write("\n\n\n")
temp_val = st.text_input("Temperature", placeholder="Eg(20.87974371)")
st.write("\n\n\n")
humi_val = st.text_input("Humidity", placeholder="Eg(82.00274423)")
st.write("\n\n\n")
ph_val = st.text_input("pH Value", placeholder="Eg(6.877)")
st.write("\n\n\n")
rain_val = st.text_input("Rainfall", placeholder="Eg(98.28583013)")
st.write("\n\n\n")
if nitrogen_val and potassium_val and phosphorus_val and temp_val and humi_val and ph_val and rain_val:
    a = [int(nitrogen_val),int(potassium_val),int(phosphorus_val),float(temp_val),float(humi_val),float(ph_val),float(rain_val)]
    loaded = pickle.load(open("crop_predict.pkl","rb"))
    prediction = loaded.predict(np.array([a]))
    d = {20: 'rice', 11: 'maize', 3: 'chickpea', 9: 'kidneybeans', 18: 'pigeonpeas', 13: 'mothbeans', 14: 'mungbean', 2: 'blackgram',
           10: 'lentil', 19: 'pomegranate', 1: 'banana', 12: 'mango', 7: 'grapes', 21: 'watermelon', 15: 'muskmelon', 0: 'apple', 16: 'orange',
           17: 'papaya', 4: 'coconut', 6: 'cotton', 8: 'jute', 5: 'coffee'}
    pred = d[prediction[0]]
    st.markdown(f"<h1 class='tit'>{pred}</h1>", unsafe_allow_html=True)

