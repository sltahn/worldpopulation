import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Bar Chart", page_icon="📊")

url = "world_population2.csv"
df = pd.read_csv(url)

st.title("World Population Data")

show_dataframe = st.checkbox('Show DataFrame')

if show_dataframe:
    st.write(df)

st.header("World Population for the year 2022")

st.set_option('deprecation.showPyplotGlobalUse', False)
st.bar_chart(df.set_index('Country')['2022 Population'])
st.text("X-axis: Country")
st.text("Y-axis: Population")

st.pyplot()
