import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup

#This st.selectbox(with desired options) creates a selection box with a list of options on streamlit server. """
tags = st.selectbox('Choose a topic', ['love','humor','life','books'])
#Putting the variable {tags} after /tag/ will add the selected option to url such as https://quotes.toscrape.com/tag/humor/
url = f"https://quotes.toscrape.com/tag/{tags}/"
