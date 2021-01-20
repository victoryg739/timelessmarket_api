from flask import Flask
from scrap import scrapData
from yahoofin import scrap_yahoofin
from flask_cors import CORS
from get_ticker import ticker
from tmxmoney import *
app = Flask(__name__)
CORS(app)

#Later change to production deployment

@app.route('/')
def hello_world():
    return "Nothing to see here"

#Return all tickers
@app.route("/ticker")
def tickers():
    return ticker()

@app.route("/fundamental/<query>")
def search_query(query):
    return scrapData(query)

@app.route("/yahoofin/<query>")
def search_yahoof(query):
    return scrap_yahoofin(query)


@app.route("/tm/annual/<query>")
def search_tmxAnnual(query):
    return scarpTmxAnnual(query)

@app.route("/tm/quarter/<query>")
def search_tmxQuarter(query):
    return scarpTmxQuarter(query)

@app.route("/tm/summary/<query>")
def search_tmxSummary(query):
    return scarpTmxSummary(query)

if __name__ == '__main__':
    app.run()
