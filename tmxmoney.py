import requests

# Get Token
headers = {
    'authority': 'app.quotemedia.com',
    'content-length': '0',
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
    'origin': 'https://money.tmx.com',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://money.tmx.com/',
    'accept-language': 'en-US,en;q=0.9',
}

TokenResponse = requests.post(
    'https://app.quotemedia.com/auth/g/authenticate/dataTool/v0/101020/4e4f1565fb7c9f2a8b4b32b9aa3137af684f3da8a2ce97799d3a7117b14f07be',
    headers=headers).json()



#headers for all report
headers = {
    'authority': 'app.quotemedia.com',
    'accept': '*/*',
    'accept-language': 'en',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
    'origin': 'https://money.tmx.com',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://money.tmx.com/',
}


def scarpTmxQuarter(ticker):
    #Quarter Reports
    params = (
        ('symbol', ticker + ':US'),
        ('numberOfReports', '5'),
        ('latestfiscaldate', 'true'),
        ('currency', 'true'),
        ('reportType', 'Q'),
        ('lang', 'en'),
        ('reportOrder', 'D'),
        ('chart[colors][]', ['#27ae60', '#a6c04b', '#ede348', '#f18247', '#df404a']),
        ('chart[backgroundColor]', '#ffffff'),
        ('chart[legend][textColor]', '#434348'),
        ('chart[legend][backgroundColor]', '#ffffff'),
        ('chart[yAxis][titleTextColor]', '#434348'),
        ('chart[yAxis][labelTextColor]', '#434348'),
        ('chart[xAxis][titleTextColor]', '#434348'),
        ('chart[xAxis][labelTextColor]', '#434348'),
        ('typeList', 'IncomeStatement,BalanceSheet,CashFlow'),
        ('groupReports', '5'),
        ('defaultUnit', 'Millions'),
        ('tradeUrl', ''),
        ('showLogo', 'false'),
        ('lowHigh', 'false'),
        ('token', TokenResponse['token']),
    )

    QuarterlyResponse = requests.get('https://app.quotemedia.com/datatool/getFinancialsEnhancedBySymbol.json', headers=headers, params=params).json()
    return QuarterlyResponse

def scarpTmxAnnual(ticker):
    #Annual Report
    params = (
        ('symbol', ticker + ':US'),
        ('numberOfReports', '5'),
        ('latestfiscaldate', 'true'),
        ('currency', 'true'),
        ('reportType', 'A'),
        ('lang', 'en'),
        ('reportOrder', 'D'),
        ('chart[colors][]', ['#27ae60', '#a6c04b', '#ede348', '#f18247', '#df404a']),
        ('chart[backgroundColor]', '#ffffff'),
        ('chart[legend][textColor]', '#434348'),
        ('chart[legend][backgroundColor]', '#ffffff'),
        ('chart[yAxis][titleTextColor]', '#434348'),
        ('chart[yAxis][labelTextColor]', '#434348'),
        ('chart[xAxis][titleTextColor]', '#434348'),
        ('chart[xAxis][labelTextColor]', '#434348'),
        ('typeList', 'IncomeStatement,BalanceSheet,CashFlow'),
        ('groupReports', '5'),
        ('defaultUnit', 'Millions'),
        ('tradeUrl', ''),
        ('showLogo', 'false'),
        ('lowHigh', 'false'),
        ('token',  TokenResponse['token']),
    )

    AnnualResponse = requests.get('https://app.quotemedia.com/datatool/getFinancialsEnhancedBySymbol.json', headers=headers, params=params).json()
    return AnnualResponse

def scarpTmxSummary(ticker):
    params = (
        ('symbols', ticker + ':US'),
        ('timezone', 'true'),
        ('afterhours', 'true'),
        ('premarket', 'true'),
        ('currencyInd', 'true'),
        ('countryInd', 'true'),
        ('marketstatus', 'true'),
        ('lang', 'en'),
        ('reportOrder', 'D'),
        ('chart[colors][]', ['#27ae60', '#a6c04b', '#ede348', '#f18247', '#df404a']),
        ('chart[backgroundColor]', '#ffffff'),
        ('chart[legend][textColor]', '#434348'),
        ('chart[legend][backgroundColor]', '#ffffff'),
        ('chart[yAxis][titleTextColor]', '#434348'),
        ('chart[yAxis][labelTextColor]', '#434348'),
        ('chart[xAxis][titleTextColor]', '#434348'),
        ('chart[xAxis][labelTextColor]', '#434348'),
        ('typeList', 'IncomeStatement,BalanceSheet,CashFlow'),
        ('groupReports', '5'),
        ('defaultUnit', 'Millions'),
        ('tradeUrl', ''),
        ('showLogo', 'false'),
        ('lowHigh', 'false'),
        ('reportType', 'A'),
        ('token',  TokenResponse['token']),
    )

    SummaryResponse = requests.get('https://app.quotemedia.com/datatool/getEnhancedQuotes.json', headers=headers, params=params).json()
    return SummaryResponse

