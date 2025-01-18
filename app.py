import streamlit as st
import pandas as pd
from ast import literal_eval
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu


users_data = pd.read_csv("user_data.csv", 
                         index_col="usernames", 
                         dtype={"password": str}, 
                         converters={'pet_pixs': literal_eval})

credentials = {"usernames": users_data.to_dict(orient="index")}

authenticator = Authenticate(
    credentials, # Les données des comptes
    "cookie_name", # Le nom du cookie, un str quelconque
    "cookie_key", # La clé du cookie, un str quelconque
    30, # Le nombre de jours avant que le cookie expire 
)

authenticator.login()

def accueil():
    with st.sidebar:
        st.write("Bienvenue", st.session_state["name"])
        user_data = credentials['usernames'][st.session_state["username"]]
            
        selection = option_menu(menu_title = None, 
                                options=["🤩 Accueil", "📸 Les photos de mon "+ user_data["pet_name"]], 
                                default_index=0)
      
    if selection == "🤩 Accueil":
        st.title("Bienvenue sur ma page")
        st.image(user_data['profile_pic'])
    elif selection == "📸 Les photos de mon " + user_data["pet_name"]:
        st.title("Bienvenue dans l'album de mon " + user_data["pet_name"] + user_data["pet_icone"])
    
        for index, col in enumerate(st.columns(3)):
            col.image(user_data["pet_pixs"][index])


if st.session_state["authentication_status"]:
        accueil()
        authenticator.logout("Déconnexion", location="sidebar")
    
elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning('Les champs username et mot de passe doivent être remplie')
