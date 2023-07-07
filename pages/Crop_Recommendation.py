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
def load_data():
    if nitrogen_val and potassium_val and phosphorus_val and temp_val and humi_val and ph_val and rain_val:
        a = list(int(nitrogen_val),int(potassium_val),int(phosphorus_val),float(temp_val),float(humi_val),float(ph_val),float(rain_val))
        loaded = pickle.load(open("crop_predict.pkl","rb"))
        prediction = loaded.predict(np.array([a]))
        d = {20: 'Rice(Arici)', 11: 'Maize(Cholam)', 3: 'Chickpea(Kondakkadalai)', 9: 'Kidneybeans(Rajma Sundal)', 18: 'Pigeonpeas(Thuvaram Parupu)', 13: 'Mothbeans(Nari Payir)', 14: 'Mungbean(Pasi Payir)', 2: 'Blackgram(Ulunthu)',
               10: 'Lentil(Mysore Parupu)', 19: 'Pomegranate(Madhulai)', 1: 'Banana', 12: 'Mango', 7: 'Grapes', 21: 'Watermelon', 15: 'Muskmelon(Mulam Palam)', 0: 'Apple', 16: 'Orange',
               17: 'Papaya', 4: 'Coconut', 6: 'Cotton', 8: 'Jute(Sanal)', 5: 'Coffee'}
        pred = d[prediction[0]]
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
            img = Image.open("jute.jpg")
            img_dis(img,pred)
        elif prediction[0] == 5:
            img = Image.open("coffee.jpg")
            img_dis(img,pred)
btn_val = st.button("Predict")
if(btn_val):
    load_data()
