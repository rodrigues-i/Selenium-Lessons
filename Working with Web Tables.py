from selenium import webdriver
from selenium.webdriver.common.by import By
import traceback

PATH = '/usr/local/bin/chromedriver'

try:
    driver = webdriver.Chrome(PATH)
    driver.get('https://sqengineer.com/practice-sites/practice-tables-selenium/')

    # Getting all the rows
    rows = driver.find_elements_by_xpath('//*[@id="table1"]/tbody/tr')
    print(f'The table has {len(rows)} rows', end=' ')

    # Getting all columns
    columns = driver.find_elements_by_xpath('/html/body/div/div[3]/div/div[1]/main/article/div/table[1]/tbody/tr[1]/th')
    print(f'and {len(columns)} columns')
    print()

    # Printing table content
    for r in range(2,len(rows)+1):
        for c in range(1,len(columns)+1):
            value = driver.find_element(By.XPATH,f'//*[@id="table1"]/tbody/tr[{r}]/td[{c}]').text
            print(value, end='    ')
        print()

except Exception:
    traceback.print_exc()
    driver.quit()