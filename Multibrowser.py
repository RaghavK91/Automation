from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path=r"C:\Users\ragha\OneDrive\Desktop\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("http://en.wikipedia.org/wiki/Main_Page")

print(driver.title)  # To get the title of the page


