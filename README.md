# Universal Web Scraper

A versatile and user-friendly web scraping application that extracts data from websites and presents it in a structured format. This project is designed with a modular architecture, making it easy to extend, maintain, and deploy. The application includes a Streamlit-based user interface and integrates Selenium for robust scraping capabilities.

## Features

- **Streamlit UI**: A simple and interactive user interface for inputting URLs and viewing scraped data.
- **Selenium Integration**: Handles dynamic content and complex websites.
- **Modular Design**: Easily extendable codebase with separate utility and logic files.
- **Dynamic Data Models**: Uses Pydantic for dynamic and structured data modeling.
- **Output Formats**: Supports raw, cleaned, and formatted data outputs (Markdown, JSON, Excel).
- **Cloud-Ready**: Deployable on Streamlit Cloud and other hosting platforms.

## Setup

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/universal-web-scraper.git
    cd universal-web-scraper
    ```

2. **Create and activate a virtual environment**:
    ```sh
    python -m venv venv
    .\venv\Scripts\activate  # On Windows
    source venv/bin/activate  # On macOS/Linux
    ```

3. **Install the required packages**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Download the Chrome WebDriver**:
    - Download the appropriate version of ChromeDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads).
    - Place the `chromedriver.exe` file in the `chromedriver-win64` directory.

5. **Set up environment variables**:
    - Create a [.env](http://_vscodecontentref_/2) file in the root directory and add your OpenAI API key:
    ```env
    OPENAI_API_KEY=your_openai_api_key
    ```

## Usage

1. **Run the Streamlit app**:
    ```sh
    streamlit run streamlit_app.py
    ```

2. **Interact with the UI**:
    - Enter the URL you want to scrape.
    - Add the fields you want to extract.
    - Click the "Scrape" button to start the scraping process.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.