from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
import json
import urllib.request
import requests
from yahoo_fin import stock_info
import pandas as pd
import ftplib
import io



def scrap_sp500():
    sp500 = pd.read_html("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")[0]
    sp500["Symbol"] = sp500["Symbol"].str.replace(".", "-", regex=True)
    newSp500= sp500[["Symbol","Security"]]
    newSp500 = newSp500.rename(columns={'Security':'SecurityName'})
    #js = newSp500.to_json(orient = 'records')
    #print(js)
    return newSp500
#scrap_sp500()


def scrap_nasdaq():
    ftp = ftplib.FTP("ftp.nasdaqtrader.com")
    ftp.login()
    ftp.cwd("SymbolDirectory")

    r = io.BytesIO()
    ftp.retrbinary('RETR nasdaqlisted.txt', r.write)

    
    r.seek(0)
    data = pd.read_csv(r, sep = "|")
    data.drop(data.tail(1).index,inplace=True)
    newNasdaq = data[["Symbol","Security Name"]]
    newNasdaq = newNasdaq.rename(columns={'Security Name':'SecurityName'})

   # js = newNasdaq.to_json(orient = 'records')
    #print(js)
    # info = r.getvalue().decode()
    # splits = info.split("|")


    # tickers = [x for x in splits if "\r\n" in x]
    # tickers = [x.split("\r\n")[1] for x in tickers if "NASDAQ" not in x != "\r\n"]
    # tickers = [ticker for ticker in tickers if "File" not in ticker]    

    ftp.close()    
    return newNasdaq


dfNasdaq = scrap_nasdaq()
dfSp500 = scrap_sp500()
result = pd.concat([dfNasdaq, dfSp500], ignore_index=True, sort=True)
jsonData = result.to_json(orient = 'records')
jsonData = json.loads(jsonData)
print(jsonData)
with open('data.json', 'w') as outfile:
    json.dump(jsonData, outfile)