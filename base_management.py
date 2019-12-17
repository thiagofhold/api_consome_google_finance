#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 00:54:24 2019

@author: thiagofhold
"""

# connect_db.py
# 01_create_db.py
import sqlite3
conn = sqlite3.connect('stocks_base.db')

# definindo um cursor
cursor = conn.cursor()

def criar_tabela():
    # criando a tabela (schema)
    cursor.execute("""
    CREATE TABLE stocks (
            date_stock DATE NOT NULL,
            open FLOAT NOT NULL,
            high FLOAT NOT NULL,
            low FLOAT NOT NULL,
            close FLOAT NOT NULL,
            volume FLOAT  NOT NULL
    );
    """)
    
    print('Tabela criada com sucesso.')
    # desconectando...
    conn.close()
    return 'Tabela criada com sucesso.s'

cursor = conn.cursor()
print('CONECTADO AO BANCO DE DADOS.')
# inserindo dados na tabela
cursor.execute("""
               SELECT * FROM stocks
""")

for linha in cursor.fetchall():
    print(linha)
    
conn.close()
