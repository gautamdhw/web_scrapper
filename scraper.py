# scraper.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
import time

def scrape_truemeds(query):
    # Chrome options
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("user-agent=Mozilla/5.0")

    driver = webdriver.Chrome(options=options)
    url = f"https://www.truemeds.in/search/{query}"
    driver.get(url)
    time.sleep(5)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()

    # Extract details
    medicine_divs = soup.find_all("div", class_="sc-a39eeb4f-12 daYLth")
    manufacturer_spans = soup.find_all("span", class_="sc-a39eeb4f-14 faASZT")
    qty_spans = soup.find_all("span", class_="sc-a39eeb4f-16 jdUNAq")
    price_spans = soup.find_all("span", class_="sc-a39eeb4f-17 iwZSqt")
    img_containers = soup.find_all("div", class_="sc-a39eeb4f-2 gzQHwG")
    image_links = [div.find("img")["src"] for div in img_containers if div.find("img") and div.find("img").has_attr("src")]

    # Texts
    medicine_names = [div.get_text(strip=True) for div in medicine_divs]
    manufacturer_names = [span.get_text(strip=True) for span in manufacturer_spans]
    quantities = [span.get_text(strip=True) for span in qty_spans]
    prices = [span.get_text(strip=True) for span in price_spans]

    min_len = min(len(medicine_names), len(manufacturer_names), len(quantities), len(prices), len(image_links))
    df = pd.DataFrame({
        "Medicine Name": medicine_names[:min_len],
        "Manufacturer": manufacturer_names[:min_len],
        "Quantity": quantities[:min_len],
        "Price": prices[:min_len],
        "Image Link": image_links[:min_len]
    })
    return df
