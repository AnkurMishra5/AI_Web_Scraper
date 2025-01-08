# Project Design Documentation

## 1. Overview
This document provides an overview of the project's design, including its architecture, file structure, and key decisions made during development.

---

## 2. Directory Structure
The project is organized into the following directories:

universal-web-scraper/
│
├── .env                     # Environment file for API keys
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
│
├── src/                     # Source code folder
│   ├── __init__.py          # Marks this as a package
│   ├── scraper.py           # Web scraping logic
│   ├── utils/               # Helper functions
│   │   ├── __init__.py
│   │   ├── selenium_utils.py # Selenium-specific helper functions
│   │   ├── openai_utils.py   # OpenAI integration helper functions
│   │   └── file_utils.py     # File I/O helpers
│   ├── models/              # Pydantic models for dynamic data
│       ├── __init__.py
│       ├── dynamic_model.py # Model generation logic
│
├── app/                     # Application folder
│   ├── streamlit_app.py     # Streamlit application code
│   └── assets/              # Static assets (e.g., images, stylesheets)
│
├── output/                  # Output folder for scraped data
│   ├── raw_data/            # Raw markdown data
│   ├── cleaned_data/        # Cleaned data files
│   ├── formatted_data/      # JSON and Excel outputs
│
├── tests/                   # Test suite for the project
│   ├── test_scraper.py      # Tests for scraper.py
│   ├── test_utils.py        # Tests for utility functions
│
└── docs/                    # Documentation folder (optional)
    ├── design.md            # Design details for the project
    └── api_reference.md     # API reference for the project
