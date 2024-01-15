import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()
driver.get("https://app.vwo.com/#/login")
driver.maximize_window()
def test_appvwologin():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    driver.maximize_window()
    # mappbtn = driver.find_element(By.ID,value="btn-make-appointment")
    # mappbtn.click()
    # assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login", "Incorrect URL"

    username = driver.find_element(By.ID,value="login-username")
    password = driver.find_element(By.ID,"login-password")
    submit_btn = driver.find_element(By.ID,"js-login-btn")
    username.send_keys("John Doe")
    password.send_keys("ThisIsNotAPassword")
    submit_btn.click()
    message = driver.find_element(By.ID, value = "js-notification-box-msg")
    assert message != "Valid Credentials"
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment", "Wrong credentials"

def test_loginsuccess():
    username = driver.find_element(By.ID, value="login-username")
    password = driver.find_element(By.ID, "login-password")
    submit_btn = driver.find_element(By.ID, "js-login-btn")
    username.send_keys("contact+atb5x@thetestingacademy.com")
    password.send_keys("ATBx@1234")
    submit_btn.click()

    WebDriverWait(driver,15).until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR,".page-heading"),"Dashboard"))

    assert driver.current_url == "https://app.vwo.com/#/dashboard", "Wrong Page"
    uname = driver.find_element(By.XPATH,value="//span[@class='Fw(semi-bold) ng-binding']")
    #kk = driver.find_element(By.XPATH("//p/span[@class ='Fw(semi-bold) ng-binding']"))
    assert uname.text == "Aman"

    # mappbtn.click()
    # assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login", "Incorrect URL"
def test_trialpage():
        trial_link = driver.find_element(By.LINK_TEXT, "Start a free trial")
        trial_link.click()
        assert driver.current_url == "https://vwo.com/free-trial/?utm_medium=website&utm_source=login-page&utm_campaign=mof_eg_loginpage", "Wrong Page"

        time.sleep(10)
        driver.quit()
















































































