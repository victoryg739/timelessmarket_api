from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
import requests
import json
import re
from lxml import html
import pandas as pd
import urllib.request


my_url = 'http://financials.morningstar.com/finan/financials/getFinancePart.html?&callback=jsonp1601568971821&t=XNAS:MSFT&region=usa&culture=en-US&cur=&order=asc&_=1601568972042'

text = urllib.request.urlopen(my_url).read().decode()


apijson = text[text.index("(") + 1: text.rindex(")")]
test = json.loads(apijson)
apijson = apijson.replace("\\","")



sp = soup(apijson,"lxml")

htmlDate = sp.findAll("th",{"scope":"col"})
date = []
for a in htmlDate:
    date.append(a.text)
print(date)

htmlRevenue = sp.findAll("td",{'headers':'i0'})
revenue = []
for a in htmlRevenue:
    revenue.append(a.text)
print(revenue)

htmlGrossMargin = sp.findAll("td",{'headers':'i1'})
grossmargin = []
for a in htmlGrossMargin:
    grossmargin.append(a.text)
print(grossmargin)

htmlOperatingIncome = sp.findAll("td",{'headers':'i2'})
operatingincome = []
for a in htmlOperatingIncome:
    operatingincome.append(a.text)
print(operatingincome)

htmlOperatingMargin = sp.findAll("td",{'headers':'i3'})
operatingmargin = []
for a in htmlOperatingMargin:
    operatingmargin.append(a.text)
print(operatingmargin)

htmlNetIncome = sp.findAll("td",{'headers':'i4'})
netIncome = []
for a in htmlNetIncome:
    netIncome.append(a.text)
print(netIncome)

htmlEPS = sp.findAll("td",{'headers':'i5'})
eps = []
for a in htmlEPS:
    eps.append(a.text)
print(eps)

htmldividends = sp.findAll("td",{'headers':'i6'})
dividends = []
for a in htmldividends:
    dividends.append(a.text)
print(dividends)

htmlpayoutratio = sp.findAll("td",{'headers':'i91'})
payoutratio  = []
for a in htmlpayoutratio:
    payoutratio.append(a.text)
print(payoutratio)

htmlshares = sp.findAll("td",{'headers':'i7'})
shares = []
for a in htmlshares:
    shares.append(a.text)
print(shares)

htmlbookvalue = sp.findAll("td",{'headers':'i8'})
bookvalue = []
for a in htmlbookvalue:
    bookvalue.append(a.text)
print(bookvalue)

htmlOperatingCashFlow = sp.findAll("td",{'headers':'i9'})
OperatingCashFlow = []
for a in htmlOperatingCashFlow:
    OperatingCashFlow.append(a.text)
print(OperatingCashFlow)

htmlCapSpending = sp.findAll("td",{'headers':'i10'})
CapSpending = []
for a in htmlCapSpending:
    CapSpending.append(a.text)
print(CapSpending)


htmlfcf = sp.findAll("td",{'headers':'i11'})
fcf = []
for a in htmlfcf:
    fcf.append(a.text)
print(fcf)

htmlfcfPerShare = sp.findAll("td",{'headers':'i90'})
fcfPerShare = []
for a in htmlfcfPerShare:
    fcfPerShare.append(a.text)
print(fcfPerShare)

htmlWorkingCapital = sp.findAll("td",{'headers':'i80'})
WorkingCapital = []
for a in htmlWorkingCapital:
    WorkingCapital.append(a.text)
print(WorkingCapital)