from selenium import webdriver
from selenium.webdriver.common.by import By
import traceback
import time


PATH = '/usr/local/bin/chromedriver'
browser = webdriver.Chrome(PATH)
browser.maximize_window()

try:
    browser.get('https://testautomationpractice.blogspot.com/')
    browser.find_element(By.XPATH,'//*[@id="HTML9"]/div[1]/button').click()

    time.sleep(5)
    #browser.switch_to_alert().accept() # This is will close the alert by clicking OK

    browser.switch_to_alert().dismiss() # This will close the alert by clicking CANCEL
    
except Exception:
    traceback.print_exc()
    browser.close()