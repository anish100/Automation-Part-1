import pdb
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver_win32\chromedriver.exe")
# Connect the Qlicr Engine with Selenium
driver.get("http://intertradeglobal.24livehost.com")
time.sleep(4)
driver.execute_script("window.scrollTo(0, 500)") 


# search_page = driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/header/div[3]/div[2]/div/div[3]/div/i").click()
# search_input = driver.find_element_by_xpath("/html/body/div[6]/div[2]/div/form/input[1]").send_keys("test")
# print(search_input)
# search_input_enter = driver.find_element_by_xpath("/html/body/div[6]/div[2]/div/form/input[2]").click()




# Home_page = driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/header/div[3]/div[2]/div/div[2]/ul/li[1]/a").click()
# print(Home_page)
# time.sleep(4)

# #About us page
# About_us  = driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/header/div[3]/div[2]/div/div[2]/ul/li[2]/a").click()
# print(About_us)
# time.sleep(4)

# #Our Services Page
# our_services = driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/header/div[3]/div[2]/div/div[2]/ul/li[3]/a").click()
# #print(our_services)
# time.sleep(4)

# Service_private = driver.get("https://intertradeglobal.24livehost.com/services/private-client/")
# print(Service_private)
# time.sleep(2)

# #Scrolling of the Page

# Service_corporateclient = driver.get("https://intertradeglobal.24livehost.com/services/corporate-clients/")
# print(Service_corporateclient)
# time.sleep(3)
# #Scrolling of the Page


# Service_commercial = driver.get("https://intertradeglobal.24livehost.com/services/commercial-funding/")
# print(Service_commercial)
# time.sleep(3)
#Scrolling of the Page





# time.sleep(4)
# new_user_country = driver.find_element_by_name("country")
# drp_country_select = Select(new_user_country)
# print(drp_country_select)


# #Affiliate Services Page
# affiliate_module = driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/header/div[3]/div[2]/div/div[2]/ul/li[4]/a").click()
# print(affiliate_module)
# time.sleep(4)

# # become_affiliate = driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div/div/div/div[4]/div/div/button").click()
# # print(become_affiliate)
# # time.sleep(4)

# security_module  = driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/header/div[3]/div[2]/div/div[2]/ul/li[5]/a").click()
# print(security_module)
# time.sleep(4)

# contact_us = driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/header/div[3]/div[2]/div/div[2]/ul/li[6]/a").click()
# print(contact_us)
# time.sleep(4)

# contact_fullname = driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div[3]/div[2]/div/div/div/div[2]/div[3]/div/div/form/div[2]/div[1]/span/input")
# contact_fullname.send_keys("Mark")
# print(contact_fullname)
# time.sleep(4)

# contact_email = driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div[3]/div[2]/div/div/div/div[2]/div[3]/div/div/form/div[2]/div[2]/span/input")
# contact_email.send_keys("mark@yopmail.com")
# print(contact_email)
# time.sleep(4)

# contact_subject = driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div[3]/div[2]/div/div/div/div[2]/div[3]/div/div/form/div[2]/div[4]/span/input")
# contact_subject.send_keys("Hey All this is my Automation series")
# print("contact_subject")
# time.sleep(4)

# contact_message = driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div[3]/div[2]/div/div/div/div[2]/div[3]/div/div/form/div[2]/div[6]/span/textarea")
# contact_message.send_keys("Hello Everyone")
# print("contact_message")
# time.sleep(4)


# contact_submit = driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div[3]/div[2]/div/div/div/div[2]/div[3]/div/div/form/div[2]/div[7]/input").click()
# print(contact_submit)
# time.sleep(4)
