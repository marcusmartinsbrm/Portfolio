import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import os, sys
browser = webdriver.Chrome('./Driver/chromedriver')

browser.get('https://online2pdf.com/pdf2excel')

nomes = ['Lista_A', 'Lista_A_Excluidos', 'Lista_B', 'Lista_B_Excluidos']

for contadordenomes in nomes:
	browser.find_element_by_xpath('//*[@id="main_window"]/form/div[3]/button').click()
	browser.find_element_by_xpath('//*[@id="input_file0"]').send_keys(os.getcwd()+'/'+contadordenomes+".pdf")
	
browser.quit()
browser.exit()