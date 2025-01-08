from selenium import webdriver

def setup_driver():
    """Initializes and returns a Selenium WebDriver instance."""
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    return webdriver.Chrome(options=options)