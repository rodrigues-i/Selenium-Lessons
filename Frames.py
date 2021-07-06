from selenium import webdriver
from selenium.webdriver.common.by import By
import time


PATH = '/usr/local/bin/chromedriver'
browser = webdriver.Chrome(PATH)

browser.get('https://seleniumhq.github.io/selenium/docs/api/java/index.html')
browser.find_element_by_link_text('FRAMES').click()

browser.switch_to.frame('packageListFrame')
browser.find_element(By.LINK_TEXT,'org.openqa.selenium').click()
browser.switch_to.default_content()

browser.switch_to_frame('packageFrame')
browser.find_element(By.LINK_TEXT,'WebDriver').click()
browser.switch_to_default_content()

browser.switch_to.frame('classFrame')
browser.find_element_by_link_text('DEPRECATED').click()