#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 00:44:34 2019

@author: thiagofhold
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 22:49:46 2019

@author: thiagofhold
"""


#IMPORTANDO AS BIBLIOTECAS
import requests
import re
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import gspread
from oauth2client.service_account import ServiceAccountCredentials


URL_PLANILHA = 'https://docs.google.com/spreadsheets/d/1LEM6gSrcDPtZSd3j6qjCBTDjEnciGVCAFI3FHH0coiQ/edit?usp=sharing'
# A VARIÁVEL PAGE RECEBE A URL DA PLANILHA.
page = requests.get(URL_PLANILHA)

#UTILIZANDO A BIBLIOTECA BEAUTIFULSOAP PARA RENDERIZAR O DOCUMENTO RECEBIDO
from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')


#RECEBE TODOS OS TITULOS DA TABELA
table_titulos = []
for tb_title in soup.find_all("td", {"class": "s0"}):
    table_titulos.append(re.sub(r'\<.*\>', '', str(re.sub(r'.*<td.*\">', '', str(tb_title)))))


#print(table_titulos)

#RECEBE TODOS OS VALORES DA TABELA:
tot_vals = soup.find_all("td", {"class": "s1"})

#CRUA OS OBJETOS PARA REDCEBER OS VALORES DA TABELA
c_Date = []
c_Open = []
c_High = []
c_Low = []
c_Close = []
c_Volume = []


#FUNÇÃO PARA TRATAR OS VALORES DE DATA DA TABELA
def trata_date(pdt):
    return dt.datetime.strptime(pdt, '%d/%m/%Y %H:%M:%S').strftime('%d/%m/%Y')




#TRATA OS VALORES DA TABELA RECEBIDA
for tb_values in range(0, len(tot_vals), len(table_titulos)):
    c_Date.append(trata_date(re.sub(r'\<.*\>', '', str(re.sub(r'.*<td.*\">', '', str(tot_vals[tb_values]))))))
    c_Open.append(float(re.sub(r'\<.*\>', '', str(re.sub(r'.*<td.*\">', '', str(tot_vals[tb_values+1])))).replace(',','.')))
    c_High.append(float(re.sub(r'\<.*\>', '', str(re.sub(r'.*<td.*\">', '', str(tot_vals[tb_values+2])))).replace(',','.')))
    c_Low.append(float(re.sub(r'\<.*\>', '', str(re.sub(r'.*<td.*\">', '', str(tot_vals[tb_values+3])))).replace(',','.')))
    c_Close.append(float(re.sub(r'\<.*\>', '', str(re.sub(r'.*<td.*\">', '', str(tot_vals[tb_values+4])))).replace(',','.')))
    c_Volume.append(float(re.sub(r'\<.*\>', '', str(re.sub(r'.*<td.*\">', '', str(tot_vals[tb_values+5])))).replace(',','.')))


df = pd.DataFrame({
    'date':c_Date,
    'open':c_Open,
    'high':c_High,
    'low':c_Low,
    'close':c_Close,
    'volume':c_Volume
})

print(df)

print(len(tot_vals))