#!/usr/bin/python
# -*- coding: utf-8 -*-
from lxml import html
import os, sys
import requests
import re 
import csv
from unidecode import unidecode
pa = open('principioativo.csv', 'rb')
listapa = csv.reader(pa)
salvaremedio = open('remedios.csv', 'w')
for principativosite in listapa:
    num = 1
    numlab = 1
    pacsv = principativosite[0]
    print pacsv 
    a = pacsv.decode('utf-8')
    a = a.strip().replace('+ ','').replace('.','').replace(' ','-').lower()
    a = unidecode(a)
    print unidecode(a)
    page = requests.get('https://consultaremedios.com.br/%s/pa' %a)
    tree = html.fromstring(page.content)
    while True:     
        remedio = tree.xpath(('//*[@id="search"]/div[2]/div[%s]/div[1]/div[2]/h4/a/span/text()') %num)
        lab = tree.xpath(('//*[@id="search"]/div[2]/div[%s]/div[1]/div[2]/a[2]/span/text()') %numlab)
        num += 1
        numlab += 1
        aux = str(remedio) + " ; " + str(lab)
        if lab:
            print 'aux', aux
            laba = lab[0].encode('utf-8')
            reme = remedio[0].encode('utf-8')
            aux2 = str(reme + " ; " + laba + " ; " + principativosite[0] + " ; " + '\n')
            salvaremedio.write(aux2)
        elif not remedio:
            break
salvaremedio.close()
    