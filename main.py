import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


#data mininig

df = pd.read_csv('data.csv')


st.title('Data Analysis')
if st.sidebar.button("show data"):
  st.write(df)

if st.sidebar.button('load describtion'):
  st.write(df.describe())

a1 = pd.DataFrame(df['year'],df['TotalPrice'])
st.line_chart(a1)

a1 = pd.DataFrame(df['year'], df['TotalPrice'])

fig=plt.figure(figsize=(10,8))
plt.plot(df['year'],df['TotalPrice'])
st.pyplot(fig)



