import yfinance as yf

def get_info(ticker):

    stock = yf.Ticker(ticker)

    # get stock info

    return stock.info

