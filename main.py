from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from webdriver_manager.chrome import ChromeDriverManager


url = input("URL: ")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))



driver.get(url)

# Wait until price is visible
WebDriverWait(driver, 60).until(ec.visibility_of_element_located((By.XPATH, "//div[@class='pdp-product-price']/span")))

priceEl = driver.find_element(By.XPATH, "//div[@class='pdp-product-price']/span")
price = priceEl.text
nameEl = driver.find_element(By.XPATH, "//span[@class='pdp-mod-product-badge-title']")
name = nameEl.text


print(f"Name: {name}\nPrice: {price}")