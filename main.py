import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


#data mininig

df = pd.read_csv('data.csv')

st.title('Data Analysis')
if st.sidebar.button("show data"):
  st.write(df)
  
if st.sidebar.button("title"):
  st.title("hello how are you")



