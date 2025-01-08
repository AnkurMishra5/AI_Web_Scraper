# Unit tests for scraper.py
import pytest
from src.scraper import scrape_website

def test_scrape_website():
    result = scrape_website("https://example.com")
    assert isinstance(result, list)