from selenium import webdriver

PATH = '/usr/local/bin/chromedriver'
driver = webdriver.Chrome(PATH)
driver.maximize_window()

driver.get('http://demo.automationtesting.in/Windows.html')

driver.find_element_by_xpath('//*[@id="Tabbed"]/a/button').click()

print(driver.current_window_handle)

handles = driver.window_handles
for handle in handles:
    driver.switch_to_window(handle)
    print(driver.title)