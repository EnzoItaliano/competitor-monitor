from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

def get_amazon_data(product_url):
    """
    Scrapes product information from an Amazon product page.

    Args:
        product_url: The URL of the Amazon product page.

    Returns:
        A dictionary containing the product title, price, and a list of reviews.
        If an error occurs, it returns a dictionary with an 'error' key.
    """
    # Configure Chrome options
    options = Options()
    options.add_argument("--headless")  # Run Chrome in headless mode (no UI)
    options.add_argument("--no-sandbox") # Necessary to run in a restricted container like Streamlit's
    options.add_argument("--disable-dev-shm-usage") # Necessary to run in a restricted container like Streamlit's
    options.add_argument("--disable-gpu")
    # Used to set a specific user agent
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36")

    # Initialize the Chrome driver using webdriver_manager to handle automatic driver installation
    driver = webdriver.Chrome(options=options)
    
    try:
        # Navigate to the given product URL
        driver.get(product_url)
        # Wait for 3 seconds to allow the page to fully load
        time.sleep(3)
        
        # Extract the product title
        title = driver.find_element(By.ID, "productTitle").text.strip()
        
        # Extract the product price
        price_whole = driver.find_element(By.CLASS_NAME, "a-price-whole").text
        price_fraction = driver.find_element(By.CLASS_NAME, "a-price-fraction").text
        full_price = f"${price_whole}.{price_fraction}"
        
        # Extract the top 3 customer reviews
        review_elements = driver.find_elements(By.CLASS_NAME, "review-text-content")
        reviews = [r.text.strip() for r in review_elements[:3]]
        
        # Return the scraped data as a dictionary
        return {"title": title, "price": full_price, "reviews": reviews}
    
    except Exception as e:
        # If any error occurs during the scraping process, return an error message
        return {"error": str(e)}
    finally:
        # Ensure the browser is closed regardless of whether an error occurred or not
        driver.quit()