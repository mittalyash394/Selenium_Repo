import time
from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager

class DemoFindElementById():
    def locate_by_id_demo(self):
        driver = webdriver.Chrome()
        driver.get("https://www.amazon.in/")
        driver.find_element("id", "twotabsearchtextbox").send_keys('iphone')
        driver.find_element("id", "nav-search-submit-button").click()
        # 1st element
        eles = driver.find_element("xpath", '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/span/div/div/div/div[1]/div/div[2]/div/span/a/div/img')
        eles.click()
        
        time.sleep(5)
        

find_by_id = DemoFindElementById()
find_by_id.locate_by_id_demo()