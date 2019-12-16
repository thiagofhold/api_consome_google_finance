#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 23:38:25 2019

@author: thiagofhold
"""

import datetime as dt


hoje = dt.datetime.today().strftime('%d/%m/%Y')
print('Hoje é: '+ str(hoje))


ano_passado = (dt.datetime.now() - dt.timedelta(days=100)).strftime('%d/%m/%Y')
print('Período anterior: '+ str(ano_passado))