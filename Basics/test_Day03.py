import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

def test_ebay_search_result():
    driver = webdriver.Chrome()
    #driver.implicitly_wait(15)
    driver.get("https://www.ebay.com/b/Computers-Tablets-Network-Hardware/58058/bn_1865247")
    pclink = driver.find_element(By.XPATH,"//div[@class='b-visualnav__title']")
    pclink.click()
    ramlink = driver.find_element(By.XPATH,"//a[@href='https://www.ebay.com/b/16-GB-RAM-PC-Laptops-Netbooks/177/bn_7114664539']")
    ramlink.click()
    WebDriverWait(driver,15).until(expected_conditions.presence_of_element_located((By.
CSS_SELECTOR, "h2[class = 'srp-controls__count-heading']")))
    itemdescription = driver.find_elements(By.XPATH,"//h3[@class='s-item__title']")
    itemprice = driver.find_elements(By.XPATH, "//span[@class='s-item__price']")
    for r in range(48):
        print(itemdescription[r].text)
        print(itemprice[r].text)

    #time.sleep(10)
    driver.quit()



