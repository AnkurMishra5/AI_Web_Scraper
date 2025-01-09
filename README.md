A versatile and user-friendly web scraping application that extracts data from websites and presents it in a structured format. This project is designed with a modular architecture, making it easy to extend, maintain, and deploy. The application includes a Streamlit-based user interface and integrates Selenium for robust scraping capabilities.

Features

Streamlit UI: A simple and interactive user interface for inputting URLs and viewing scraped data.
Selenium Integration: Handles dynamic content and complex websites.
Modular Design: Easily extendable codebase with separate utility and logic files.
Dynamic Data Models: Uses Pydantic for dynamic and structured data modeling.
Output Formats: Supports raw, cleaned, and formatted data outputs (Markdown, JSON, Excel).
Cloud-Ready: Deployable on Streamlit Cloud and other hosting platforms.

Installation Prerequisites

Python 3.9 or above
pip (Python package installer)
Google Chrome and ChromeDriver

Steps

Clone the repository:

git clone https://github.com/your-username/universal-web-scraper.git
cd universal-web-scraper

Install dependencies:

pip install -r requirements.txt
Set up the .env file (if required) with any API keys or environment variables.

Run the application locally:

streamlit run app/streamlit_app.py

