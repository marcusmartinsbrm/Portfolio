import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import os, sys

browser = webdriver.Chrome()
browser.get('https://online2pdf.com/pdf2excel')
cont=0
#Site de coleta
listas = ['Lista_A', 'Lista_A_Excluidos', 'Lista_B', 'Lista_B_Excluidos']

for contlistas in listas:
	browser.find_element_by_xpath('//*[@id="input_file'+str(cont)+'"]').send_keys(os.getcwd()+"/"+listas[cont]+".pdf")
	cont+=1

option = Select(browser.find_element_by_xpath('//*[@id="conversion_mode_multiple_pdf"]'))
option.select_by_value('single')

browser.find_element_by_xpath('//*[@id="main_window"]/form/div[3]/button').click()
#browser.close()
