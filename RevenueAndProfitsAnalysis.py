# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 09:35:34 2022

@author: CyprianNdlovu
"""
import requests
import matplotlib.pyplot as plt

api_key='24d1f765af7e6651138b60ed7c26e38c'

company="AAPL"
years=10

### PLOT TITLES ####
title_revenue_and_profits= company + ' Revenue and Profits'



income_statement=requests.get(f"https://financialmodellingprep.com/api/v3/income-statement/{company}?limit={years}&apikey={api_key}")

income_statement=income_statement.json()

revenues=list(reversed([income_statement[i]['revenue'] for i in range(len(income_statement))]))
profits=list(reversed([income_statement[i]['grossProfit'] for i in range(len(income_statement))]))

plt.plot(revenues, label='Revenue')
plt.plot(profits, label='Profit')
plt.title(title_revenue_and_profits)
plt.legend(loc='upper left')
plt.show()


