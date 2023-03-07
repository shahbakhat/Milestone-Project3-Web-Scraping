import streamlit as st # for visualization and interaction.
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv).
import requests # for HTML to be displayed and read in text.
from bs4 import BeautifulSoup # for sxrapping Web pages.
# Created a variable below for the comment because it was rendered and shown on streamlit.
my_comment = """STEPS WE ARE TAKING:
1. Performing a GET request to thr URL.
2.Parsing the HTML HTML.
3.Locating the desired Elements to scrape.
4.Extracting the data from the HTML.
5.Exporting thre Data to a CSV file.
"""

#This st.selectbox(with desired options) creates a selection box with a list of options on streamlit server. """
tags = st.selectbox('Choose a topic', ['love','humor','life','books'])
#Putting the variable {tags} after /tag/ will add the selected option to url such as https://quotes.toscrape.com/tag/humor/
url = f"https://quotes.toscrape.com/tag/{tags}/"
#Sending request to url ot get a response.
response = requests.get(url)
# st.write(response) checked the response status and it was successful type 200.
content = BeautifulSoup(response.content,'html.parser')
# st.code(content)
quotes  = content.find_all('div', class_='quote')
quote_file = []
for quote in quotes:
    text = quote.find('span', class_='text').text
    author = quote.find('small', class_='author').text
    link = quote.find('a')
    st.success(text)
    # st.write(author)
    # Streamlit does allow HTML , so we use unsafe_allow_html=Ture
    #st.markdown displays string formatted as Markdown.
    st.markdown(f"<a href='https://quotes.toscrape.com{link['href']}'>{author}</a>",unsafe_allow_html=True)
    quote_file.append([text,author,link])
    # st.code(link['href']) This is the link to quote 'a' tags but only with
    # href excluding the <a> tag. but we need to add the link to the url.
    st.code(f"https://quotes.toscrape.com{link['href']}")
