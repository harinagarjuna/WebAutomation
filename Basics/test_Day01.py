import time

import pytest
from selenium import webdriver
import logging
from selenium.webdriver.chrome.options import Options


# def test_chrome_login():
#     driver = webdriver.Chrome()
#     LOGGER = logging.getLogger(__name__)
#     driver.maximize_window()
#     driver.get("https://www.google.com/")
#     LOGGER.info(driver.title)
#     print("This is printed")
#     time.sleep(50)
#     driver.close()
#     time.sleep(2000)

def test_chrom_options():
    options = webdriver.ChromeOptions()
    extension = r"C:\Users\harin\Downloads\IHNKNOKEGKBPMOFMAFNKOADFJKHLOGPH_1_0_2_0.crx"
    chrome_options = Options()
    chrome_options.add_extension(extension)
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get("https://www.google.com/")
    time.sleep(50)
