import pandas as pd
import streamlit as st
import matplotlib as plt
import seaborn as sns
import colaborativeFiltering



st.title("Colaborative Filtering Influencers/Pymes")

st.subheader("Evalúa al influencer con el que trabajaste la primera vez")
influencer = st.selectbox("Influencer: ",colaborativeFiltering.df.columns.tolist(), key=0)
score = st.slider('Valoración del 1 al 5', min_value=1, max_value=5, step=1, key = 0)

st.text("-----------------------------------------------------------------------------------------------------------")

st.subheader("Evalúa al influencer con el que trabajaste la segunda vez")
influencer2 = st.selectbox("Influencer: ",colaborativeFiltering.df.columns.tolist(), key=1)
score2 = st.slider('Valoración del 1 al 5', min_value=1, max_value=5, step=1,key = 1)

st.text("-----------------------------------------------------------------------------------------------------------")
st.subheader("Evalúa al influencer con el que trabajaste la tercera vez")
influencer3 = st.selectbox("Influencer: ",colaborativeFiltering.df.columns.tolist(), key = 2)
score3 = st.slider('Valoración del 1 al 5', min_value=1, max_value=5, step=1, key = 2)

st.text("Tus Recomendaciones (TOP 10)")

store_likes = [tuple([influencer,score]),tuple([influencer2,score2]),tuple([influencer3,score3])]

st.table(colaborativeFiltering.recommend(store_likes))
