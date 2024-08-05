import pickle
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor

st.image(r"ino_img.jpg",width=150)

st.title("DIAMOND PRICE PREDICTION")

model = pickle.load(open(r"C:\Users\jathi\machine learning folder\dt.pkl","rb"))

Carat = st.slider("carat",max_value=0.2,min_value=5.01)

text = {1:"IDEAL",2:"PREMIUM",3:"GOOD",4:"VERY GOOD",5:"FAIR"}
cut = st.selectbox("Select the cut value", text.keys())
st.markdown(f"<h3 style='font-size:20px;'>Cut type: {text[cut]}</h3>", unsafe_allow_html=True)

text1 = {1:"E - Colorless",2:"I - Near Colorless",3:"J - Faint Yellow",4:"H - Near colorless",5:"F - Coloress",6:"G - ",7:"D - colorless"}
color = st.selectbox("Select the color value", text1.keys())
st.markdown(f"<h3 style='font-size:20px;'>Color type: {text1[color]}</h3>", unsafe_allow_html=True)

text2 = {1:"SI2 - Slightly Included",2:"SI1 - Slightly Included",3:"VS1 - Very Slightly Included",4:"VS2 - Very Slightly Included",5:"VVS2 - Very vrey Slightly Included",6:"VVS1 - Very Vrey Slightly Included",7:"I1 - Included",8:"IF - Internally Flawflass"}
clarity = st.selectbox("Select the clarity value", text2.keys())
st.markdown(f"<h3 style='font-size:20px;'>Color type: {text2[clarity]}</h3>", unsafe_allow_html=True)

Depth = st.slider("Depth",max_value=79.0,min_value=43.0)

Table = st.slider("Table",max_value=95.0,min_value=43.0)

Length =st.slider("Length",min_value=0.0 ,max_value=10.74)

Weidth = st.slider("Weidth",min_value=0.0,max_value=58.9)

Height = st.slider("Height",min_value=0.0,max_value=31.8)

model1 = model.predict([[Carat,cut,color,clarity,Depth,Table,Length,Weidth,Height]])[0]

if st.button("Submit"):
    st.write("The price of the Diamond",model1)
