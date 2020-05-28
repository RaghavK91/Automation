from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path=r"C:\Users\ragha\OneDrive\Desktop\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("http://newtours.demoaut.com/")

user_ele = driver.find_element_by_name("userName")
print(user_ele.is_displayed())
print(user_ele.is_enabled())

pwd_ele = driver.find_element_by_name("password")
print(pwd_ele.is_displayed())
print(pwd_ele.is_enabled())

user_ele.send_keys("mercury")
pwd_ele.send_keys("mercury")

driver.find_element_by_name("login").click()

