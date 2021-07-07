from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chromeOptions = Options()
chromeOptions.add_experimental_option("prefs", {"download.default_directory": "/home/rodrigues/Área de Trabalho", "download.directory_upgrade": True})
PATH = '/usr/local/bin/chromedriver'

# creating the driver instance
driver = webdriver.Chrome(PATH, options=chromeOptions)

driver.get('http://demo.automationtesting.in/FileDownload.html')
driver.maximize_window()

# getting the text are field and sending a text
text_area = driver.find_element_by_id('textbox')
text_area.send_keys('Landing a job as programmer is quite hard and it takes time\nBecause one has to learn loads of stuff.')

# getting the download button
download_button = driver.find_element_by_id('createTxt')
download_button.click()

# gettinf the link to download
driver.find_element_by_id('link-to-download').click()
