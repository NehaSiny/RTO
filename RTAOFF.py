import streamlit as st
import pandas as pd
import seaborn as sns

st.balloons()
#https://kerala.data.gov.in/catalog/motor-vehicles-department-kerala#web_catalog_tabs_block_10 
df = pd.read_csv('/Users/nirmal/Desktop/RTO.csv')
st.title("Kerala Road Transport Authority ")
option1 = st.selectbox('Select District ',df['Office'].unique())
kk=df[df.Office == option1].sort_values('OfficeType')
st.write(kk)

pp=kk.groupby(['OfficeType']).size()
st.subheader('Zone Information' )
st.bar_chart(pp)
