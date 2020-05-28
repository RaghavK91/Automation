from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome(executable_path=r"C:\Users\ragha\OneDrive\Desktop\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en")
print(driver.title)
driver.get("https://www.sastra.edu/")
time.sleep(7)

print(driver.title)

driver.back()

time.sleep(7)
print(driver.title)

driver.forward()

time.sleep(7)
print(driver.title)