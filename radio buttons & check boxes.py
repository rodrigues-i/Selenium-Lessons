from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

PATH = '/usr/local/bin/chromedriver'
driver = webdriver.Chrome(PATH)
driver.maximize_window()


driver.get('https://www.seleniumeasy.com/test/basic-radiobutton-demo.html')
driver.implicitly_wait(10)

status = WebDriverWait(driver,15).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR,'input[name=optradio]'))
)
status.click()

print(status.is_selected())
 