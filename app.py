import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import random
import plotly.express as px

from PIL import Image
image_choco = Image.open('Choco.jpg')
st.image(image_choco, width=200)

st.title("Chocolate Ratings")

st.sidebar.header("Dashboard")
st.sidebar.markdown("---")

df = pd.read_csv("chocolate.csv")
st.markdown("## Visualization")

list_variables = df.columns
symbols = st.multiselect("Select two variables", list_variables, ["company_location", "rating"])

rating_min, rating_max = st.sidebar.slider('Select rating Range', min_value=int(df['rating'].min()), max_value=int(df['rating'].max()), value=(int(df['rating'].min()), int(df['rating'].max())))

# Filtering the dataframe based on the slider values
filtered_df = df[(df['rating'] >= rating_min) & (df['rating'] <= rating_max)]

tab1, tab2 = st.tabs(["Line Chart", "Bar Chart"])

tab1.subheader("Line Chart")
tab1.line_chart(data=df, x=symbols[0], y=symbols[1], width=0, height=0, use_container_width=True)

tab2.subheader("Bar Chart")
tab2.bar_chart(data=df, x=symbols[0], y=symbols[1], use_container_width=True)



## Description of Dataset

num = st.number_input('No of Rows',5,10)
st.dataframe(df.head(num))

### Description of the dataset

st.dataframe(df.describe())

### Missing value

dfnull = df.isnull().sum()/len(df)*100
totalmiss = dfnull.sum().round(2)
st.write("Percentage of missing value in my dataset",totalmiss)


if st.button("Show Describe Code"):
        code = '''df.describe()'''
        st.code(code, language='python')

if st.button("Generate Report"):
  import streamlit as st
  import streamlit.components.v1 as components

  # Title for your app
  st.title('Sweetviz Report for chocolate ratings in Streamlit')

  # Display the Sweetviz report
  report_path = 'report.html'
  HtmlFile = open(report_path, 'r', encoding='utf-8')
  source_code = HtmlFile.read()
  components.html(source_code, height=1000,width=1000)

