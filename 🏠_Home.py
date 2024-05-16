import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Home",
    page_icon="🏠",
)

st.write("# World Population 🌎")

show_dataframe = st.checkbox('Show DataFrame')

if show_dataframe:
    url = "world_population.csv"
    df = pd.read_csv(url)
    st.write(df)

st.markdown(
    """
    This multi-page app has charts of the world population. Click on the page link to go to that page to see the charts.
"""
)

url = "world_population.csv"
df = pd.read_csv(url)

st.set_option('deprecation.showPyplotGlobalUse', False)
st.line_chart(df.set_index('Country')['2020 Population'])
st.text("Population for the year 2020")
st.text("X-axis: Country")
st.text("Y-axis: Population")

st.pyplot()
