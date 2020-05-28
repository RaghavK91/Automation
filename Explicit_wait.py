from selenium import webdriver
import time
driver = webdriver.Chrome(
    executable_path=r"C:\Users\ragha\OneDrive\Desktop\Drivers\chromedriver_win32\chromedriver.exe")

driver.maximize_window()

driver.get("https://www.yatra.com/")

time.sleep(5)

driver.find_element_by_id("booking_engine_hotels").click()

driver.find_element_by_id("BE_hotel_destination_city").clear()
driver.find_element_by_id("BE_hotel_destination_city").send_keys("Goa, Goa, India")

time.sleep(2)
driver.find_element_by_id("BE_hotel_checkin_date").clear()
driver.find_element_by_id("BE_hotel_checkin_date").send_keys("25 May' 20")

time.sleep(2)
driver.find_element_by_id("BE_hotel_checkout_date").clear()
driver.find_element_by_id("BE_hotel_checkout_date").send_keys("28 May' 20")




