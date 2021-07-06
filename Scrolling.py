from selenium import webdriver
from selenium.webdriver.common.by import By
import traceback
import time

PATH = '/usr/local/bin/chromedriver'
driver = webdriver.Chrome(PATH)
driver.maximize_window()

driver.get('https://superanimes.org')

try:
    #driver.find_element_by_xpath('//*[@id="rodapeConteudo"]/ul/li[8]/a').click()

    # Scroll down the page by pixel
    #driver.execute_script("window.scrollBy(0, 1000)", "")

    # Scroll down with to desired element
    # Click the link to go to the 100 animes of the week
    driver.find_element(By.XPATH, '//*[@id="lateral"]/div[3]/div[6]/a').click()
    # Finds the 20th anime of the week
    el = driver.find_element(By.XPATH,'//*[@id="corpo"]/div[2]/section/div/div/div/article[20]')
    # Scroll down until the 20th anime of the week
    driver.execute_script("arguments[0].scrollIntoView();", el)
    time.sleep(5)

    # Go to the Super Mangás page
    driver.find_element_by_xpath('//*[@id="rodapeConteudo"]/ul/li[8]/a').click()

    handles = driver.window_handles
    for handle in handles:
        if driver.title != 'Super Mangas':
            driver.switch_to.window(handle)
            if driver.title == 'Super Mangas': break

except Exception:
    hj = traceback.format_exc()
    print(hj)
    driver.quit()
else:
    print(driver.title)
    time.sleep(3)
    
    driver.execute_script('window.scrollBy(0,document.body.scrollHeight)')