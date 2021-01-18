from flask import Flask
from scrap import scrapData
from yahoofin import scrap_yahoofin
from flask_cors import CORS
from get_ticker import ticker
from selenium import webdriver
import os

app = Flask(__name__)
CORS(app)

#Later change to production deployment

@app.route('/<ticker>')
def tested(ticker):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

    driver.get("https://www.google.com")

    # ticker = "aapl"
    # driver = webdriver.Chrome(executable_path="chromedriver.exe")
    # url = "https://money.tmx.com/en/quote/" + ticker + ":US/financials-filings"
    # driver.get(url)
    # html = driver.page_source
    return(driver.page_source)

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
