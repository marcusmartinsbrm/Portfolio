# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

usernameSTR = input('Username: ').lower()
passwordSTR = input('Password: ').lower()

driver = webdriver.Chrome(ChromeDriverManager (). install())
url = "https://siga.cps.sp.gov.br/ALUNO/login.aspx"

try:
    driver.get(url)

    element = driver.find_element_by_xpath("//input[@id='vSIS_USUARIOID']")
    element.send_keys(usernameSTR)

    element = driver.find_element_by_xpath("//input[@id='vSIS_USUARIOSENHA']")
    element.send_keys(passwordSTR)
    time.sleep(1)

    try:
        element = driver.find_element_by_xpath(
            '//div[@style="position: static; display: block; width: auto;'
            ' height: auto; padding: 0px; margin: 0px; font-style: normal;'
            ' font-variant: normal; font-weight: normal; font-stretch: normal;'
            ' font-size: 11px; line-height: 1; font-family: Arial, Helvetica, sans-serif;'
            ' text-align: left; color: rgb(0, 0, 0); border: none; border-radius: 0px;'
            ' white-space: nowrap; z-index: 2147483646;"]')
        element.click()
    except Exception as e:
        pass

    element = driver.find_element_by_xpath("//input[@name='BTCONFIRMA']")
    print (element.get_attribute('innerHTML'))
    element.click()
    time.sleep(5)
    btnentra = driver.find_element_by_name('BTCONFIRMA')
    btnentra.click()

except Exception as e:
    print (e)
    driver.quit()
