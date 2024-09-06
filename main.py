import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import MoveTargetOutOfBoundsException

email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")


driver = webdriver.Firefox()
driver.get("https://www.linkedin.com/")
action = ActionChains(driver)



login = driver.find_element(By.XPATH, "//a[contains(., 'Sign in')]")
login.click()
time.sleep(2)
user = driver.find_element(By.XPATH, "//input[contains(@id, 'username')]")
user.send_keys(email)
log_pass = driver.find_element(By.XPATH, "//input[contains(@id, 'password')]")
log_pass.send_keys(password)
signin = driver.find_element(By.XPATH, "//button[contains(., 'Sign in')][contains(@class, 'btn__primary')]")
signin.click()
time.sleep(2)
jobs = driver.find_element(By.XPATH, "//span[contains(@title, 'Jobs')]")
jobs.click()
time.sleep(2)
search = driver.find_element(By.XPATH, "//input[contains(@class, 'jobs-search-box')]")
search.send_keys("Junior QA Automation")
time.sleep(1)
search.send_keys(Keys.ENTER)
time.sleep(2)
jobs = driver.find_elements(By.XPATH, "//a[contains(@class, 'ember-view job')][contains(., 'QA Automation')]")
for i in jobs:
    try:
        action.move_to_element(i).click().perform()
        action.pause(2)
        try:
            link = driver.find_element(By.XPATH, "//button[contains(@class, 'jobs-save-button')]")
        except NoSuchElementException:
            time.sleep(2)
        finally:
            link = driver.find_element(By.XPATH, "//button[contains(@class, 'jobs-save-button')]")
            link.click()
    except MoveTargetOutOfBoundsException:
        driver.execute_script("arguments[0].scrollIntoView();", i)
        action.move_to_element(i).click().perform()
        action.pause(2)


