#!/usr/bin/python
# -*- coding: utf-8 -*-
from lxml import html
import os, sys
import requests
import re 
import csv
#Novo = open('remedios.csv', 'w')
pa = open('principioativo.csv')
lerpa = csv.reader(pa)
listapa = list(lerpa)

num=1
pagina = ['true']
remedio = ['true']

for principativosite in listapa:
    print principativosite
    remedio = ['true']
    pagina = ['true']
    num=1
    while pagina:
        principativosite = principativosite[0].lower()
        page = requests.get('https://consultaremedios.com.br/%s/pa' %principativosite)
        tree = html.fromstring(page.content)
        remedio = tree.xpath(('//*[@id="search"]/div[2]/div[%s]/div[1]/div[2]/h4/a/span/text()') %num)
        #colocar um delimitador para parar 
        num += 1
        aux = str(remedio)
        print aux
          #      Novo.write(aux)
#Novo.close()