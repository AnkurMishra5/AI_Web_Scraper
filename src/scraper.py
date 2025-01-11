import os
import time
import re
import json
from datetime import datetime
from typing import List, Dict, Type

import pandas as pd
from bs4 import BeautifulSoup
from pydantic import BaseModel, Field, create_model
import html2text
import tiktoken

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from openai import OpenAI

load_dotenv()

# Setup the Chrome WebDriver options
def setup_selenium():
    options = Options()
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124"
    )
    service = Service(r"./chromedriver-win64/chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def fetch_html_selenium(url):
    driver = setup_selenium()
    try:
        driver.get(url)
        time.sleep(5)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        html = driver.page_source
        return html
    finally:
        driver.quit()

def clean_html(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    for element in soup.find_all(["header", "footer"]):
        element.decompose()
    return str(soup)

def html_to_markdown_with_readability(html_content):
    cleaned_html = clean_html(html_content)
    markdown_converter = html2text.HTML2Text()
    markdown_converter.ignore_links = False
    markdown_content = markdown_converter.handle(cleaned_html)
    return markdown_content

# Pricing details
pricing = {
    "gpt-4o-mini": {"input": 0.150 / 1_000_000, "output": 0.600 / 1_000_000},
    "gpt-4o-2024-08-06": {"input": 2.5 / 1_000_000, "output": 10 / 1_000_000},
}

model_used = "gpt-4o-mini"

def save_raw_data(raw_data, timestamp, output_folder="output"):
    os.makedirs(output_folder, exist_ok=True)
    raw_output_path = os.path.join(output_folder, f"rawData_{timestamp}.md")
    with open(raw_output_path, "w", encoding="utf-8") as f:
        f.write(raw_data)
    print(f"Raw data saved to {raw_output_path}")
    return raw_output_path

def remove_urls_from_file(file_path):
    url_pattern = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
    base, ext = os.path.splitext(file_path)
    new_file_path = f"{base}_cleaned{ext}"
    with open(file_path, "r", encoding="utf-8") as file:
        markdown_content = file.read()
    cleaned_content = re.sub(url_pattern, "", markdown_content)
    with open(new_file_path, "w", encoding="utf-8") as file:
        file.write(cleaned_content)
    print(f"Cleaned file saved as: {new_file_path}")
    return cleaned_content

# Additional functions for model creation, formatting, and cost calculation
def create_dynamic_listing_model(field_names: List[str]) -> Type[BaseModel]:
    field_definitions = {field: (str, ...) for field in field_names}
    return create_model("DynamicListingModel", **field_definitions)

def create_listings_container_model(listing_model: Type[BaseModel]) -> Type[BaseModel]:
    return create_model("DynamicListingsContainer", listings=(List[listing_model], ...))

def trim_to_token_limit(text, model, max_tokens=200000):
    encoder = tiktoken.encoding_for_model(model)
    tokens = encoder.encode(text)
    if len(tokens) > max_tokens:
        trimmed_text = encoder.decode(tokens[:max_tokens])
        return trimmed_text
    return text

def format_data(data, DynamicListingsContainer):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    system_message = "You are an intelligent text extraction and conversion assistant..."
    user_message = f"Extract the following information from the provided text:\n\n{data}"
    completion = client.beta.chat.completions.create(
        model=model_used,
        messages=[{"role": "system", "content": system_message}, {"role": "user", "content": user_message}],
        response_format=DynamicListingsContainer,
    )
    return completion.choices[0].message.parsed

def save_formatted_data(formatted_data, timestamp, output_folder="output"):
    os.makedirs(output_folder, exist_ok=True)
    json_output_path = os.path.join(output_folder, f"sorted_data_{timestamp}.json")
    with open(json_output_path, "w", encoding="utf-8") as f:
        json.dump(formatted_data, f, indent=4)
    print(f"Formatted data saved to JSON at {json_output_path}")

if __name__ == "__main__":
    url = "https://news.ycombinator.com/"
    fields = ["Title", "Number of Points", "Creator", "Time Posted", "Number of Comments"]
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    raw_html = fetch_html_selenium(url)
    markdown = html_to_markdown_with_readability(raw_html)
    save_raw_data(markdown, timestamp)
