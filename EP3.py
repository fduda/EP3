# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 19:32:56 2015

@author: André, Felipe Duda, Felipe Gross
"""


############################################## Arquivos

alimento = open('alimentos.csv','r+')
lista0 = alimento.readlines()
lista=[]

for i in lista0:
    lista.append(i.strip().split(';'))    
user1 = open('usuario.csv','r+')
user0 = user1.readlines()
user =[]

for i in user0:
    user.append(i.strip().split(','))