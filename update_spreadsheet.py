#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 23:59:15 2019

@author: thiagofhold
"""
#IMPORTANDO AS BIBLIOTECAS
import requests
import re
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials

###########################
###CONECTANDO A PLANILHA###
###########################
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('chave_api.json', scope)

gc = gspread.authorize(credentials)

planilha = gc.open_by_url(URL_PLANILHA)

PLANILHA_STATUS_ATUAL = planilha.worksheet("status_atual")


#ALTERANDO OS VALORES DE DATA
hoje = dt.datetime.today().strftime('%d/%m/%Y')
PLANILHA_STATUS_ATUAL.update_acell('C9', hoje)
print('Valor da data inicial alterado com sucesso.')
print('Valor da data atual: '+ hoje)

total_dias = 700
periodo_anterior = (dt.datetime.now() - dt.timedelta(days=total_dias)).strftime('%d/%m/%Y')
PLANILHA_STATUS_ATUAL.update_acell('C10', periodo_anterior)
print('\nValor da data final alterado com sucesso.')
print('Valor da data anterior: '+ periodo_anterior + '\n')

#########################################################################################
###PASSA PELO OBJETO DE TICKERS, ATUALIZA OS VALORES NA PLANILHA E GRAVA EM UM ARQUIVO###
#########################################################################################

#FUNÇÃO PARA ALTERAR O VALOR DO TICKER:
def altera_ticker(p_ticker):
    #ALTERANDO O VALOR DO TICKER NA PLANILHA
    PLANILHA_STATUS_ATUAL.update_acell('B5', str(p_ticker).upper())
    print('\nValor do ticker atualizado na planilha com sucesso.') 
    print('Ticker alterado para: '+ str(p_ticker))



RELACAO_TICKERS = planilha.worksheet("tickers")
rel_tickers = RELACAO_TICKERS.col_values(1)
rel_tickers = values_list[1:]
print('Relação de tickers: '+ str(rel_tickers))


for ticker in rel_tickers:
    tempo_sleep = 2
    altera_ticker(ticker)
    time.sleep(2)
    print('Aguardando '+str(tempo_sleep)+' segundos.')


































