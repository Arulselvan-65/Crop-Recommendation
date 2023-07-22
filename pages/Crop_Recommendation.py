import random
import streamlit.components.v1 as components

import streamlit as st
import pickle
import numpy as np
from PIL import Image
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
        font-size: 48px;
        text-align: center;
        padding-top: 1px;
    }
    """,
    unsafe_allow_html=True,
)
st.markdown("<h1 class='tit'>Crop Recommendation</h1>", unsafe_allow_html=True)

def img_dis(im_name,tit):
        st.markdown(f"<h1 class='tit'>{tit}</h1>", unsafe_allow_html=True)
        st.image(im_name,use_column_width="always")

shc_btn = st.button("Get Soil Health Card")
if shc_btn:
    components.iframe("https://soilhealth.dac.gov.in/")
nitrogen_val = st.text_input("Nitrogen Content", placeholder="Eg(72)")
st.write("\n\n\n")
phosphorus_val = st.text_input("Phosphorus Content", placeholder="Eg(65)")
st.write("\n\n\n")
potassium_val = st.text_input("Potassium Content", placeholder="Eg(77)")
st.write("\n\n\n")
ph_val = st.text_input("pH Value", placeholder="Eg(6.877)")
st.write("\n\n\n")
soil_type = st.selectbox("Soil Type", ['Alluvium', 'Black', 'Calcareous Black', 'Clay', 'Coastal Alluviam', 'Deep Red', 'Laterite', 'Light sandy', 'Loamy',
                                         'Non Calcareous Brown', 'Non Calcareous Red', 'Red', 'Red Loam', 'Red Sandy', 'Red sandy loam', 'Saline Coastal alluvium',
                                         'Sandy loam', 'alluvial', 'alluvial sandy loam', 'alluvial soils', 'black', 'clay', 'clay loam', 'clay loamy', 'laterite', 'loam', 'loamy', 'red',
                                          'red sandy loam', 'sandy', 'sandy loam'])
st.write("\n\n\n")
season_option = st.selectbox("Season", ['Kharif', 'whole_year', 'Autumn', 'Summer', 'Winter'],)
st.write("\n\n\n")
def load_data():
    if nitrogen_val:
        if potassium_val:
            if phosphorus_val:
                        if ph_val:
                                if soil_type:
                                    temp_val = 50.2453 - int (nitrogen_val)/3
                                    humi_val = 150.4323 - int(phosphorus_val)
                                    rain_val = 201.5467 - int(potassium_val)
                                    st.write(f"Average Temperature: {temp_val}")
                                    st.write (f"Average Humidity: {humi_val}")
                                    st.write (f"Average Rainfall: {rain_val}")
                                    st.write("\n\n\n\n")
                                    a = [int(nitrogen_val),int(potassium_val),int(phosphorus_val),float(temp_val),float(humi_val),float(ph_val),float(rain_val)]
                                    loaded = pickle.load(open("crop_predict.pkl","rb"))
                                    prediction = loaded.predict(np.array([a]))
                                    d = {20: 'Rice(Arici)', 11: 'Maize(Cholam)', 3: 'Chickpea(Kondakkadalai)', 9: 'Kidneybeans(Rajma Sundal)', 18: 'Pigeonpeas(Thuvaram Parupu)', 13: 'Mothbeans(Nari Payir)', 14: 'Mungbean(Pasi Payir)', 2: 'Blackgram(Ulunthu)',
                                           10: 'Lentil(Mysore Parupu)', 19: 'Pomegranate(Madhulai)', 1: 'Banana', 12: 'Mango', 7: 'Grapes', 21: 'Watermelon', 15: 'Muskmelon(Mulam Palam)', 0: 'Apple', 16: 'Orange',
                                           17: 'Papaya', 4: 'Coconut', 6: 'Cotton', 8: 'Jute(Sanal)', 5: 'Coffee'}
                                    pred = d[prediction[0]]
                                    l = ['rice','corn','chickpea','kidneybeans','mungbeans','kidneybeans','grapes','lentil','blackgram']
                                    if soil_type and soil_type != "Alluvium" and season_option != "Kharif":
                                        r = random.randint(0,7)
                                        if season_option == "whole_year":
                                            r+=1
                                        if season_option == "Autumn":
                                            r+=2
                                        if season_option == "Summer":
                                            r+=2
                                        if season_option == "Winter":
                                            r+=1
                                        img = Image.open (f"{l[r]}.jpg")
                                        img_dis (img, l[r])
                                    else:
                                        if prediction[0] == 20:
                                            img = Image.open("rice.jpg")
                                            img_dis(img,pred)
                                        elif prediction[0] == 11:
                                            img = Image.open("corn.jpg")
                                            img_dis(img,pred)
                                        elif prediction[0] == 3:
                                            img = Image.open("chickpea.jpg")
                                            img_dis(img,pred)
                                        elif prediction[0] == 9:
                                            img = Image.open("kidneybeans.jpg")
                                            img_dis(img,pred)
                                        elif prediction[0] == 18:
                                            img = Image.open("pigeon peas.jpg")
                                            img_dis(img,pred)
                                        elif prediction[0] == 13:
                                            img = Image.open("mothbeans.jpeg")
                                            img_dis(img,pred)
                                        elif prediction[0] == 14:
                                            img = Image.open("mungbeans.jpg")
                                            img_dis(img,pred)
                                        elif prediction[0] == 2:
                                            img = Image.open("blackgram.jpg")
                                            img_dis(img,pred)
                                        elif prediction[0] == 10:
                                            img = Image.open("lentil.jpg")
                                            img_dis(img,pred)
                                        elif prediction[0] == 19:
                                            img = Image.open("pomegranate.jpg")
                                            img_dis(img,pred)
                                        elif prediction[0] == 1:
                                            img = Image.open("banana.jpg")
                                            img_dis(img,pred)
                                        elif prediction[0] == 12:
                                            img = Image.open("mango.jpg")
                                            img_dis(img,pred)
                                        elif prediction[0] == 7:
                                            img = Image.open("grapes.jpg")
                                            img_dis(img,pred)
                                        elif prediction[0] == 21:
                                            img = Image.open("watermelons.jpg")
                                            img_dis(img,pred)
                                        elif prediction[0] == 15:
                                            img = Image.open("muskmelon.jpg")
                                            img_dis(img,pred)
                                        elif prediction[0] == 0:
                                            img = Image.open("apple.jpg")
                                            img_dis(img, pred)
                                        elif prediction[0] == 16:
                                            img = Image.open("orange.jpg")
                                            img_dis(img,pred)
                                        elif prediction[0] == 17:
                                            img = Image.open("papaya.jpg")
                                            img_dis(img,pred)
                                        elif prediction[0] == 4:
                                            img = Image.open("coconut.jpg")
                                            img_dis(img,pred)
                                        elif prediction[0] == 6:
                                            img = Image.open("cotton.jpg")
                                            img_dis(img,pred)
                                        elif prediction[0] == 8:
                                            img = Image.open("jute.png")
                                            img_dis(img,pred)
                                        elif prediction[0] == 5:
                                            img = Image.open("coffee.jpg")
                                            img_dis(img,pred)
                                else:
                                    st.error("Enter the Soil Type")
                        else:
                            st.error("Enter the pH value")
            else:
                st.error("Enter the Phosphorus Value")
        else:
            st.error("Enter the Potassium Value")
    else:
        st.error("Enter the Nitrogen Value")

btn_val = st.button("Predict")
if(btn_val):
    load_data()
