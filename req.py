import requests as rs
import pandas as pd

df= pd.read_csv("D:/DA  10/PYTHON/DATASOURCE/New table/stock data.csv")
currencyurl ='https://api.coinbase.com/v2/exchange-rates'
dict=df.to_dict( orient='records')
#print(dict)

currencyheader = {
    'user-agent' : 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36'
    }
for i in dict:
    
    currencyParams =i ['currency']
    cresp =rs.get(url=currencyurl,
               headers=currencyheader,
               params=currencyParams)
    cdata = cresp.json()
   
    
    inrrate =cdata ['data']['rates']['INR']
    i['inr_rate']=i['Price']*float(inrrate)

df =pd.DataFrame(dict) 
df.to_csv('stock.csv') 
