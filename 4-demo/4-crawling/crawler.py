from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class craigslist_crawler(object):
    def __init__(self, query):
        self.query = query
        self.url =f'https://vietnam.craigslist.org/d/for-sale/search/sss?query={query}&sort=rel&lang=en&cc=us'
        self.driver = webdriver.Chrome("C:\Drivers\chromedriver.exe")
        self.delay = 5
    
    def load_page(self):
        driver = self.driver
        driver.get(self.url)
        all_data = driver.find_elements_by_class_name("result-row")
        for data in all_data:
            print(data.text)
    
    def close_driver(self):
        self.driver.close()
        print('Goodbye')

query = "food"
crawler = craigslist_crawler(query)
crawler.load_page()
crawler.close_driver()