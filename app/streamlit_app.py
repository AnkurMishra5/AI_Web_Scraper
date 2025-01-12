import streamlit as st
from streamlit_tags import st_tags_sidebar
import pandas as pd
import json
from datetime import datetime
#from scraper import fetch_html_selenium, save_raw_data, format_data, save_formatted_data

st.set_page_config(page_title="Universal Web Scraper")
st.title("Universal Web Scraper")

# Sidebar components
st.sidebar.title("Web Scraper Settings")
model_selection = st.sidebar.selectbox("Select Model", options=["gpt-40-mini", "gpt-40-2024-08-06"], index=0)
url_input = st.sidebar.text_input("Enter URL")

tags = st_tags_sidebar(
    label="Enter Fields to Extract:",
    text="Press enter to add a tag",
    value=[],
    key="tags_input",
)

fields = tags

if st.sidebar.button("Scrape"):
    st.spinner("Scraping in progress...")
    # Call scrape functions
