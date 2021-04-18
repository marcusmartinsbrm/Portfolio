import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

links = ['Fill','Lista_A', 'Lista_A_Excluidos', 'Nada', 'Lista_B', 'Lista_B_Excluidos']



browser = webdriver.Chrome(ChromeDriverManager (). install())
url = 'http://portal.anvisa.gov.br/registros-e-autorizacoes/medicamentos/produtos/medicamentos-de-referencia/lista'

pag=1

while pag<=5:
	
	if pag==3:
		pag=4

	browser.get(url)

	link = browser.find_element_by_xpath('//*[@id="p_p_id_56_INSTANCE_MgZ6wfGi4eGc_"]/div/div/div[1]/div/div[2]/div[1]/a')
	link2 = browser.find_element_by_xpath(('//*[@id="p_p_id_56_INSTANCE_MgZ6wfGi4eGc_"]/div/div/div[1]/div/div[2]/div[2]/div/p[%i]/a')%pag)

	link.click()
	time.sleep(7)
	
	link2.click()
	time.sleep(2)

	r = requests.get(browser.current_url)

	with open(('%s.pdf')%links[pag], 'wb') as f:
		f.write(r.content)
	f.close()

	pag+=1


#download = browser.find_element_by_xpath('//*[@id="download"]')
#download.click(2)


#browser.quit()
#browser.exit()
