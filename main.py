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

# a1 = pd.DataFrame(df['year'],df['TotalPrice'])
# st.line_chart(a1)
# a1 = pd.DataFrame(df['year'], df['TotalPrice'])
# fig=plt.figure(figsize=(10,8))
# plt.plot(df['year'],df['TotalPrice'])
# st.pyplot(fig)

data = pd.DataFrame({
    'x': np.arange(10),
    'y': np.random.randint(1, 10, 10)
})

# Create a bar chart
st.bar_chart(data('x'))


Wicket ={'Bowlers':['M Shami','A Zampa','S Madushanka','J Bumrah','G Coetzee','S Afridi','M Jensen','R Jadeja','J Hazlewood','M Santner'],
         'Wickets':[24,23,21,20,20,18,17,16,16,16]}
df3 = pd.DataFrame(Wicket)
show_chart = st.sidebar.checkbox('Show Line Chart')
if show_chart:
    st.line_chart(df3.set_index('Bowlers'))



