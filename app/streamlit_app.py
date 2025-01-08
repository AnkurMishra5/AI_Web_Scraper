# Streamlit app
import streamlit as st
from src.scraper import scrape_website

def main():
    st.title("Universal Web Scraper")

    url = st.text_input("Enter the URL to scrape:")
    if st.button("Scrape"):
        if url:
            data = scrape_website(url)
            st.write("Scraped Data:", data)
        else:
            st.error("Please provide a valid URL.")

if __name__ == "__main__":
    main()