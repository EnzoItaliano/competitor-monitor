# 📈 AI-Powered Competitor & Sentiment Monitor

A professional-grade backend solution that automates market research by combining **Web Automation**, **Large Language Models (LLMs)**, and **Interactive Data Visualization**.

---

## 🎯 The Business Value
Manual competitor tracking is slow and error-prone. This tool allows businesses to:
* **Monitor Pricing:** Instantly see current market rates for any Amazon product.
* **Sentiment Analysis:** Use AI to distill hundreds of customer reviews into a single "Market Mood" summary.
* **Data-Driven Decisions:** Save hours of manual reading by getting summarized pros/cons of competitor products.

## 🛠️ Tech Stack
* **Python 3.10+**
* **Selenium & Webdriver Manager:** For robust, headless web scraping.
* **OpenAI API:** For intelligent NLP and sentiment summarization.
* **Streamlit:** For a clean, responsive executive dashboard.
* **pip-tools:** For sophisticated dependency pinning and environment stability.

## 📦 Installation & Setup

This project uses `pip-tools` to ensure that every developer and server runs the exact same environment.

1. **Clone the repository:**
   ```bash
   git clone https://github.com/EnzoItaliano/competitor-monitor.git
   cd competitor-monitor

2. **Sync the dependencies:** This project uses `pip-sync` to ensure your virtual environment matches the locked requirements.txt.

    ```bash
    pip install pip-tools
    pip-sync requirements.txt
    ```

    _Note: To add new packages, edit requirements.in and run `pip-compile`._

3. **Environment Variables:** Create a .env file in the root directory and add your API key:

    ```Snippet de código
    OPENAI_API_KEY=your_actual_key_here

4. **Run the Dashboard:**

    ```Bash
    streamlit run app.py

## 🏗️ **Architecture Design**

The project is built with modularity in mind:
- `scraper.py`: Handles browser initialization, user-agent rotation, and DOM extraction.

- `analyzer.py`: Manages the connection to OpenAI and prompt engineering.

- `app.py`: The entry point that integrates the backend logic with the Streamlit UI.

## 🚀 **Professional Features**
- **Headless Browsing:** Optimized for deployment on Linux servers.

- **Anti-Detection:** Uses custom headers and random delays to mimic human behavior.

- **Type Hinting:** Written with clean, typed Python for better maintainability.

- **Locked Dependencies:** High security and reliability via pip-compile.

---
_Developed by [Enzo Italiano](https://github.com/EnzoItaliano) — Specialized in Backend Automation & Data Engineering._
