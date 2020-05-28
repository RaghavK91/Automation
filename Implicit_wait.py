from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C:\Users\ragha\OneDrive\Desktop\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en") #opening URL takes some time

driver.implicitly_wait(10) # waiting for 10 seconds

assert "Google News" in driver.title

driver.find_element_by_class_name("rdp59b").click()

