import re
from bs4 import BeautifulSoup as bsoup
import requests


def scrap_yahoofin(ticker):
    yahoo_url = "https://finance.yahoo.com/quote/" + ticker
    page = requests.get(yahoo_url)
    soup = bsoup(page.text, 'html.parser')

    rootappmain = soup.find("script", text=re.compile("root.App.main"))
    data = str(rootappmain)[str(rootappmain).find('root.App.main'):str(rootappmain).find(';\n}(this));')]
    data = data.replace("root.App.main = ","")
    return data



