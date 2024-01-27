from selenium import webdriver
from selenium.webdriver.common.by import By

# keep Chrome open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--use_subprocess")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://uzum.uz/uz/product/televizor-samsung-crystal-820195")

price_dollar = driver.find_element(By.CLASS_NAME, value="currency old-price")
print(price_dollar.text)

driver.quit()