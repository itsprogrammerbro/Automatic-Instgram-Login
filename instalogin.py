from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from  random import randint

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.instagram.com/')
print ("Opened Instagram")

sleep(randint(1,4))
username = driver.find_element_by_name('username')
username.send_keys('programmingkeda')
password = driver.find_element_by_name('password')
password.send_keys('#dummy#account1')


button_login = driver.find_element_by_css_selector('#loginForm > div > div:nth-child(3) > button')
button_login.click()
sleep(randint(3,5))

notnow = driver.find_element_by_css_selector('#react-root > section > main > div > div > div > div > button')
notnow.click()
sleep(randint(3,5))
notificationnotnow = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
notificationnotnow.click()


