import re
from bs4 import BeautifulSoup as bsoup
import requests


def scrap_yahoofin(ticker):
    yahoo_url = "https://finance.yahoo.com/quote/" + ticker
    page = requests.get(yahoo_url)
    soup = bsoup(page.text, 'html.parser')

    rootappmain = soup.find("script", text=re.compile("root.App.main"))
    data = "compiledData:{"+str(rootappmain)[str(rootappmain).find('"summaryProfile'):str(rootappmain).find(',"pageViews')] + "}"

    return data



