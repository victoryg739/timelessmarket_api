from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
import json
import urllib.request
import requests

def scrapData(ticker):

    #Get ticker's exchange
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


    #finance api part
    my_url_finance = 'http://financials.morningstar.com/finan/financials/getFinancePart.html?&callback=jsonp1601568971821&t='+ exchangeLink + ':'+ticker+'&region=usa&culture=en-US&cur=&order=asc&_=1601568972042'
    textFinance = urllib.request.urlopen(my_url_finance).read().decode()
    apijsonFinance = textFinance[textFinance.index("(") + 1: textFinance.rindex(")")]
    apijsonFinance = apijsonFinance.replace("\\","")
    spFinance = soup(apijsonFinance,"lxml")

    #KeyStat api part
    my_url_keystat = 'http://financials.morningstar.com/finan/financials/getKeyStatPart.html?&callback=jsonp1602671629303&t=' + exchangeLink + ':' + ticker + '&region=usa&culture=en-US&cur=&order=asc&_=1601568972042'

    textKeystat = urllib.request.urlopen(my_url_keystat).read().decode()
    apijsonKeystat = textKeystat[textKeystat.index("(") + 1: textKeystat.rindex(")")]
    apijsonKeystat = apijsonKeystat.replace("\\", "")
    spKeystat = soup(apijsonKeystat, "lxml")



    #intialise array
    CombineList = []

    htmlDate = spFinance.findAll("th",{"scope":"col"})
    date = [" "]
    for a in htmlDate:
        date.append(a.text)
    CombineList.append(date)


    # Income statement
    htmlEPS = spFinance.findAll("td",{'headers':'i5'})
    eps = ["Earnings per share"]
    for a in htmlEPS:
        eps.append(a.text)
    CombineList.append(eps)

    htmlRevenue = spFinance.findAll("td",{'headers':'i0'})
    revenue = ["Revenue"]
    for a in htmlRevenue:
        revenue.append(a.text)
    CombineList.append(revenue)

    htmlOperatingIncome = spFinance.findAll("td",{'headers':'i2'})
    operatingincome = ["Operating Income"]
    for a in htmlOperatingIncome:
        operatingincome.append(a.text)
    CombineList.append(operatingincome)

    htmlNetIncome = spFinance.findAll("td",{'headers':'i4'})
    netIncome = ["Net Income"]
    for a in htmlNetIncome:
        netIncome.append(a.text)
    CombineList.append(netIncome)


    #Balance Sheet
    htmlbookvalue = spFinance.findAll("td",{'headers':'i8'})
    bookvalue = ["Book Value"]
    for a in htmlbookvalue:
        bookvalue.append(a.text)
    CombineList.append(bookvalue)

    htmlCurrentRatio = spKeystat.findAll("td", {'headers': 'i65'})
    currentRatio = ["Net Income"]
    for a in htmlCurrentRatio:
        currentRatio.append(a.text)
    CombineList.append(currentRatio)

    htmlQuickRatio = spKeystat.findAll("td", {'headers': 'i66'})
    quickRatio = ["Quick Ratio"]
    for a in htmlQuickRatio:
        quickRatio.append(a.text)
    CombineList.append(quickRatio)

    htmlDebtToEquityRatio = spKeystat.findAll("td", {'headers': 'i68'})
    debtToEquityRatio = ["Debt To Equity Ratio"]
    for a in htmlDebtToEquityRatio:
        debtToEquityRatio.append(a.text)
    CombineList.append(debtToEquityRatio)


    #Profitability
    htmlReturnonAsset = spKeystat.findAll("td",{'headers':'i24'})
    returnonAsset = ["Gross Margin"]
    for a in htmlReturnonAsset:
        returnonAsset.append(a.text)
    CombineList.append(returnonAsset)

    htmlReturnonEquity = spKeystat.findAll("td",{'headers':'i26'})
    returnonEquity = ["Gross Margin"]
    for a in htmlReturnonEquity:
        returnonEquity.append(a.text)
    CombineList.append(returnonEquity)

    htmlReturnonInvestedCapital = spKeystat.findAll("td", {'headers': 'i27'})
    returnonInvestedCapital = ["Gross Margin"]
    for a in htmlReturnonInvestedCapital:
        returnonInvestedCapital.append(a.text)
    CombineList.append(returnonInvestedCapital)

    #Margins
    htmlGrossMargin = spFinance.findAll("td",{'headers':'i1'})
    grossmargin = ["Gross Margin"]
    for a in htmlGrossMargin:
        grossmargin.append(a.text)
    CombineList.append(grossmargin)

    htmlOperatingMargin = spFinance.findAll("td",{'headers':'i3'})
    operatingmargin = ["Operating Margin"]
    for a in htmlOperatingMargin:
        operatingmargin.append(a.text)
    CombineList.append(operatingmargin)

    htmlEbtMargin = spKeystat.findAll("td",{'headers':'i20'})
    ebtMargin = ["EBT Margin"]
    for a in htmlEbtMargin:
        ebtMargin.append(a.text)
    CombineList.append(ebtMargin)

    htmlNetMargin = spKeystat.findAll("td",{'headers':'i20'})
    netMargin = ["Net Margin"]
    for a in htmlNetMargin:
        netMargin.append(a.text)
    CombineList.append(netMargin)


    #Cash Flow
    htmlfcf = spFinance.findAll("td",{'headers':'i11'})
    fcf = ["Free cash flow"]
    for a in htmlfcf:
        fcf.append(a.text)
    CombineList.append(fcf)

    htmlfcfPerShare = spFinance.findAll("td",{'headers':'i90'})
    fcfPerShare = ["Free cash flow/share"]
    for a in htmlfcfPerShare:
        fcfPerShare.append(a.text)
    CombineList.append(fcfPerShare)

    #dividends

    htmldividends = spFinance.findAll("td",{'headers':'i6'})
    dividends = ["Dividends"]
    for a in htmldividends:
        dividends.append(a.text)
    CombineList.append(dividends)

    htmlpayoutratio = spFinance.findAll("td",{'headers':'i91'})
    payoutratio  = ["Payout ratio"]
    for a in htmlpayoutratio:
        payoutratio.append(a.text)
    CombineList.append(payoutratio)


    #others

    htmlshares = spFinance.findAll("td",{'headers':'i7'})
    shares = ["No of shares"]
    for a in htmlshares:
        shares.append(a.text)
    CombineList.append(shares)

    htmlOperatingCashFlow = spFinance.findAll("td",{'headers':'i9'})
    OperatingCashFlow = ["Operating cash flow"]
    for a in htmlOperatingCashFlow:
        OperatingCashFlow.append(a.text)
    CombineList.append(OperatingCashFlow)

    htmlCapSpending = spFinance.findAll("td",{'headers':'i10'})
    CapSpending = ["cap spending"]
    for a in htmlCapSpending:
        CapSpending.append(a.text)
    CombineList.append(CapSpending)

    htmlWorkingCapital = spFinance.findAll("td",{'headers':'i80'})
    WorkingCapital = ["Working capital"]
    for a in htmlWorkingCapital:
        WorkingCapital.append(a.text)


    CombineList.append(WorkingCapital)
    CombineList = json.dumps(CombineList,ensure_ascii=False)

    return(CombineList)


