from selenium import webdriver
from selenium.webdriver.common.by import By
import traceback

PATH = '/usr/local/bin/chromedriver'
driver = webdriver.Chrome(PATH)

driver.get('https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407')

# How to find how many inputboxes are present in the web page

try:
    inputboxes = driver.find_elements(By.CLASS_NAME,'text_field')
    print('There ' + 'are' if len(inputboxes) > 1 else 'is', len(inputboxes), 'inputboxes in the web page.')

except Exception:
    traceback.print_exc()
    driver.close()
