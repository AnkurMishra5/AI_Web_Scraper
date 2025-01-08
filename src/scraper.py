# Main web scraping logic
from selenium import webdriver
from selenium.webdriver.common.by import By
from src.utils.selenium_utils import setup_driver

def scrape_website(url):
    """Scrapes data from a given URL."""
    driver = setup_driver()
    driver.get(url)
    data = driver.find_elements(By.TAG_NAME, "p")
    result = [item.text for item in data]
    driver.quit()
    return result

if __name__ == "__main__":
    url = "https://example.com"
    print(scrape_website(url))