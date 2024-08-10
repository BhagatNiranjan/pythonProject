from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import  service
from selenium.webdriver.common.by import By
from webdriver.chrome import ChromeDriverManager
url='https://www.python.org/'
chrome_option=Options()
chrome_option.add_experimental_option("detach",True)
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
driver.get(url)
driver.maximize_window()



