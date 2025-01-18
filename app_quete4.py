import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

car = pd.read_csv("https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv")

st.title("WCS - Challenge Quête Streamlit")
st.header("🚙 Quelques graphs sur des voitures 🚗")

with st.sidebar:
    regions = st.multiselect("Filtrez par région", car['continent'].unique(), car['continent'].unique())

st.subheader("Données :")
data = car.loc[car['continent'].isin(regions)]
st.dataframe(data)

st.subheader("Matrice de corrélation entre les features numériques")
viz_correlation = sns.heatmap(data.select_dtypes('number').corr(), vmin=-1, vmax=1, center=0)
st.pyplot(viz_correlation.figure)

st.subheader("Visualisez la relation entre 2 variables quantitatives")
x = st.selectbox("Choisissez la colonne X", data.select_dtypes('number').columns)
y = st.selectbox("Choisissez la colonne Y", data.select_dtypes('number').columns)

fig2, ax2 = plt.subplots()
ax2 = sns.scatterplot(data, x=x, y=y)
st.pyplot(fig2)

st.subheader("Analysez la distribution d'une variable")
feature = st.selectbox("Choisissez une variable à analyser", data.columns)

fig3, ax3 = plt.subplots()
ax3 = sns.histplot(data, x=feature)
plt.title(f"Distribution de la variable {feature}")
st.pyplot(fig3)
