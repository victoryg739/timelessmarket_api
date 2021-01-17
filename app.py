from flask import Flask
from scrap import scrapData
from yahoofin import scrap_yahoofin
from flask_cors import CORS
from get_ticker import ticker
from selenium import webdriver

app = Flask(__name__)
CORS(app)

#Later change to production deployment

@app.route('/<ticker>')
def tested(ticker):
    ticker = "aapl"
    driver = webdriver.Chrome(executable_path="chromedriver.exe")
    url = "https://money.tmx.com/en/quote/" + ticker + ":US/financials-filings"
    driver.get(url)
    html = driver.page_source
    return(html)

@app.route('/')
def hello_world():
    return "Nothing to see here"

@app.route("/fundamental/<query>")
def search_query(query):
    return scrapData(query)

@app.route("/yahoofin/<query>")
def search_yahoof(query):
    return scrap_yahoofin(query)

@app.route("/ticker")
def tickers():
    return ticker()


if __name__ == '__main__':
    app.run()
