import pandas as pd
from ftplib import FTP
from datetime import datetime
import os.path

def getFileFtp():
    url = "ftp.nasdaqtrader.com"
    ftp = FTP(url)
    ftp.login()
    ftp.cwd('SymbolDirectory')
    localfile = open("nasdaqtraded.txt", 'wb')
    ftp.retrbinary('RETR nasdaqtraded.txt', localfile.write)
    ftp.quit()
    localfile.close()


def ticker():
    # Check if file exist
    if(os.path.exists("nasdaqtraded.txt") == False):
        getFileFtp()


    pd.set_option('display.width', 2000)
    pd.set_option('display.max_columns', 20)

    data = pd.read_csv("nasdaqtraded.txt",sep="|")

    last_row = data.tail(1)
    fileCreationTime = last_row.iloc[0,0]
    fileCreationTime = fileCreationTime.replace("File Creation Time: ","")
    fileCreationTime = datetime.strptime(fileCreationTime,"%m%d%Y%H:%M")
    fileCreationTime_date = fileCreationTime.date()
    today = str(datetime.today().strftime("%Y-%m-%d"))

    if(today != fileCreationTime_date):
        getFileFtp()

    data = data[data["Symbol"].notna()]

    #Remove Z= BATS, V=IEXG, P= NYSE ARCA. http://www.nasdaqtrader.com/trader.aspx?id=symboldirdefs
    data = data[(data["Listing Exchange"] != "Z") & (data["Listing Exchange"] != "V") & (data["Listing Exchange"] != "P") ]
    #Remove equities with $ sign
    data = data[data["Symbol"].str.contains('\$') == False]
    #Remove all test stocks
    data = data[(data["Symbol"].str.contains('ZVV') == False) & (data["Symbol"].str.contains('ZVZZC') == False) & (data["Symbol"].str.contains('ZZT') == False) & (data["Symbol"].str.contains('ZXIET') == False) & (data["Symbol"].str.contains('ZXYZ.A') == False) & (data["Symbol"].str.contains('TEST') == False)]
    #Remove Warrant stocks
    data = data[(data["Security Name"].str.contains('Warrant') == False) & (data["Security Name"].str.contains('warrant') == False) & (data["Security Name"].str.contains('warrants') == False)]

    data = data[['Symbol','Security Name']]

    data = data.to_json()

    return(data)

