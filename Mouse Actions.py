# Mouse Hover

"""
from selenium import webdriver
from selenium.webdriver import ActionChains

PATH = '/usr/local/bin/chromedriver'
driver = webdriver.Chrome(PATH)

driver.get('https://opensource-demo.orangehrmlive.com/')

username = driver.find_element_by_id('txtUsername')
username.send_keys('Admin')

password = driver.find_element_by_id('txtPassword')
password.send_keys('admin123')

driver.find_element_by_css_selector('input[name=Submit]').click()

adm = driver.find_element_by_xpath('//*[@id="mainMenuFirstLevelUnorderedList"]/li[1]')
usrMgt = driver.find_element_by_xpath('//*[@id="mainMenuFirstLevelUnorderedList"]/li[1]/ul/li[1]')
users = driver.find_element_by_xpath('//*[@id="mainMenuFirstLevelUnorderedList"]/li[1]/ul/li[1]/ul/li')

actions = ActionChains(driver)
actions.move_to_element(adm)
actions.move_to_element(usrMgt)
actions.move_to_element(users)
actions.click()
actions.perform()
"""

# Double click

"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

path = '/usr/local/bin/chromedriver'
driver = webdriver.Chrome(path)

driver.get('http://testautomationpractice.blogspot.com/')

double_click_button = driver.find_element(By.XPATH, '//*[@id="HTML10"]/div[1]/button')

actions = ActionChains(driver)
#actions.move_to_element(double_click_button)
actions.double_click(double_click_button)
actions.perform()
"""

# Right click

"""
from selenium import webdriver
from selenium.webdriver import ActionChains

PATH = "/usr/local/bin/chromedriver"
driver = webdriver.Chrome(PATH)

try:
    driver.get('https://swisnl.github.io/jQuery-contextMenu/demo.html')
    elem = driver.find_element_by_xpath('/html/body/div/section/div/div/div/p/span')
except Exception:
    driver.quit()
else:
    actions = ActionChains(driver)
    actions.context_click(elem).perform()
"""

# Drag and drop

from selenium import webdriver
from selenium.webdriver import ActionChains

PATH = '/usr/local/bin/chromedriver'
driver = webdriver.Chrome(PATH)
driver.maximize_window()

try:
    driver.get('http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html')

except Exception:
    driver.quit()

else:
    source_element = driver.find_element_by_xpath('//*[@id="box6"]')
    target_element = driver.find_element_by_id('box106')
finally:
    actions = ActionChains(driver)
    actions.drag_and_drop(source=source_element, target=target_element)
    actions.perform()