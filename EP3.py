# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 19:32:56 2015

@author: André, Felipe Duda, Felipe Gross
"""

############################################## Arquivos e Listas

alimento = open('alimentos.csv','r+')  #abre o arquivo
lista0 = alimento.readlines()
lista=[]

for i in lista0:            #limpa e organiza o arquivo
    lista.append(i.strip().split(';'))    
user1 = open('usuario.csv','r+')
user0 = user1.readlines()
user =[]

for i in user0:
    user.append(i.strip().split(','))       #limpa e organiza a lista

lista_alimentos=[]  
  
for i in range (3, len(user)):
    lista_alimentos.append(user[i])
lista_alimentos.sort()



############################################## Funções

def TMB(idade, peso,sexo, altura):  #Quilogramas, Metros, Anos
    if sexo == 'M':
        return float(88.36 + (13.4*int(peso)) + (4.8*float(altura)) - (5.7*int(idade)))
    if sexo == 'F':
        return float(447.6 + (9.2*int(peso)) + (3.1*float(altura)) - (4.3*int(idade)))
        
tmb = TMB(user[1][1], user[1][2], user[1][3], user[1][4])


def Consumo_diario(tmb, fator):          #cria a função de consumo diário
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

def IMC(peso, altura):              #cria a função de IMC
    if float(altura) >= 1.80:        
        return ((1.3*int(peso))/(float(altura)**2.5)) - 1
    elif float(altura) <= 1.50:
        return ((1.3*int(peso))/(float(altura)**2.5)) + 1 
    else:
        return ((1.3*int(peso))/(float(altura)**2.5))
        
        
imc = IMC(user[1][2], user[1][4])


def Condição(imc):          #Cria a função de Condição
    if imc < 18.5:
        return 'abaixo do peso'
    elif 18.5<imc<24.9:
        return 'normal'
    elif 25<imc<29.9:
        return 'sobrepeso'
    elif imc >= 30:
        return 'obeso'
        
condição_fisica = Condição(imc)


#################################################### dicionário

dias = {}

for i in range (len(lista_alimentos)):
    
    if not lista_alimentos[i][0] in dias:
        dias[lista_alimentos[i][0]] = []
    dias[lista_alimentos[i][0]].append(lista_alimentos[i])    

dicionario = {}

for i in range (len(lista)):
    dicionario[lista[i][0]] = []
    dicionario[lista[i][0]].append(lista[i])

#################################################### dicionário

dias = {}                                #Dicionário com os alimentos ingeridos pelo usuário, organizado por dia

for i in range (len(lista_alimentos)):
    
    if not lista_alimentos[i][0] in dias:
        dias[lista_alimentos[i][0]] = []
    dias[lista_alimentos[i][0]].append(lista_alimentos[i])    

dicionario = {}                         #dicionário com os dados dos alkimentos, nome, quantidade, calorias, proteinas, carboidratos e ggorduras

for i in range (len(lista)):
    dicionario[lista[i][0]] = []
    dicionario[lista[i][0]].append(lista[i])


############# Calorias, Proteinas, Carboidratos e Gorduras 

def calorias_consumidas(data):
    cals = 0    
    for i in range (0,int(len(dias[data])) - 1):
        cals += (dicionario[dias[data][i][1]][2])*(dias[data][i][2]*0.1)

calorias_consumidas("07/04/15")

