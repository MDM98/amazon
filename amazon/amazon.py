#!/usr/local/bin/python3
from PySide2.QtWidgets import QApplication, QWidget, QPushButton
from PySide2.QtCore import Slot
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
import time

driver = webdriver.Chrome(executable_path= r'/usr/local/bin/chromedriver') #THIS FIRST SCRIPT OPENS CHROMINIUM INSTANCE AND LOGS INTO AMAZON 
driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")
time.sleep(1)
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div[1]/form/div/div/div/div[1]/input[1]").send_keys('youremail@gmail.com') #insert email here to login to amazon
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div[1]/form/div/div/div/div[2]/span/span/input').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div/form/div/div[1]/input').send_keys("yourpassword") #insert password here to login to amazon 
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div/form/div/div[2]/span/span/input').click()


    #def script(): OLD CHECKOUT METHOD THAT DOES NOT RETRY ADDING TO CART IF OUT OF STOCK!
	#driver.find_element_by_xpath("/html/body/div[1]/div[5]/div/div[1]/div/div/div/div[2]/div[5]/div/form/span/span/span/input").click()
	#driver.find_element_by_xpath("/html/body/div[1]/div/div[4]/div[2]/div[1]/div/div/div[4]/div/div/div/span[2]/span/a").click()
	#driver.find_element_by_xpath("/html/body/div[8]/div/div/div[2]/div/div[1]/div/div[1]/div[1]/div/span/span/input").click()
	
def checkout():
	while True:
		driver.find_element_by_xpath("/html/body/div[1]/div[5]/div/div[1]/div/div/div/div[2]/div[5]/div/form/span/span/span/input").click() #FUNTION DEFINES THE CHECKOUT PROCCESS
		if "Your Amazon cart is empty" in driver.page_source:
			driver.execute_script("window.history.go(-1)")
		else:
			driver.find_element_by_xpath("/html/body/div[1]/div/div[4]/div[2]/div[1]/div/div/div[4]/div/div/div/span[2]/span/a").click()
			driver.find_element_by_xpath("/html/body/div[8]/div/div/div[2]/div/div[1]/div/div[1]/div[1]/div/span/span/input").click()
#below: opens up the user interface that will run the funtion above when pressed
application = QApplication(sys.argv)
clickme = QPushButton("START")
clickme.setGeometry(10, 150, 380, 70)
clickme.setStyleSheet("background-color: rgb(0, 168, 225);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 168, 225);\n"
"font: 25pt \"Bangers\";")
clickme.clicked.connect(checkout)
clickme.show()
application.exec_()