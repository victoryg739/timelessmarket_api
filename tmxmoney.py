import requests
import json
import math

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

# headers for all report
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
    # Quarter Reports
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

    QuarterlyResponse = requests.get('https://app.quotemedia.com/datatool/getFinancialsEnhancedBySymbol.json',
                                     headers=headers, params=params).json()
    QuarterlyResponse = QuarterlyResponse['results']['Company']['Report']
    for count, quarter in enumerate(QuarterlyResponse):
        currentQuarterIs = quarter["IncomeStatement"]
        QuarterlyResponse[count]["IncomeStatement"] = {}
        QuarterlyResponse[count]["IncomeStatement"] = {
        **checkJsonKey(QuarterlyResponse, "IncomeStatement", currentQuarterIs, "TotalRevenue", "Total Revenue",True)
        , **checkJsonKey(QuarterlyResponse, "IncomeStatement", currentQuarterIs, "CostOfRevenue", "Cost of Revenue",True)
        , **checkJsonKey(QuarterlyResponse, "IncomeStatement", currentQuarterIs, "NetInterestIncome", "Net Interest Income",True)  # financials
        , **checkJsonKey(QuarterlyResponse, "IncomeStatement", currentQuarterIs, "NonInterestIncome", "Non Interest Income",True)  # financials
        , **checkJsonKey(QuarterlyResponse, "IncomeStatement", currentQuarterIs, "CreditLossesProvision", "Credit Losses Provision",True)  # financials
        , **checkJsonKey(QuarterlyResponse, "IncomeStatement", currentQuarterIs, "NonInterestExpense", "Non Interest Expense",True)  # financials
        , **checkJsonKey(QuarterlyResponse, "IncomeStatement", currentQuarterIs, "GrossProfit", "Gross Profit",True)
        , **checkJsonKey(QuarterlyResponse, "IncomeStatement", currentQuarterIs, "OperatingExpense", "Operating Expense",True)
        , **checkJsonKey(QuarterlyResponse, "IncomeStatement", currentQuarterIs, "OccupancyAndEquipment", "Occupancy and Equipment",True)  # financials
        , **checkJsonKey(QuarterlyResponse, "IncomeStatement", currentQuarterIs, "SellingGeneralAndAdministration", "Selling, General and Administration",True)
        , **checkJsonKey(QuarterlyResponse, "IncomeStatement", currentQuarterIs, "ResearchAndDevelopment", "Research and Development",True)
        , **checkJsonKey(QuarterlyResponse, "IncomeStatement", currentQuarterIs, "DepreciationAndAmortization", "Depreciation and Amortization",True)
        , **checkJsonKey(QuarterlyResponse, "IncomeStatement", currentQuarterIs, "Depletion", "Depletion",True)  # financials
        , **checkJsonKey(QuarterlyResponse, "IncomeStatement", currentQuarterIs, "SecuritiesAmortization", "Securities Amortization",True)  # financials
        , **checkJsonKey(QuarterlyResponse, "IncomeStatement", currentQuarterIs, "OtherNonInterestExpense", "Other Non Interest Expense",True)  # financials
        , **checkJsonKey(QuarterlyResponse, "IncomeStatement", currentQuarterIs, "IncomefromAssociatesandOtherParticipatingInterests", "Income from Associates and Other Participating Interests",True)
        # financials
        , **checkJsonKey(QuarterlyResponse, "IncomeStatement", currentQuarterIs, "OperatingIncome", "Operating Income",True)
        , **checkJsonKey(QuarterlyResponse, "IncomeStatement", currentQuarterIs, "NetNonOperatingInterestIncomeExpense", "Net Interest",True)
        , **checkJsonKey(QuarterlyResponse, "IncomeStatement", currentQuarterIs, "OtherIncomeExpense", "Other Income Expense",True)
        , **checkJsonKey(QuarterlyResponse, "IncomeStatement", currentQuarterIs, "PretaxIncome", "Income before Tax",True)
        , **checkJsonKey(QuarterlyResponse, "IncomeStatement", currentQuarterIs, "TaxProvision", "Provision for Income Tax",True)
        , **checkJsonKey(QuarterlyResponse, "IncomeStatement", currentQuarterIs, "NetIncome", "Net Income",True)
        , **checkJsonKey(QuarterlyResponse, "IncomeStatement", currentQuarterIs, "NetIncomeCommonStockholders", "Net Income Common Shareholders",True)
        , **checkJsonKey(QuarterlyResponse, "IncomeStatement", currentQuarterIs, "BasicEPS", "Basic EPS",False)
        , **checkJsonKey(QuarterlyResponse, "IncomeStatement", currentQuarterIs, "DilutedEPS", "Diluted EPS",False)
        , **checkJsonKey(QuarterlyResponse, "IncomeStatement", currentQuarterIs, "BasicAverageShares", "Basic Average Shares Outstanding",True)
        , **checkJsonKey(QuarterlyResponse, "IncomeStatement", currentQuarterIs, "DilutedAverageShares", "Diluted Average Shares Outstanding",True)
        , **checkJsonKey(QuarterlyResponse, "IncomeStatement", currentQuarterIs, "DividendPerShare", "Dividend Per Share",False)
        , **checkJsonKey(QuarterlyResponse, "IncomeStatement", currentQuarterIs, "EBIT", "EBIT",True)
        , **checkJsonKey(QuarterlyResponse, "IncomeStatement", currentQuarterIs, "EBITDA", "EBITDA",True)}

        currentQuarterBs = quarter["BalanceSheet"]
        QuarterlyResponse[count]["BalanceSheet"] = {}
        QuarterlyResponse[count]["BalanceSheet"] = {
        **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "TotalAssets", "Total Assets",True)
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "CurrentAssets", "Current Assets",True)
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "CashAndCashEquivalents", "Cash and Cash Equivalents",True)
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "ShortTermInvestments", "Short Term Investments",True)
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "RestrictedCashAndInvestments", "Restricted Cash and Investments",True)  # financials
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "MoneyMarketInvestments", "Money Market Investments",True)  # financials
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "SecuritiesAndInvestments", "Securities and Investments",True)  # financials
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "NetLoan", "Net Loan",True)  # financials
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "Receivables", "Receivables",True)
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "Inventory", "Inventory",True)
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "PrepaidAssets", "Prepaid Assets",True)
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "RestrictedCash", "Restricted Cash",True)
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "AssetHeldForSaleCurrent", "Asset Held for Sale Current",True)
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "HedgingAssetsCurrent", "Hedging Assets Current",True)
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "OtherCurrentAssets", "Other Current Assets",True)
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "TotalNonCurrentAssets", "Total Non Current Assets",True)
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "NetPPE", "Net PPE",True)
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "GrossPPE", "Gross PPE",True)  # tab
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "AccumulatedDepreciation", "Accumulated Depreciation",True)
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "Goodwill", "Goodwill",True)
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "OtherIntangibleAssets", "Intangible Assets",True)
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "InvestmentAndAdvances", "Investment And Advances",True)
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "FinancialAssets", "Financial Assets",True)
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "NonCurrentAccountsReceivable", "Non Current Accounts Receivable",True)
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "NonCurrentNoteReceivables", "Non Current Note Receivable",True)
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "DueFromRelatedPartiesNonCurrent", "Due From Related Parties Non Current",True)
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "NonCurrentDeferredAssets", "Non Current Deferred Assets",True)
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "NonCurrentPrepaidAssets", "Non Current Deferred Assets",True)
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "DeferredAssets", "Deferred Assets",True)  # financials
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "DefinedPensionBenefit", "Defined Pension Benefit",True)
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "OtherNonCurrentAssets", "Other Non Current Assets",True)
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "AssetsHeldForSale", "AssetsHeldForSale",True)  # financials
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "OtherAssets", "Other Assets",True)  # financials
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "TotalLiabilities", "Total Liabilities",True)
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "TotalDeposits", "Total Deposits",True)  # financials
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "FederalFundsPurchasedAndSecuritiesSoldUnderAgreementToRepurchase",
                         "Federal Funds Purchased and Securities Sold Under Agreement to Repurchase",True)  # financials
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "SecuritiesLoaned", "SecuritiesLoaned",True)  # financials
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "TradingLiabilities", "Trading Liabilities",True)  # financials
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "SecuritiesLoaned", "SecuritiesLoaned",True)  # financials
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "CurrentLiabilities", "Current Liabilities",True)
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "PayablesAndAccruedExpenses", "Payables and Accrued Expenses",True)
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "CurrentProvisions", "Current Provisions",True)
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "PensionandOtherPostRetirementBenefitPlansCurrent", "Pension and Other Post Retirement Benefit Plans Current",True)
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "CurrentDebtAndCapitalLeaseObligation", "Current Debt and Capital Lease Obligation",True)
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "CurrentDeferredLiabilities", "Current Deferred Liabilities",True)
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "OtherCurrentLiabilities", "Other Current Liabilities",True)
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "TotalNonCurrentLiabilities", "Total Non Current Liabilities",True)
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "LongTermProvisions", "Long Term Provisions",True)
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "LongTermDebtAndCapitalLeaseObligation", "Long Term Debt and Capital Lease Obligation",True)
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "NonCurrentDeferredLiabilities", "NonCurrentDeferredLiabilities",True)
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "TradeandOtherPayablesNonCurrent", "Trade and Other Payables Non Current",True)
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "DuetoRelatedPartiesNonCurrent", "Dueto Related Parties Non Current",True)
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "NonCurrentAccruedExpenses", "Non Current Accrued Expenses",True)
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "EmployeeBenefits", "Employee Benefits",True)
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "DerivativeProductLiabilities", "Derivative Product Liabilities",True)
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "PreferredSecuritiesOutsideStockEquity", "Preferred Securities Outside Stock Equity",True)
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "RestrictedCommonStock", "Restricted Common Stock",True)
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "LiabilitiesHeldforSaleNonCurrent", "Liabilities Held for Sale Non Current",True)
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "OtherNonCurrentLiabilities", "Other Non Current Liabilities",True)
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "LiabilitiesOfDiscontinuedOperations", "Liabilities of Discontinued Operations",True)  # financials
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "OtherLiabilities", "Other Liabilities",True)  # financials
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "TotalEquityGrossMinority", "Total Equity",True)
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "StockholdersEquity", "Stockholders Equity",True)
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "CapitalStock", "Capital Stock",True)  # tab
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "AdditionalPaidInCapital", "Additional Paid in Capital",True)
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "RetainedEarnings", "Retained Earnings",True)
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "TreasuryStock", "Treasury Stock",True)
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "GainsLossesNotAffectingRetainedEarnings", "Reserves/Accumulated Comprehensive Income/Losse",True)
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "OtherEquityInterest", "Other Equity Interest",True)
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "MinorityInterest", "Minority Interest",True)
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "TotalCapitalization", "Total Capitalization",True)
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "CapitalLeaseObligations", "Capital Lease Obligations",True)}

        currentQuarterCf = quarter["CashFlow"]
        QuarterlyResponse[count]["CashFlow"] = {}
        QuarterlyResponse[count]["CashFlow"] = {
        **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "OperatingCashFlow", "Operating Cash Flow",True)
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "CashFlowFromContinuingOperatingActivities", "Cash from Continuing Operating Activities",True)
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "NetIncomeFromContinuingOperations", "Net Income",True)  # tab
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "OperatingGainsLosses", "Operating Gains Losses",True)
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "DepreciationAmortizationDepletion", "Depreciation Amortization Depletion",True)
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "DeferredTax", "Deferred Tax",True)
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "AmortizationOfFinancingCostsAndDiscounts", "Amortization of Financing Costs and Discounts",True)
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "AmortizationOfSecurities", "Amortization of Securities",True)
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "AssetImpairmentCharge", "Asset Impairment Charge",True)
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "ProvisionandWriteOffofAssets", "Provision and Write Off of Assets",True)
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "UnrealizedGainLossOnInvestmentSecuritites", "Unrealized GainLossOnInvestmentSecuritites",True)
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "StockBasedCompensation", "Stock Based Compensation",True)
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "ExcessTaxBenefitFromStockBasedCompensation", "Excess Tax Benefit from Stock Based Compensation",True)
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "ProvisionForLoanLeaseAndOtherLosses", "Provision for Loan Lease and Other Losses",True)
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "OtherNonCashItems", "Other Non Cash Items",True)
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "ChangeInWorkingCapital", "Changes in Operating Assets and Liabilities",True)
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "ChangeInReceivables", "Receivables",True)  # tab
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "ChangeInInventory", "Inventory",True)
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "ChangeInPrepaidAssets", "Prepaid Assets",True)
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "ChangeInPayablesAndAccruedExpense", "Payables and Accrued Expense",True)
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "ChangeInOtherCurrentAssets", "Other Current Assets",True)
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "ChangeInOtherCurrentLiabilities", "Other Current Liabilities",True)
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "ChangeInOtherWorkingCapital", "Other Working Capital",True)  # untab
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "DividendPaidCFO", "DividendPaidCFO",True)
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "DividendReceivedCFO", "Dividend Received CFO",True)
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "InterestPaidCFO", "Interest Paid CFO",True)
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "InterestReceivedCFO", "Interest Received CFO",True)
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "TaxesRefundPaid", "Taxes Refund Paid",True)  # untab
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "CashFromDiscontinuedOperatingActivities", "Cash from Discontinued Operating Activities",True)
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "InvestingCashFlow", "Investing Cash Flow",True)
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "CashFlowFromContinuingInvestingActivities", "Cash from Continuing Investing Activities",True)
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "CapitalExpenditureReported", "Capital Expenditure Reported",True)
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "ProceedsPaymentFederalFundsSoldAndSecuritiesPurchasedUnderAgreementToResell",
                         "Federal Funds Sold and Securities Purchased Under Agreement to Resell",True)  # financials
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "ProceedsPaymentInInterestBearingDepositsInBank", "Interest Bearing Deposits in Bank",True)  # financials
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "NetPPEPurchaseAndSale", "Net PPE Purchase and Sale",True)
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "PurchaseOfPPE", "Purchase Of PPE",True)
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "SaleOfPPE", "Sale of PPE",True)
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "NetBusinessPurchaseAndSale", "Net Business Purchase and Sale",True)
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "NetInvestmentPropertiesPurchaseAndSale", "Net Investment Properties Purchase and Sale",True)
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "NetInvestmentPurchaseAndSale", "Net Investment Purchase and Sale",True)
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "NetProceedsPaymentForLoan", "Net Proceeds Payment for Loan",True)  # financials
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "DividendsReceivedCFI", "Dividends Received CFI",True)
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "InterestsReceivedCFI", "Interests Received CFI",True)
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "NetOtherInvestingChanges", "Net Other Investing Changes",True)
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "CashFromDiscontinuedInvestingActivities", "Cash from Discontinued Investing Activities",True)
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "FinancingCashFlow", "Financing Cash Flow",True)
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "CashFlowFromContinuingFinancingActivities", "Cash from Continuing Financing Activities",True)
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "ChangeInFederalFundsAndSecuritiesSoldForRepurchase", "Federal Funds and Securities Sold",True)  # financials
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "IncreaseDecreaseInDeposit", "Increase Decrease in Deposit",True)  # financials
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "NetIssuancePaymentsOfDebt", "Net Issuance Payments of Debt",True)
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "NetLongTermDebtIssuance", "Net Long Term Debt Issuance",True)  # tab
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "LongTermDebtIssuance", "Long Term Debt Issuance",True)
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "LongTermDebtPayments", "Long Term Debt Payments",True)  # untab
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "NetShortTermDebtIssuance", "Net Short Term Debt Issuance",True)  # tab
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "ShortTermDebtIssuance", "Short Term Debt Issuance",True)
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "ShortTermDebtPayments", "Short Term Debt Payments",True)
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "NetCommonStockIssuance", "Net Common Stock Issuance",True)
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "CommonStockIssuance", "Common Stock Issuance",True)
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "CommonStockPayments", "Common Stock Payments",True)
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "NetPreferredStockIssuance", "Net Preferred Stock Issuance",True)
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "CashDividendsPaid", "Cash Dividends Paid",True)
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "ProceedsFromStockOptionExercised", "Proceeds from Stock Option Exercised",True)
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "InterestPaidCFF", "Interest Paid CFF",True)
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "NetOtherFinancingCharges", "Net Other Financing Charges",True)
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "CashFromDiscontinuedFinancingActivities", "Cash from Discontinued Financing Activities",True)
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "CashFlowFromDiscontinuedOperation", "Cash Flow from Discontinued Operation",True)
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "OtherCashAdjustmentInsideChangeInCash", "Other Cash Adjustment Inside Change In Cash",True)
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "BeginningCashPosition", "Beginning Cash Position",True)
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "ChangesInCash", "Net Change in Cash",True)
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "EndCashPosition", "End Cash Position",True)
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "IncomeTaxPaidSupplementalData", "Income Tax Paid, Supplemental",True)
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "InterestPaidSupplementalData", "Interest Paid, Supplemental",True)
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "CapitalExpenditure", "Capital Expenditure",True)}




    firstFormat = {
        k: [d.get(k) for d in QuarterlyResponse]
        for k in set().union(*QuarterlyResponse)
    }
    from collections import defaultdict, ChainMap
    incomeStatement = defaultdict(list)

    for d in firstFormat["IncomeStatement"]:
        for k, v in d.items():
            incomeStatement[k].insert(0, v)

    balanceSheet = defaultdict(list)

    for d in firstFormat["BalanceSheet"]:
        for k, v in d.items():
            balanceSheet[k].insert(0, v)

    cashFlow = defaultdict(list)

    for d in firstFormat["CashFlow"]:
        for k, v in d.items():
            cashFlow[k].insert(0, v)

    formattedQuartelyResponse = ChainMap(firstFormat["reportDate"][::-1], incomeStatement, balanceSheet, cashFlow)
    return json.dumps(formattedQuartelyResponse.maps)


