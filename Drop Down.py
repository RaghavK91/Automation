from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path=r"C:\Users\ragha\OneDrive\Desktop\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("http://demo.automationtesting.in/Register.html")

driver.maximize_window()


element = driver.find_element_by_id("Skills")

drp=Select(element)

# Select by visible text
drp.select_by_visible_text('Analytics')

