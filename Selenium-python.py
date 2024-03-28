from selenium import webdriver
# # from selenium.webdriver.common.keys import Keys
# import time

# driver = webdriver.Edge()
# # Navigate to the Amazon homepage
# driver.get("https://www.amazon.com/")

# time.sleep(20)

# # E:\Drivers\edgedriver_win64\msedgedriver.exe

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Set the path to chromedriver


driver = webdriver.Edge()
# Navigate to the Amazon homepage
driver.get("https://www.amazon.com/")


# Search for a specific product
# search_box = driver.find_element("twotabsearchtextbox").search_box.send_keys("iPhone 14 256GB").search_box.send_keys(Keys.RETURN)
search_box = driver.find_element_by_name("q")
search_box.send_keys("iPhone 14 256GB")
search_box.send_keys(Keys.RETURN)

time.sleep(20)  # Adjust the sleep time as needed