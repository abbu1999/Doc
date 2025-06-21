from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("http://192.168.56.103:3000/login")

username = driver.find_element(By.NAME, "user")
password = driver.find_element(By.NAME, "password")

username.send_keys("admin")
password.send_keys("admin")

btn = driver.find_element(By.CLASS_NAME, "css-1b7vft8-button")
btn.click()

driver.save_screenshot("grafana.png")

time.sleep(10)
driver.close()
