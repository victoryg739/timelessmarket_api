import yfinance as yf
import json

def get_info(ticker):

    stock = yf.Ticker(ticker)

    # get stock info
    
    return json.dumps(stock.info)


