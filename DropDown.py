from selenium import webdriver
from selenium.webdriver.support.ui import Select

PATH = '/usr/local/bin/chromedriver'
driver = webdriver.Chrome(PATH)
driver.maximize_window()

driver.get('https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407')

drop_down = Select(driver.find_element_by_id('RESULT_RadioButton-9'))

drop_down.select_by_index('3') # Evening

# Number of options
number_of_options = len(drop_down.options)
print(f'Number of options: {number_of_options}')

# Capturando todas as opções
all_options = drop_down.options
for option in all_options:
    print(option.text)