from selenium import webdriver
from time import sleep
PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)

driver.get('http://www.mercury-tours.com/')
sleep(5)
print(driver.title)

driver.get('https://www.pavantestingtools.com/')
sleep(5)
print(driver.title)

driver.back()
sleep(5)
print(driver.title)

driver.forward()
sleep(5)
print(driver.title)

