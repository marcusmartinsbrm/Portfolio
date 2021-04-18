# encoding: utf-8
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
import csv
from pymongo import MongoClient
from pyvirtualdisplay import Display
from datetime import datetime
now = datetime.now()

novo = open('RemediosM.csv','a+')

display = Display(visible=0, size=(800,800))
display.start()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome = webdriver.Chrome('/root/chromedriver', chrome_options=chrome_options)

client = MongoClient('mongodb://usersaude:nksaude@172.16.28.72:27017/datalakesaude')
mydb = client['datalakesaude']

alfabeto=('a','b','c','d','e','f','g','h','i','j','k','l','m', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
total=0
novo.write('N' + ';' +'Remedios' + ';' + 'Preco Pago' + ';' +'Economia' + '\n')
for x in alfabeto:
	chrome.get('http://www.multifarmas.com.br/busca/'+ str(x))
	time.sleep(5)
	y=1

	while True:
		try:
			produto = chrome.find_element_by_xpath('/html/body/div/section[1]/section[2]/div['+ str(y) +']//div/a[1]/h3/span').text

			try:
				preco = chrome.find_element_by_xpath('/html/body/div/section[1]/section[2]/div['+ str(y) +']/div/a[1]/div[3]/div/span').text
			except Exception:
				try:
					preco = chrome.find_element_by_xpath('/html/body/div/section[1]/section[2]/div['+ str(y) +']/div/a[1]/div[2]/div/span').text
				except Exception:
					pass
				pass

			try:
				econo = chrome.find_element_by_xpath('/html/body/div/section[1]/section[2]/div['+ str(y) +']/div/a[1]/div[3]/p/span').text
			except Exception:
				try:
					econo = chrome.find_element_by_xpath('/html/body/div/section[1]/section[2]/div['+ str(y) +']/div/a[1]/div[2]/p/span').text
				except Exception:
					pass
				pass
#/--------------------chamada do valor final da variavel e visualização---------------------------------------\
			preco = preco.replace(',','.').replace('R','').replace('$','')
			econo = econo.replace(',','.').replace('R','').replace('$','')

			preco = float(preco)
			econo = float(econo)

			produto = produto.encode('utf-8')
			print (y, ';', (produto), ';', (preco), ';', (econo))

			novo.write(str(y) + ';' + str(produto) + ';' + str(preco) + ';' + str(econo) + ';' + '\n')
			y += 1
			total+=1



			mydb.remedios.insert({
				"remedio":produto,
				"preco":preco,
				"economia":econo,
				"Licenca": 'Anvisa',
				"Data": now
				})


		except Exception as e:
			print (e)
			break

client.close()
chrome.quit()
