from selenium import webdriver

PATH = '/usr/local/bin/chromedriver'

driver = webdriver.Chrome(PATH)
driver.maximize_window()

driver.get('https://testautomationpractice.blogspot.com/')
driver.switch_to.frame(0)

uploader = driver.find_element_by_id('RESULT_FileUpload-10')
uploader.send_keys('/home/rodrigues/Downloads/Python/OpenCV_Tutorial/lena.jpg')