from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='driver/chromedriver')
#Step1
driver.get('https://en.wikipedia.org/wiki/Main_Page')
#Step2
searchBox = driver.find_element(By.ID,'searchInput')
searchBox.send_keys('Test automation')
driver.find_element(By.ID, 'searchButton').click()
#Step3
#Step4
list = driver.find_elements(By.XPATH,'/html/body/div[3]/div[3]/div[5]/div[1]/div[3]/ul/li/a/span[1]')
if len(list)==10:
    print('Checked')
    driver.close()
else:
    print('Error')
