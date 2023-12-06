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


# Wicket ={'Bowlers':['M Shami','A Zampa','S Madushanka','J Bumrah','G Coetzee','S Afridi','M Jensen','R Jadeja','J Hazlewood','M Santner'],
#          'Wickets':[24,23,21,20,20,18,17,16,16,16]}
# df3 = pd.DataFrame(Wicket)
# show_chart = st.sidebar.checkbox('Show Line Chart')
# if show_chart:
#     st.line_chart(df3.set_index('Bowlers'))

Squad = {'Batsmen':['R sharma','S Gill','Vkohli','S iyyer','KL Rahul','S yadav'],
         'All Rounder':['R Jadeja'],
         'Bowler':['M shami','J Bumrah','M Siraj']}
df= pd.Series(Squad)
if st.sidebar.button('squad'):
    st.write(df)

Score ={'Batsmen':['V Kohli','R Sharma','De Kock','R Ravindra','D Mitchell','D Warner','S Iyer','Kl Rahul','Van der Dussen','M Marsh'],
    'Runs':[765,597,594,578,552,535,530,452,448,441]}
df2 = pd.DataFrame(Score)
show_chart = st.sidebar.checkbox('Show Runs Chart')
if show_chart:
    st.bar_chart(df2.set_index('Batsmen'))


Wicket ={'Bowlers':['M Shami','A Zampa','S Madushanka','J Bumrah','G Coetzee','S Afridi','M Jensen','R Jadeja','J Hazlewood','M Santner'],
         'Wickets':[24,23,21,20,20,18,17,16,16,16]}
df3 = pd.DataFrame(Wicket)
show_chart = st.sidebar.checkbox('Show Wicket Chart')
if show_chart:
    st.line_chart(df3.set_index('Bowlers'))


Wins ={'Teams':['IND','AUS','RSA','NZ','PAK','AFG','ENG','BAN','SN','NED'],
       'Percentage':[90,81,70,50,44,44,33,22,22,22]}
var=pd.DataFrame(Wins)
Per = px.bar(var, x='Teams',y='Percentage')
if st.sidebar.button('Per'):
    st.subheader('best win percentage in ICC WORLD-CUP 2023')
    st.write(Per)



Table ={'TEAMS':['IND','AUS','RSA','NZ','PAK','AFG','ENG','BAN','SN','NED'],
        'POINTS':[18,14,14,10,8,8,6,4,4,4]}
df1= pd.DataFrame(Table)
points =px.bar(df1, x='TEAMS',y='POINTS')
if st.sidebar.button('points'):
    st.subheader('teams point table')
    st.bar_chart(df1.set_index('TEAMS'))









