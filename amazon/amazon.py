#!/usr/local/bin/python3
from PySide2.QtWidgets import QApplication, QWidget, QPushButton
from PySide2.QtCore import Slot
from selenium import webdriver
import sys

driver = webdriver.Chrome(executable_path= r'/usr/local/bin/chromedriver')
def script():
	driver.find_element_by_xpath("/html/body/div[1]/div[5]/div/div[1]/div/div/div/div[2]/div[5]/div/form/span/span/span/input").click()
	driver.find_element_by_xpath("/html/body/div[1]/div/div[4]/div[2]/div[1]/div/div/div[4]/div/div/div/span[2]/span/a").click()
	driver.find_element_by_xpath("/html/body/div[8]/div/div/div[2]/div/div[1]/div/div[1]/div[1]/div/span/span/input").click()
	

app = QApplication(sys.argv)
# Button
button = QPushButton("START")
button.setGeometry(10, 150, 381, 71)
button.setStyleSheet("background-color: rgb(0, 168, 225);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 168, 225);\n"
"font: 25pt \"Bangers\";")
button.clicked.connect(script)
button.show()
# Loop
app.exec_()