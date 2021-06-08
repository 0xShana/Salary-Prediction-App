from re import I
import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page


kk=st.sidebar.selectbox("Predict OR Explore",("Predict","Explore",))



if(kk=="Predict"):
    show_predict_page()
elif (kk =="Explore"):
    show_explore_page()