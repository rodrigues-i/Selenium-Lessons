import traceback
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

PATH = '/usr/local/bin/chromedriver'
driver = webdriver.Chrome(PATH)

driver.get('https://www.superanimes.org/')

driver.implicitly_wait(10)

try:
    assert 'Super Animes - Vivendo um novo Mundo!' in driver.title

    # Fazer log in
    driver.find_element_by_class_name('actionMenuUser').click()

    driver.find_element_by_css_selector('li[id=myLogin]').click()
    
    email = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,'input[name=login]'))
    )
    email.send_keys('xlucasmn')

    senha = driver.find_element(By.ID,'password')
    senha.send_keys('kankuro')

    driver.find_element_by_id('bt-login').click()
    
except Exception:
    s = traceback.format_exc()
    print(s)
    driver.close()