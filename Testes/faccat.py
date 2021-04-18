# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pymongo

conexao = pymongo.MongoClient("localhost", 27017)
db = conexao["Notas_FACCAT"]

username_str = input('Username: ').lower()
password_str = input('Password: ').lower()

browser = webdriver.Chrome(ChromeDriverManager (). install())
browser.get('http://187.85.207.60/corpore.net/Login.aspx')


username = browser.find_element_by_id('txtUser')
username.send_keys(username_str)

password = browser.find_element_by_id('txtPass')
password.send_keys(password_str)

btnentra = browser.find_element_by_id('btnLogin')
btnentra.click()


notas_select = browser.find_element_by_id('ctl17_EDU_EduNotaEtapaActionWeb_LinkControl')
notas_select.click()

print ("Disciplina | 1 Bimestre | 2 Bimestre | Media Parcial | Media Final | Total de Faltas")
materia = 0

while  materia < 7:
	disciplina = browser.find_element_by_xpath('//tr[@id="ctl23_xgvNotasFilial_DXDataRow%d"]/td[4]' % materia).text
	bimestre1 = browser.find_element_by_xpath('//tr[@id="ctl23_xgvNotasFilial_DXDataRow%d"]/td[6]' % materia).text
	bimestre2 = browser.find_element_by_xpath('//tr[@id="ctl23_xgvNotasFilial_DXDataRow%d"]/td[8]' % materia).text
	media_parcial = browser.find_element_by_xpath('//tr[@id="ctl23_xgvNotasFilial_DXDataRow%d"]/td[11]' % materia).text
	media_final = browser.find_element_by_xpath('//tr[@id="ctl23_xgvNotasFilial_DXDataRow%d"]/td[12]' % materia).text
	total_faltas = browser.find_element_by_xpath('//tr[@id="ctl23_xgvFaltasFilial_DXDataRow%d"]/td[6]' % materia).text

	disciplina = str(disciplina.strip('\n\t').encode('utf-8')) if disciplina != [] else ""
	
	print (str(disciplina) + ' | ' + str(bimestre1) + ' | ' + str(bimestre2) + ' | ' + str(media_parcial) + ' | ' + str(media_final) + ' | ' + str(total_faltas))

	collection = (db.notas.update(
        {"username": str(username_str),
        "disciplina": str(disciplina)},
        {"disciplina": str(disciplina),
        "bimestre1": str(bimestre1),
        "bimestre2": str(bimestre2),
        "media_parcial": str(media_parcial),
        "media_final": str(media_final),
        "total_faltas": str(total_faltas)}, upsert = True))

	materia += 1