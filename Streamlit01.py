import streamlit as st
import pandas as pd

st.title("การทดสอบสร้างเว็บด้วยPython")
st.image("data.jpeg")
st.header("การนำเสนอข้อมูลกราฟด้วย Python")

col1, col2, col3 = st.columns(3)

with col1: 
    st.header("Versicolor")
    st.image("https://en.m.wikipedia.org/wiki/File:Iris_versicolor_3.jpg")
with col2:
    st.header("Verginica")
    st.image("https://commons.wikimedia.org/wiki/Category:Silene_virginica")
with col3:
    st.header("Setosa")
    st.image("https://en.wikipedia.org/wiki/Iris_setosa")