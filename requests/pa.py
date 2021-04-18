#!/usr/bin/python
# -*- coding: utf-8 -*-

from lxml import html

import os, sys

import requests
import re 
import csv

Novo = open('principioativo.csv', 'a+')

a = 0
abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
contadorproduto = 0

temp = []
for x in abecedario:
    numeropagina = 1

    while True:        
        numeroproduto = 1

        page = requests.get('https://consultaremedios.com.br/principios-ativos/' + str(x) + '?pagina=' + str(numeropagina))
        tree = html.fromstring(page.content)

        if not (tree.xpath('//*[@id="' + str(x) + '"]/div[2]/div/div[%d]/a/text()' % numeroproduto)):
            break

        while True:
            produtos = tree.xpath('//*[@id="' + str(x) + '"]/div[2]/div/div[%d]/a/text()' % numeroproduto)
            
            if not produtos:
                break

            contadorproduto += 1
            produtos = str(produtos[0].encode('utf-8'))
            aux = str(contadorproduto) + " ; " + str(produtos+'\n')
            
            print aux
            
            Novo.write(aux)
            
            
            numeroproduto += 1

        numeropagina +=1
      
Novo.close()
