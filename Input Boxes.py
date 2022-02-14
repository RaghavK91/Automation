from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome(executable_path=r"C:\Users\ragha\OneDrive\Desktop\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://www.irctc.co.in/nget/profile/user-registration")

driver.maximize_window()

driver.find_element_by_xpath("/html/body/app-root/app-home/div[1]/app-header/p-dialog[2]/div/div[2]/div/form/div[2]/button").click()

driver.find_element_by_xpath("//*[@id='userName']").send_keys("RaghavK91")

driver.find_element_by_xpath("//*[@id='usrPwd']").send_keys("June@@2020")

driver.find_element_by_xpath("//*[@id='cnfUsrPwd']").send_keys("June@@2020")

# Working with Dropdown
element = driver.find_element_by_xpath("//*[@id='divMain']/div/app-user-registration/div[2]/div/div[2]/div[5]/form/div[4]/div[2]/p-dropdown/div/label")
drp = Select(element)
drp.select_by_visible_text('What was the name of your first school')

#Working with the radio buttons
status = driver.find_element_by_id("M").click()
status = driver.find_element_by_id("M").is_selected()   #gives True or Flse
print(status)
driver.find_element_by_xpath("//*[@id='divMain']/div/app-user-registration/div[2]/div/div[2]/div[5]/form/div[10]/div[2]/label[2]/input").click()

# Working with checkboxes
driver.find_element_by_id("sbi").click() #Info about IRCTC SBI card
driver.find_element_by_xpath("//*[@id='divMain']/div/app-user-registration/div[2]/div/div[2]/div[5]/form/div[21]/div/input").click() #Terms and Conditions check box

