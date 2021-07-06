from selenium import webdriver
from selenium.webdriver.common.by import By
import traceback

PATH = '/usr/local/bin/chromedriver'
driver = webdriver.Chrome(PATH)

driver.get('http://www.practiceselenium.com/')
try:
    # Getting all the links on the webpage
    links = driver.find_elements(By.TAG_NAME,'a')
    print(len(links))
    print('links:')
    for link in links:
        print(link.text)

    # Clicking a link by lin_text
    #driver.find_element(By.LINK_TEXT,"Let's Talk Tea").click()

    # Clicking link by partial link text
    driver.find_element(By.PARTIAL_LINK_TEXT,"Let").click()
except Exception:
    r = traceback.format_exc()
    print(r)
    driver.quit()