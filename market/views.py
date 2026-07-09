from django.shortcuts import render

import  MetaTrader5 as mt5

if not mt5.initialize():
    print("Initialization failed", mt5.last_error())
    quit()

account = mt5.account_info()
print(account)

mt5.shutdown()
