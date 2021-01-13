import streamlit as st
import pandas as pd
import seaborn as sns

st.balloons()
#https://kerala.data.gov.in/catalog/motor-vehicles-department-kerala#web_catalog_tabs_block_10 
#https://kerala.data.gov.in/resources/offices-under-motor-vehicles-department-kerala-28092020/download
df = pd.read_csv('https://kerala.data.gov.in/resources/offices-under-motor-vehicles-department-kerala-28092020/download')

st.title("Kerala Road Transport Authority ")
option1 = st.selectbox('Select District ',df['Office'].unique())
kk=df[df.Office == option1].sort_values('OfficeType')
st.write(kk)

pp=kk.groupby(['OfficeType']).size()
st.subheader('Zone Information' )
st.bar_chart(pp)
