from selenium import webdriver
from time import sleep

PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)
driver.get('http://demo.automationtesting.in/Windows.html')

print(driver.title)

print(driver.current_url)

driver.find_element_by_xpath('//*[@id="Tabbed"]/a/button').click()

sleep(7)

#driver.close() # Closes current browser

driver.quit() # Closes all browsers