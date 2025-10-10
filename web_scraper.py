import requests
from bs4 import BeautifulSoup
import pandas as pd

# ==========================================================
# 1. CONFIGURATION AND HEADERS
# ==========================================================

# Headers to simulate a real browser request (Anti-Blocking Logic)
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# Base URL for the target website
BASE_URL = "http://books.toscrape.com/"
book_listings = [] 

# ==========================================================
# 2. SCRAPING FUNCTION
# ==========================================================
def scrape_data():
    print(f"Starting web scraping process for: {BASE_URL}")
    
    # Make the HTTP request using the defined headers
    response = requests.get(BASE_URL, headers=HEADERS)
    
    # Check if the request was successful (HTTP status code 200)
    if response.status_code == 200:
        print("Connection successful. Analyzing HTML...")
        
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all product containers
        products = soup.find_all('article', class_='product_pod')
        
        # Loop through each product to extract data
        for product in products:
            try:
                # Extract the Title
                title = product.h3.a['title']
            except AttributeError:
                title = "N/A"
            
            # Extract and Clean the Price
            price_raw = product.find('p', class_='price_color').text.strip()
            # Remove currency symbol (£) and convert to float
            cleaned_price = float(price_raw.replace('£', ''))
            
            # Append data to the list
            book_listings.append({
                'Book Title': title,
                'Price (GBP)': cleaned_price
            })
            
        print(f"✅ Extraction completed. Found {len(book_listings)} books.")
        export_to_csv(book_listings)
        
    else:
        print(f"❌ Connection Error. Status code: {response.status_code}")

# ==========================================================
# 3. EXPORT FUNCTION
# ==========================================================
def export_to_csv(data):
    # Convert list of dictionaries to a Pandas DataFrame
    df = pd.DataFrame(data)
    
    # Define the final column order for a clean report structure
    final_columns = ['Book Title', 'Price (GBP)'] 
    df_final = df[final_columns]
    
    output_filename = 'book_scraping_report.csv'
    
    # Export to CSV, forcing semicolon delimiter (sep=';') for better Excel compatibility
    df_final.to_csv(output_filename, index=False, encoding='utf-8', sep=';', decimal='.')
    
    print(f"✅ Web Scraping Report saved as: {output_filename}")

# Execute the main function
if __name__ == "__main__":
    scrape_data()