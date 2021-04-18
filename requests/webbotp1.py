#!/usr/bin/python
# -*- coding: utf-8 -*-
from lxml import html
import os, sys
import requests
import re 
import csv

Novo = open('principioativo.csv', 'w')

num=1

pagina = ['true']
produtos =['true']

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for letra in alpha:
    produtos = ['true']
    pagina = ['true']
    num=1
    print 'reset'

    while pagina:
        page = requests.get('https://consultaremedios.com.br/principios-ativos/%s?pagina=%d' %(letra, num))
        print 'https://consultaremedios.com.br/principios-ativos/%s?pagina=%d' %(letra, num)
        tree = html.fromstring(page.content)
    
        pagina = tree.xpath(('//*[@id="%s"]/div[2]/div/div[40]/a/text()') %letra)
        
        x=1

        while produtos:
            produtos = tree.xpath('//*[@id="%s"]/div[2]/div/div[%d]/a/text()' % (letra, x))
            x += 1
            try:
                produtos = str(produtos[0].encode('utf-8'))
                aux = str(produtos+'\n')
                print aux
                Novo.write(aux)
            except Exception:
                pass

        num +=1
        produtos = ['true']

Novo.close()