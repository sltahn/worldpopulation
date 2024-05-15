import pandas as pd
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.palettes import Spectral16
import streamlit as st

st.set_page_config(page_title="Line Chart", page_icon="📈")

data_url = "world_population.csv"
df = pd.read_csv(data_url)

st.title("World Population Data")

show_dataframe = st.checkbox('Show DataFrame')

if show_dataframe:
    st.write(df)

p = figure(width=800, height=600, title="Population vs Area", x_axis_type="log", y_axis_type="log")
p.xaxis.axis_label = "Population"
p.yaxis.axis_label = "Area (km²)"

source = ColumnDataSource(df)

p.circle(x="2022 Population", y="Area (km²)", size=10, color=Spectral6[0], source=source)

hover = HoverTool()
hover.tooltips = [("Country", "@Country"), ("Population", "@{2022 Population}"), ("Area", "@{Area (km²)}")]
p.add_tools(hover)

st.bokeh_chart(p)
