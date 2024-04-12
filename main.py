import base64
import requests
import streamlit as st
from streamlit_option_menu import option_menu


import about, compare, predict, recommend

st.set_page_config(
    page_title="Recommend Cars",
    page_icon="🚘",
    # layout="wide"
)

class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })

    def run():
        app = option_menu(
            menu_title = "Main Menu", 
            options = ["Recommend", "Predict", "Compare", "About"],
            icons = ["car-front", "calculator", "search", "info-circle-fill"],
            default_index = 1,
            orientation = "horizontal",
            styles={
                            "container": {"padding": "5!important","background-color":'black'},
                "icon": {"color": "white", "font-size": "23px"}, 
                "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
                "nav-link-selected": {"background-color": "#02ab21"},}
            )

        if app == "Recommend":
            recommend.app()
        if app == "Predict":
            predict.app()
        if app == "Compare":
            compare.app()
        if app == "About":
            about.app()

    run()