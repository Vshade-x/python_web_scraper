# PYTHON WEB SCRAPER | ANTI-BLOCKING DATA EXTRACTION TOOL

### 🎯 Project Overview

A robust Python script designed to securely and efficiently extract publicly available data (titles, prices, product listings) from target websites and deliver clean, structured reports.

### ✨ Key Features & Anti-Blocking Logic

* **Core Function:** Extracts specific data points from listing pages, demonstrating the ability to handle nested HTML elements.
* **Anti-Blocking Logic:** Uses professional **User-Agent headers** to simulate a real browser request, significantly reducing the risk of being blocked by the target website.
* **Data Cleaning:** Automatically cleans price data (removes currency symbols) and prepares the data for immediate analysis in Excel/CSV.
* **Delivery:** Includes a **1-Click Execution File (.bat)** for easy client use on Windows.

### 🚀 Execution and Usage

**1. Requirements:** Python (3.x) and required libraries: `pip install requests beautifulsoup4 pandas`
**2. Execution:** Simply **double-click the `ejecutar_scraper.bat` file** to run the automation.
**3. Data Output:** The data is saved to a file named **`book_scraping_report.csv`** in the project root folder.
