import pandas as pd

import streamlit as st
import main
import preprocessing
import EDA
import modeling

st.title("Beijing Multi-Site Air Quality data analysis ")
combined_dataFrame = None
csv_files = st.file_uploader("Please Upload at least 6 of the CSV files to start the analysis", accept_multiple_files=True, type='csv')
if csv_files is not None:
  if len(csv_files) >= 6:
    dataframes = []
    for file in csv_files:
      df = pd.read_csv(file)
      dataframes.append(df)
    combined_dataFrame=pd.concat(dataframes,ignore_index=True)

    st.sidebar.title("AQI application")
    page = st.sidebar.radio("Select a page please:", ["Data Overview", "Exploratory Data Analysis (Part1)","Exploratory Data Analysis (Part2)" , "Modelling and Prediction"])
    if page == "Data Overview":
      main.Data_Overview(combined_dataFrame)
    elif page=="Exploratory Data Analysis (Part1)":
      preprocessing.EDA_Part1(combined_dataFrame)
    elif page=="Exploratory Data Analysis (Part2)":
      EDA.EDA_Part2(combined_dataFrame)
    elif page=="Modelling and Prediction":
      modeling.modeling_prediction(combined_dataFrame)
    else:
        st.warning("Please upload at least 6 CSV files first.")
  else:
    st.warning("Please upload at least 6 CSV files to start the analysis")

