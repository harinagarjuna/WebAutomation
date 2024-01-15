import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_kapplogin():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    driver.maximize_window()
    mappbtn = driver.find_element(By.ID,value="btn-make-appointment")
    mappbtn.click()
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login", "Incorrect URL"

    username = driver.find_element(By.ID,value="txt-username")
    password = driver.find_element(By.CSS_SELECTOR,"#col-sm-8.password")
    submit_btn = driver.find_element(By.ID,"btn-login")
    username.send_keys("John Doe")
    password.send_keys("ThisIsNotAPassword")
    submit_btn.click()
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment", "Wrong Page"


    time.sleep(5)
    driver.quit()
















































































