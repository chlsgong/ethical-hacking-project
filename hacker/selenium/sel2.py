from selenium import webdriver
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ChromeOptions
import time

def facebook(driver, username, password):
	# navigate to the application home page
	driver.get("https://www.facebook.com")


	email_field = driver.find_element_by_name("email")
	# get the search textbox
	pass_field = driver.find_element_by_name("pass")


	# enter search keyword and submit
	email_field.send_keys(username)
	pass_field.send_keys(password)
	pass_field.send_keys(Keys.ENTER)

	try:
		elem = driver.find_element_by_class_name("uiHeaderTitle")
		print("Successful Login")
		return True
	except:
		print("Failed Login")
		return False

def gmail(driver):
	# navigate to the application home page
	driver.get("https://www.gmail.com")


	email_field = driver.find_element_by_name("identifier")
	# get the search textbox


	# enter search keyword and submit
	email_field.send_keys("myethicalproject@gmail.com")

	email_field.send_keys(Keys.ENTER)

	driver.implicitly_wait(10)

	pass_field = driver.find_element_by_name("password")

	pass_field.send_keys("easypasswor")

	pass_field.send_keys(Keys.ENTER)

	try:
		elem = driver.find_element_by_class_name("asdfasfdsaf")
		print("Successful Login")
		return True
	except:
		print("Failed Login")
		return False


def reddit(driver, username, password):
	# navigate to the application home page
	driver.get("https://www.reddit.com/login")

	try:
		email_field = driver.find_element_by_id("user_login")
	except:
		email_field = driver.find_element_by_id("loginUsername")
	# get the search textbox
	try:
		pass_field = driver.find_element_by_id("passwd_login")
	except:
		pass_field = driver.find_element_by_id("loginPassword")

	# enter search keyword and submit
	email_field.send_keys(username)
	pass_field.send_keys(password)
	pass_field.send_keys(Keys.ENTER)
	time.sleep(4)
	try:
		#driver.implicitly_wait(3)
		elem = driver.find_element_by_id("passwd_login")
		print("Failed Login")
		return False
	except:
		try:
			#driver.implicitly_wait(3)
			elem = driver.find_element_by_id("loginPassword")
			print("Failed Login")
			return False
		except:
			print("Successful Login")
			return True


def main():
	# get the path of ChromeDriverServer
	chrome_driver_path = "D:/chromedriver.exe"

	opts = ChromeOptions()
	opts.add_experimental_option("detach", True)
	# create a new Chrome session
	driver = webdriver.Chrome(chrome_driver_path, chrome_options=opts)



	#failed attempt example
	attempt = facebook(driver, "myethicalproject@gmail.com", "easypasswordsfsf")
	if attempt == False:
		#successful attempt
		facebook(driver, "myethicalproject@gmail.com", "easypasswor")

	#failed attempt example
	attempt = reddit(driver, "ethicalhackingprojec", "samplepassworsaldkfa")
	if attempt == False:
		#successful attempt
		reddit(driver, "ethicalhackingprojec", "samplepasswor")


	
if __name__ == '__main__':
	main()



