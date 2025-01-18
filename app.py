import streamlit as st
import seaborn as sns
import numpy as np

taxis = sns.load_dataset("taxis")
images = {"Brooklyn": "https://voyageforum.info/images/hd/posts/openmedium/1570541343-3kyuiYKirJKB97b.jpeg", 
          "Queens": "https://th.bing.com/th/id/R.abea870b3c0a1bbc5f08c57e9c69c664?rik=54HguWX%2f5IEiUA&pid=ImgRaw&r=0",
          "Bronx": "https://plus.unsplash.com/premium_photo-1682116752742-7bb2b3698486?q=80&w=2065&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", 
          "Manhattan": "https://plus.unsplash.com/premium_photo-1680284197408-0f83f185818b?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
          np.nan: "https://th.bing.com/th/id/OIP.x7DV_yk6r4eEpB1EZ33_xwHaHa?rs=1&pid=ImgDetMain"}

st.title("Bienvenue sur le site web HEY HO, TAXIS ! 🚕")

pickup_borough = st.selectbox("Indiquez votre arrondissement de récupération", 
                              options=taxis['pickup_borough'].unique())

st.write("Tu as choisis: ", pickup_borough)
st.image(images[pickup_borough])
