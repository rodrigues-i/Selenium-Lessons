from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import traceback


PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)
driver.maximize_window()
"""
driver.get('https://ancap.su')

# clicar em Log in
try:
    pr = WebDriverWait(driver,15).until(
        EC.presence_of_element_located((By.LINK_TEXT,'Log in'))
    )
    pr.click()
    
    email = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,'input[type=email]'))
    )
    print(email.is_displayed())
    print(email.is_enabled())

    psw = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,'input[type=password]'))
    )

    print(psw.is_displayed())
    print(psw.is_enabled())

    email.send_keys('Consegui')
    psw.send_keys('Conseguiii')
except Exception:
    v = traceback.format_exc()
    print(v)
    driver.close()
    """
driver.get('https://www.techlistic.com/p/selenium-practice-form.html')

li = [driver.find_element_by_css_selector(f'input[id=exp-{i}]') for i in range(7)]
for k,v in enumerate(li):
    print(f'Is element at position {k} selected?','yes' if v.is_selected() else 'no')
