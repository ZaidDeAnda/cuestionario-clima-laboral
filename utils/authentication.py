import pandas as pd
import streamlit as st
from utils.config import Config
from utils.database import get_mongo_client

def check_password():
    config = Config()
    client = get_mongo_client(config)
    collection = client['ambiente_laboral']['usuarios']
    """Returns `True` if the user had a correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        query = {"password":st.session_state["password"]}
        doc = collection.find_one(query)
        if doc:
            st.session_state["user"] = doc["user"]
            st.session_state["password_correct"] = True
            del st.session_state["password"]
        else:
            st.session_state["password_correct"] = False

    sb1 = st.sidebar.empty()
    sb2 = st.sidebar.empty()
    sb3 = st.sidebar.empty()


    if "password_correct" not in st.session_state:
        # First run, show inputs for username + password.
        sb2.text_input("Contraseña",
                    type="password",
                    on_change=password_entered,
                    key="password")
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        sb2.text_input("Contraseña",
                    type="password",
                    on_change=password_entered,
                    key="password")
        sb3.error("😕 Usuario desconocido o contraseña errónea")
        return False
    else:
        # Password correct.
        sb3.success("Datos ingresados correctamente")
        return True