def scarpTmxAnnual(ticker):
    # Annual Report
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
        ('token', TokenResponse['token']),
    )

    AnnualResponse = requests.get('https://app.quotemedia.com/datatool/getFinancialsEnhancedBySymbol.json',
                                  headers=headers, params=params).json()
    AnnualResponse = AnnualResponse['results']['Company']['Report']
    for count, year in enumerate(AnnualResponse):
        currentYearIs = year["IncomeStatement"]
        AnnualResponse[count]["IncomeStatement"] = {}
        AnnualResponse[count]["IncomeStatement"] = {
        **checkJsonKey(AnnualResponse, "IncomeStatement", currentYearIs, "TotalRevenue", "Total Revenue",True)
        , **checkJsonKey(AnnualResponse, "IncomeStatement", currentYearIs, "CostOfRevenue", "Cost of Revenue",True)
        , **checkJsonKey(AnnualResponse, "IncomeStatement", currentYearIs, "NetInterestIncome", "Net Interest Income",True)  # financials
        , **checkJsonKey(AnnualResponse, "IncomeStatement", currentYearIs, "NonInterestIncome", "Non Interest Income",True)  # financials
        , **checkJsonKey(AnnualResponse, "IncomeStatement", currentYearIs, "CreditLossesProvision", "Credit Losses Provision",True)  # financials
        , **checkJsonKey(AnnualResponse, "IncomeStatement", currentYearIs, "NonInterestExpense", "Non Interest Expense",True)  # financials
        , **checkJsonKey(AnnualResponse, "IncomeStatement", currentYearIs, "GrossProfit", "Gross Profit",True)
        , **checkJsonKey(AnnualResponse, "IncomeStatement", currentYearIs, "OperatingExpense", "Operating Expense",True)
        , **checkJsonKey(AnnualResponse, "IncomeStatement", currentYearIs, "OccupancyAndEquipment", "Occupancy and Equipment",True)  # financials
        , **checkJsonKey(AnnualResponse, "IncomeStatement", currentYearIs, "SellingGeneralAndAdministration", "Selling, General and Administration",True)
        , **checkJsonKey(AnnualResponse, "IncomeStatement", currentYearIs, "ResearchAndDevelopment", "Research and Development",True)
        , **checkJsonKey(AnnualResponse, "IncomeStatement", currentYearIs, "DepreciationAndAmortization", "Depreciation and Amortization",True)
        , **checkJsonKey(AnnualResponse, "IncomeStatement", currentYearIs, "Depletion", "Depletion",True)  # financials
        , **checkJsonKey(AnnualResponse, "IncomeStatement", currentYearIs, "SecuritiesAmortization", "Securities Amortization",True)  # financials
        , **checkJsonKey(AnnualResponse, "IncomeStatement", currentYearIs, "OtherNonInterestExpense", "Other Non Interest Expense",True)  # financials
        , **checkJsonKey(AnnualResponse, "IncomeStatement", currentYearIs, "IncomefromAssociatesandOtherParticipatingInterests", "Income from Associates and Other Participating Interests",True)#financials
        , **checkJsonKey(AnnualResponse, "IncomeStatement", currentYearIs, "OperatingIncome", "Operating Income",True)
        , **checkJsonKey(AnnualResponse, "IncomeStatement", currentYearIs, "NetNonOperatingInterestIncomeExpense", "Net Interest",True)
        , **checkJsonKey(AnnualResponse, "IncomeStatement", currentYearIs, "OtherIncomeExpense", "Other Income Expense",True)
        , **checkJsonKey(AnnualResponse, "IncomeStatement", currentYearIs, "PretaxIncome", "Income before Tax",True)
        , **checkJsonKey(AnnualResponse, "IncomeStatement", currentYearIs, "TaxProvision", "Provision for Income Tax",True)
        , **checkJsonKey(AnnualResponse, "IncomeStatement", currentYearIs, "NetIncome", "Net Income",True)
        , **checkJsonKey(AnnualResponse, "IncomeStatement", currentYearIs, "NetIncomeCommonStockholders", "Net Income Common Shareholders",True)
        , **checkJsonKey(AnnualResponse, "IncomeStatement", currentYearIs, "BasicEPS", "Basic EPS",False)
        , **checkJsonKey(AnnualResponse, "IncomeStatement", currentYearIs, "DilutedEPS", "Diluted EPS",False)
        , **checkJsonKey(AnnualResponse, "IncomeStatement", currentYearIs, "BasicAverageShares", "Basic Average Shares Outstanding",True)
        , **checkJsonKey(AnnualResponse, "IncomeStatement", currentYearIs, "DilutedAverageShares", "Diluted Average Shares Outstanding",True)
        , **checkJsonKey(AnnualResponse, "IncomeStatement", currentYearIs, "DividendPerShare", "Dividend Per Share",False)
        , **checkJsonKey(AnnualResponse, "IncomeStatement", currentYearIs, "EBIT", "EBIT",True)
        , **checkJsonKey(AnnualResponse, "IncomeStatement", currentYearIs, "EBITDA", "EBITDA",True)}

        currentYearBs = year["BalanceSheet"]
        AnnualResponse[count]["BalanceSheet"] = {}
        AnnualResponse[count]["BalanceSheet"] = {
        **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "TotalAssets", "Total Assets",True)
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "CurrentAssets", "Current Assets",True)
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "CashAndCashEquivalents", "Cash and Cash Equivalents",True)
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "ShortTermInvestments", "Short Term Investments",True)
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "RestrictedCashAndInvestments", "Restricted Cash and Investments",True)  # financials
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "MoneyMarketInvestments", "Money Market Investments",True)  # financials
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "SecuritiesAndInvestments", "Securities and Investments",True)  # financials
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "NetLoan", "Net Loan",True)  # financials
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "Receivables", "Receivables",True)
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "Inventory", "Inventory",True)
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "PrepaidAssets", "Prepaid Assets",True)
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "RestrictedCash", "Restricted Cash",True)
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "AssetHeldForSaleCurrent", "Asset Held for Sale Current",True)
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "HedgingAssetsCurrent", "Hedging Assets Current",True)
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "OtherCurrentAssets", "Other Current Assets",True)
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "TotalNonCurrentAssets", "Total Non Current Assets",True)
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "NetPPE", "Net PPE",True)
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "GrossPPE", "Gross PPE",True)  # tab
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "AccumulatedDepreciation", "Accumulated Depreciation",True)
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "Goodwill", "Goodwill",True)
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "OtherIntangibleAssets", "Intangible Assets",True)
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "InvestmentAndAdvances", "Investment And Advances",True)
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "FinancialAssets", "Financial Assets",True)
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "NonCurrentAccountsReceivable", "Non Current Accounts Receivable",True)
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "NonCurrentNoteReceivables", "Non Current Note Receivable",True)
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "DueFromRelatedPartiesNonCurrent", "Due From Related Parties Non Current",True)
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "NonCurrentDeferredAssets", "Non Current Deferred Assets",True)
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "NonCurrentPrepaidAssets", "Non Current Deferred Assets",True)
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "DeferredAssets", "Deferred Assets",True)  # financials
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "DefinedPensionBenefit", "Defined Pension Benefit",True)
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "OtherNonCurrentAssets", "Other Non Current Assets",True)
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "AssetsHeldForSale", "AssetsHeldForSale",True)  # financials
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "OtherAssets", "Other Assets",True)  # financials
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "TotalLiabilities", "Total Liabilities",True)
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "TotalDeposits", "Total Deposits",True)  # financials
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "FederalFundsPurchasedAndSecuritiesSoldUnderAgreementToRepurchase",
                         "Federal Funds Purchased and Securities Sold Under Agreement to Repurchase",True)  # financials
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "SecuritiesLoaned", "SecuritiesLoaned",True)  # financials
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "TradingLiabilities", "Trading Liabilities",True)  # financials
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "SecuritiesLoaned", "SecuritiesLoaned",True)  # financials
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "CurrentLiabilities", "Current Liabilities",True)
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "PayablesAndAccruedExpenses", "Payables and Accrued Expenses",True)
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "CurrentProvisions", "Current Provisions",True)
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "PensionandOtherPostRetirementBenefitPlansCurrent", "Pension and Other Post Retirement Benefit Plans Current",True)
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "CurrentDebtAndCapitalLeaseObligation", "Current Debt and Capital Lease Obligation",True)
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "CurrentDeferredLiabilities", "Current Deferred Liabilities",True)
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "OtherCurrentLiabilities", "Other Current Liabilities",True)
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "TotalNonCurrentLiabilities", "Total Non Current Liabilities",True)
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "LongTermProvisions", "Long Term Provisions",True)
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "LongTermDebtAndCapitalLeaseObligation", "Long Term Debt and Capital Lease Obligation",True)
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "NonCurrentDeferredLiabilities", "NonCurrentDeferredLiabilities",True)
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "TradeandOtherPayablesNonCurrent", "Trade and Other Payables Non Current",True)
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "DuetoRelatedPartiesNonCurrent", "Dueto Related Parties Non Current",True)
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "NonCurrentAccruedExpenses", "Non Current Accrued Expenses",True)
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "EmployeeBenefits", "Employee Benefits",True)
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "DerivativeProductLiabilities", "Derivative Product Liabilities",True)
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "PreferredSecuritiesOutsideStockEquity", "Preferred Securities Outside Stock Equity",True)
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "RestrictedCommonStock", "Restricted Common Stock",True)
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "LiabilitiesHeldforSaleNonCurrent", "Liabilities Held for Sale Non Current",True)
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "OtherNonCurrentLiabilities", "Other Non Current Liabilities",True)
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "LiabilitiesOfDiscontinuedOperations", "Liabilities of Discontinued Operations",True)  # financials
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "OtherLiabilities", "Other Liabilities",True)  # financials
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "TotalEquityGrossMinority", "Total Equity",True)
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "StockholdersEquity", "Stockholders Equity",True)
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "CapitalStock", "Capital Stock",True)  # tab
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "AdditionalPaidInCapital", "Additional Paid in Capital",True)
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "RetainedEarnings", "Retained Earnings",True)
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "TreasuryStock", "Treasury Stock",True)
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "GainsLossesNotAffectingRetainedEarnings", "Reserves/Accumulated Comprehensive Income/Losse",True)
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "OtherEquityInterest", "Other Equity Interest",True)
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "MinorityInterest", "Minority Interest",True)
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "TotalCapitalization", "Total Capitalization",True)
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "CapitalLeaseObligations", "Capital Lease Obligations",True)}

        currentYearCf = year["CashFlow"]
        AnnualResponse[count]["CashFlow"] = {}
        AnnualResponse[count]["CashFlow"] = {
        **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "OperatingCashFlow", "Operating Cash Flow",True)
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "CashFlowFromContinuingOperatingActivities", "Cash from Continuing Operating Activities",True)
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "NetIncomeFromContinuingOperations", "Net Income",True)  # tab
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "OperatingGainsLosses", "Operating Gains Losses",True)
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "DepreciationAmortizationDepletion", "Depreciation Amortization Depletion",True)
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "DeferredTax", "Deferred Tax",True)
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "AmortizationOfFinancingCostsAndDiscounts", "Amortization of Financing Costs and Discounts",True)
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "AmortizationOfSecurities", "Amortization of Securities",True)
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "AssetImpairmentCharge", "Asset Impairment Charge",True)
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "ProvisionandWriteOffofAssets", "Provision and Write Off of Assets",True)
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "UnrealizedGainLossOnInvestmentSecuritites", "Unrealized GainLossOnInvestmentSecuritites",True)
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "StockBasedCompensation", "Stock Based Compensation",True)
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "ExcessTaxBenefitFromStockBasedCompensation", "Excess Tax Benefit from Stock Based Compensation",True)
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "ProvisionForLoanLeaseAndOtherLosses", "Provision for Loan Lease and Other Losses",True)
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "OtherNonCashItems", "Other Non Cash Items",True)
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "ChangeInWorkingCapital", "Changes in Operating Assets and Liabilities",True)
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "ChangeInReceivables", "Receivables",True)  # tab
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "ChangeInInventory", "Inventory",True)
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "ChangeInPrepaidAssets", "Prepaid Assets",True)
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "ChangeInPayablesAndAccruedExpense", "Payables and Accrued Expense",True)
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "ChangeInOtherCurrentAssets", "Other Current Assets",True)
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "ChangeInOtherCurrentLiabilities", "Other Current Liabilities",True)
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "ChangeInOtherWorkingCapital", "Other Working Capital",True)  # untab
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "DividendPaidCFO", "DividendPaidCFO",True)
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "DividendReceivedCFO", "Dividend Received CFO",True)
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "InterestPaidCFO", "Interest Paid CFO",True)
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "InterestReceivedCFO", "Interest Received CFO",True)
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "TaxesRefundPaid", "Taxes Refund Paid",True)  # untab
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "CashFromDiscontinuedOperatingActivities", "Cash from Discontinued Operating Activities",True)
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "InvestingCashFlow", "Investing Cash Flow",True)
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "CashFlowFromContinuingInvestingActivities", "Cash from Continuing Investing Activities",True)
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "CapitalExpenditureReported", "Capital Expenditure Reported",True)
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "ProceedsPaymentFederalFundsSoldAndSecuritiesPurchasedUnderAgreementToResell",
                         "Federal Funds Sold and Securities Purchased Under Agreement to Resell",True)  # financials
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "ProceedsPaymentInInterestBearingDepositsInBank", "Interest Bearing Deposits in Bank",True)  # financials
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "NetPPEPurchaseAndSale", "Net PPE Purchase and Sale",True)
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "PurchaseOfPPE", "Purchase Of PPE",True)
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "SaleOfPPE", "Sale of PPE",True)
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "NetBusinessPurchaseAndSale", "Net Business Purchase and Sale",True)
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "NetInvestmentPropertiesPurchaseAndSale", "Net Investment Properties Purchase and Sale",True)
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "NetInvestmentPurchaseAndSale", "Net Investment Purchase and Sale",True)
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "NetProceedsPaymentForLoan", "Net Proceeds Payment for Loan",True)  # financials
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "DividendsReceivedCFI", "Dividends Received CFI",True)
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "InterestsReceivedCFI", "Interests Received CFI",True)
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "NetOtherInvestingChanges", "Net Other Investing Changes",True)
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "CashFromDiscontinuedInvestingActivities", "Cash from Discontinued Investing Activities",True)
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "FinancingCashFlow", "Financing Cash Flow",True)
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "CashFlowFromContinuingFinancingActivities", "Cash from Continuing Financing Activities",True)
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "ChangeInFederalFundsAndSecuritiesSoldForRepurchase", "Federal Funds and Securities Sold",True)  # financials
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "IncreaseDecreaseInDeposit", "Increase Decrease in Deposit",True)  # financials
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "NetIssuancePaymentsOfDebt", "Net Issuance Payments of Debt",True)
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "NetLongTermDebtIssuance", "Net Long Term Debt Issuance",True)  # tab
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "LongTermDebtIssuance", "Long Term Debt Issuance",True)
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "LongTermDebtPayments", "Long Term Debt Payments",True)  # untab
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "NetShortTermDebtIssuance", "Net Short Term Debt Issuance",True)  # tab
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "ShortTermDebtIssuance", "Short Term Debt Issuance",True)
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "ShortTermDebtPayments", "Short Term Debt Payments",True)
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "NetCommonStockIssuance", "Net Common Stock Issuance",True)
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "CommonStockIssuance", "Common Stock Issuance",True)
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "CommonStockPayments", "Common Stock Payments",True)
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "NetPreferredStockIssuance", "Net Preferred Stock Issuance",True)
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "CashDividendsPaid", "Cash Dividends Paid",True)
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "ProceedsFromStockOptionExercised", "Proceeds from Stock Option Exercised",True)
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "InterestPaidCFF", "Interest Paid CFF",True)
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "NetOtherFinancingCharges", "Net Other Financing Charges",True)
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "CashFromDiscontinuedFinancingActivities", "Cash from Discontinued Financing Activities",True)
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "CashFlowFromDiscontinuedOperation", "Cash Flow from Discontinued Operation",True)
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "OtherCashAdjustmentInsideChangeInCash", "Other Cash Adjustment Inside Change In Cash",True)
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "BeginningCashPosition", "Beginning Cash Position",True)
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "ChangesInCash", "Net Change in Cash",True)
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "EndCashPosition", "End Cash Position",True)
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "IncomeTaxPaidSupplementalData", "Income Tax Paid, Supplemental",True)
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "InterestPaidSupplementalData", "Interest Paid, Supplemental",True)
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "CapitalExpenditure", "Capital Expenditure",True)}

    firstFormat = {
        k: [d.get(k) for d in AnnualResponse]
        for k in set().union(*AnnualResponse)
    }
    from collections import defaultdict, ChainMap
    incomeStatement = defaultdict(list)

    for d in firstFormat["IncomeStatement"]:
        for k, v in d.items():
            incomeStatement[k].insert(0, v)

    balanceSheet = defaultdict(list)

    for d in firstFormat["BalanceSheet"]:
        for k, v in d.items():
            balanceSheet[k].insert(0, v)

    cashFlow = defaultdict(list)

    for d in firstFormat["CashFlow"]:
        for k, v in d.items():
            cashFlow[k].insert(0, v)

    formattedAnnualResponse = ChainMap(firstFormat["reportDate"][::-1], incomeStatement, balanceSheet, cashFlow)
    return json.dumps(formattedAnnualResponse.maps)


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
        ('token', TokenResponse['token']),

    )

    SummaryResponse = requests.get('https://app.quotemedia.com/datatool/getEnhancedQuotes.json', headers=headers,
                                   params=params).json()
    return json.dumps(SummaryResponse)


def checkJsonKey(annualResponse, statement, json_data, json_keyname, NewKeyname, formatNumber):
    boolkey = json_keyname in json_data
    if boolkey is True:
        if formatNumber is True:
            value = (json_data[json_keyname])/1000000
            decimalValue = value - int(value)
            if decimalValue == 0:
                return {NewKeyname: '{:,}'.format(int(value))}
            else:
                value = round(value,2)
                return {NewKeyname: '{:,}'.format(value)}
        else:
            value = round(float(json_data[json_keyname]),2)
            return {NewKeyname: value}
    else:
        for year in annualResponse:
            for key in year[statement]:
                if key == json_keyname or key == NewKeyname:
                    return {NewKeyname: "-"}

    boolkey = json_keyname in json_data
    if boolkey is False:
        return {}

print(scarpTmxAnnual("aapl"))
print(scarpTmxQuarter("aapl"))
