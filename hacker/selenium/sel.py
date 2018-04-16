from selenium import webdriver
import os
from selenium.webdriver.common.keys import Keys



# get the path of ChromeDriverServer
chrome_driver_path = "/Users/charlesgong/Desktop/chromedriver"

# create a new Chrome session
driver = webdriver.Chrome(chrome_driver_path)

# navigate to the application home page
driver.get("https://www.facebook.com")


email_field = driver.find_element_by_name("email")
# get the search textbox
pass_field = driver.find_element_by_name("pass")



# enter search keyword and submit
email_field.send_keys("hello@gmail.com")
pass_field.send_keys("123")
pass_field.send_keys(Keys.ENTER)





