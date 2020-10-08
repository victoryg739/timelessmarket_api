from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
import json
import urllib.request
import requests

def scrapData(ticker):
    yahoo_url = "https://finance.yahoo.com/quote/"+ticker
    page = requests.get(yahoo_url)
    yahoosoup = soup(page.text, 'html.parser')

    exchangeData = yahoosoup.find("span", {"data-reactid": "9"}).text
    exchange = exchangeData.split(" -", 1)
    exchangeLink = ""
    if(exchange[0] == "NYSE"):
        exchangeLink = "XNYS"
    elif (exchange[0] == "NasdaqGS"):
        exchangeLink = "XNAS"



    my_url = 'http://financials.morningstar.com/finan/financials/getFinancePart.html?&callback=jsonp1601568971821&t='+ exchangeLink + ':'+ticker+'&region=usa&culture=en-US&cur=&order=asc&_=1601568972042'

    text = urllib.request.urlopen(my_url).read().decode()


    apijson = text[text.index("(") + 1: text.rindex(")")]
    test = json.loads(apijson)
    apijson = apijson.replace("\\","")
    
    CombineList = []


    sp = soup(apijson,"lxml")

    htmlDate = sp.findAll("th",{"scope":"col"})
    date = []
    for a in htmlDate:
        date.append(a.text)
    CombineList.append(date)

    htmlRevenue = sp.findAll("td",{'headers':'i0'})
    revenue = ["Revenue"]
    for a in htmlRevenue:
        revenue.append(a.text)
    CombineList.append(revenue)


    htmlGrossMargin = sp.findAll("td",{'headers':'i1'})
    grossmargin = []
    for a in htmlGrossMargin:
        grossmargin.append(a.text)
    CombineList.append(grossmargin)

    htmlOperatingIncome = sp.findAll("td",{'headers':'i2'})
    operatingincome = []
    for a in htmlOperatingIncome:
        operatingincome.append(a.text)
    CombineList.append(operatingincome)

    htmlOperatingMargin = sp.findAll("td",{'headers':'i3'})
    operatingmargin = []
    for a in htmlOperatingMargin:
        operatingmargin.append(a.text)
    CombineList.append(operatingmargin)

    htmlNetIncome = sp.findAll("td",{'headers':'i4'})
    netIncome = []
    for a in htmlNetIncome:
        netIncome.append(a.text)
    CombineList.append(netIncome)

    htmlEPS = sp.findAll("td",{'headers':'i5'})
    eps = []
    for a in htmlEPS:
        eps.append(a.text)
    CombineList.append(eps)

    htmldividends = sp.findAll("td",{'headers':'i6'})
    dividends = []
    for a in htmldividends:
        dividends.append(a.text)
    CombineList.append(dividends)

    htmlpayoutratio = sp.findAll("td",{'headers':'i91'})
    payoutratio  = []
    for a in htmlpayoutratio:
        payoutratio.append(a.text)
    CombineList.append(payoutratio)

    htmlshares = sp.findAll("td",{'headers':'i7'})
    shares = []
    for a in htmlshares:
        shares.append(a.text)
    CombineList.append(shares)

    htmlbookvalue = sp.findAll("td",{'headers':'i8'})
    bookvalue = []
    for a in htmlbookvalue:
        bookvalue.append(a.text)
    CombineList.append(bookvalue)

    htmlOperatingCashFlow = sp.findAll("td",{'headers':'i9'})
    OperatingCashFlow = []
    for a in htmlOperatingCashFlow:
        OperatingCashFlow.append(a.text)
    CombineList.append(OperatingCashFlow)

    htmlCapSpending = sp.findAll("td",{'headers':'i10'})
    CapSpending = []
    for a in htmlCapSpending:
        CapSpending.append(a.text)
    CombineList.append(CapSpending)


    htmlfcf = sp.findAll("td",{'headers':'i11'})
    fcf = []
    for a in htmlfcf:
        fcf.append(a.text)
    CombineList.append(fcf)

    htmlfcfPerShare = sp.findAll("td",{'headers':'i90'})
    fcfPerShare = []
    for a in htmlfcfPerShare:
        fcfPerShare.append(a.text)
    CombineList.append(fcfPerShare)

    htmlWorkingCapital = sp.findAll("td",{'headers':'i80'})
    WorkingCapital = []
    for a in htmlWorkingCapital:
        WorkingCapital.append(a.text)


    CombineList.append(WorkingCapital)
    CombineList = json.dumps(CombineList,ensure_ascii=False)

    return(CombineList)

