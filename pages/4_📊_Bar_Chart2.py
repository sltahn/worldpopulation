import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Bar Chart2", page_icon="📊")

url = 'world_population.csv'
df = pd.read_csv(url)

st.title("World Population Data")

df_sorted = df.sort_values(by='2015 Population', ascending=False)

top_20 = df_sorted.head(20)

top_20.set_index('Country', inplace=True)

show_dataframe = st.checkbox('Show DataFrame')

if show_dataframe:
    st.write(top_20)

st.bar_chart(top_20['2015 Population'])
