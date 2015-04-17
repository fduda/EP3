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

############################################## Funções

def TMB(idade, peso,sexo, altura):  #Quilogramas, Metros, Anos
    if sexo == 'M':
        return float(88.36 + (13.4*int(peso)) + (4.8*float(altura)) - (5.7*int(idade)))
    if sexo == 'F':
        return float(447.6 + (9.2*int(peso)) + (3.1*float(altura)) - (4.3*int(idade)))
        
tmb = TMB(user[1][1], user[1][2], user[1][3], user[1][4])


def Consumo_diario(tmb, fator):
    if fator == 'mínimo':
        return tmb*1.2 
    if fator == 'baixo':
        return tmb*1.375
    if fator == 'médio':
        return tmb*1.55
    if fator == 'alto':
        return tmb*1.725
    if fator == 'muito alto':
        return tmb*1.9
        
consumo_diario = Consumo_diario(tmb, user[1][5])