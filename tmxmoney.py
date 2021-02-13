import requests
import json

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
        **checkJsonKey(QuarterlyResponse, "IncomeStatement", currentQuarterIs, "TotalRevenue", "Total Revenue")
        , **checkJsonKey(QuarterlyResponse, "IncomeStatement", currentQuarterIs, "CostOfRevenue", "Cost of Revenue")
        , **checkJsonKey(QuarterlyResponse, "IncomeStatement", currentQuarterIs, "NetInterestIncome", "Net Interest Income")  # financials
        , **checkJsonKey(QuarterlyResponse, "IncomeStatement", currentQuarterIs, "NonInterestIncome", "Non Interest Income")  # financials
        , **checkJsonKey(QuarterlyResponse, "IncomeStatement", currentQuarterIs, "CreditLossesProvision", "Credit Losses Provision")  # financials
        , **checkJsonKey(QuarterlyResponse, "IncomeStatement", currentQuarterIs, "NonInterestExpense", "Non Interest Expense")  # financials
        , **checkJsonKey(QuarterlyResponse, "IncomeStatement", currentQuarterIs, "GrossProfit", "Gross Profit")
        , **checkJsonKey(QuarterlyResponse, "IncomeStatement", currentQuarterIs, "OperatingExpense", "Operating Expense")
        , **checkJsonKey(QuarterlyResponse, "IncomeStatement", currentQuarterIs, "OccupancyAndEquipment", "Occupancy and Equipment")  # financials
        , **checkJsonKey(QuarterlyResponse, "IncomeStatement", currentQuarterIs, "SellingGeneralAndAdministration", "Selling, General and Administration")
        , **checkJsonKey(QuarterlyResponse, "IncomeStatement", currentQuarterIs, "ResearchAndDevelopment", "Research and Development")
        , **checkJsonKey(QuarterlyResponse, "IncomeStatement", currentQuarterIs, "DepreciationAndAmortization", "Depreciation and Amortization")
        , **checkJsonKey(QuarterlyResponse, "IncomeStatement", currentQuarterIs, "Depletion", "Depletion")  # financials
        , **checkJsonKey(QuarterlyResponse, "IncomeStatement", currentQuarterIs, "SecuritiesAmortization", "Securities Amortization")  # financials
        , **checkJsonKey(QuarterlyResponse, "IncomeStatement", currentQuarterIs, "OtherNonInterestExpense", "Other Non Interest Expense")  # financials
        , **checkJsonKey(QuarterlyResponse, "IncomeStatement", currentQuarterIs, "IncomefromAssociatesandOtherParticipatingInterests", "Income from Associates and Other Participating Interests")
        # financials
        , **checkJsonKey(QuarterlyResponse, "IncomeStatement", currentQuarterIs, "OperatingIncome", "Operating Income")
        , **checkJsonKey(QuarterlyResponse, "IncomeStatement", currentQuarterIs, "NetNonOperatingInterestIncomeExpense", "Net Interest")
        , **checkJsonKey(QuarterlyResponse, "IncomeStatement", currentQuarterIs, "OtherIncomeExpense", "Other Income Expense")
        , **checkJsonKey(QuarterlyResponse, "IncomeStatement", currentQuarterIs, "PretaxIncome", "Income before Tax")
        , **checkJsonKey(QuarterlyResponse, "IncomeStatement", currentQuarterIs, "TaxProvision", "Provision for Income Tax")
        , **checkJsonKey(QuarterlyResponse, "IncomeStatement", currentQuarterIs, "NetIncome", "Net Income")
        , **checkJsonKey(QuarterlyResponse, "IncomeStatement", currentQuarterIs, "NetIncomeCommonStockholders", "Net Income Common Shareholders")
        , **checkJsonKey(QuarterlyResponse, "IncomeStatement", currentQuarterIs, "BasicEPS", "Basic EPS")
        , **checkJsonKey(QuarterlyResponse, "IncomeStatement", currentQuarterIs, "DilutedEPS", "Diluted EPS")
        , **checkJsonKey(QuarterlyResponse, "IncomeStatement", currentQuarterIs, "BasicAverageShares", "Basic Average Shares Outstanding")
        , **checkJsonKey(QuarterlyResponse, "IncomeStatement", currentQuarterIs, "DilutedAverageShares", "Diluted Average Shares Outstanding")
        , **checkJsonKey(QuarterlyResponse, "IncomeStatement", currentQuarterIs, "DividendPerShare", "Dividend Per Share")
        , **checkJsonKey(QuarterlyResponse, "IncomeStatement", currentQuarterIs, "EBIT", "EBIT")
        , **checkJsonKey(QuarterlyResponse, "IncomeStatement", currentQuarterIs, "EBITDA", "EBITDA")}

        currentQuarterBs = quarter["BalanceSheet"]
        QuarterlyResponse[count]["BalanceSheet"] = {}
        QuarterlyResponse[count]["BalanceSheet"] = {
        **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "TotalAssets", "Total Assets")
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "CurrentAssets", "Current Assets")
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "CashAndCashEquivalents", "Cash and Cash Equivalents")
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "ShortTermInvestments", "Short Term Investments")
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "RestrictedCashAndInvestments", "Restricted Cash and Investments")  # financials
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "MoneyMarketInvestments", "Money Market Investments")  # financials
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "SecuritiesAndInvestments", "Securities and Investments")  # financials
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "NetLoan", "Net Loan")  # financials
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "Receivables", "Receivables")
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "Inventory", "Inventory")
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "PrepaidAssets", "Prepaid Assets")
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "RestrictedCash", "Restricted Cash")
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "AssetHeldForSaleCurrent", "Asset Held for Sale Current")
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "HedgingAssetsCurrent", "Hedging Assets Current")
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "OtherCurrentAssets", "Other Current Assets")
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "TotalNonCurrentAssets", "Total Non Current Assets")
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "NetPPE", "Net PPE")
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "GrossPPE", "Gross PPE")  # tab
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "AccumulatedDepreciation", "Accumulated Depreciation")
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "Goodwill", "Goodwill")
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "OtherIntangibleAssets", "Intangible Assets")
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "InvestmentAndAdvances", "Investment And Advances")
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "FinancialAssets", "Financial Assets")
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "NonCurrentAccountsReceivable", "Non Current Accounts Receivable")
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "NonCurrentNoteReceivables", "Non Current Note Receivable")
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "DueFromRelatedPartiesNonCurrent", "Due From Related Parties Non Current")
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "NonCurrentDeferredAssets", "Non Current Deferred Assets")
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "NonCurrentPrepaidAssets", "Non Current Deferred Assets")
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "DeferredAssets", "Deferred Assets")  # financials
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "DefinedPensionBenefit", "Defined Pension Benefit")
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "OtherNonCurrentAssets", "Other Non Current Assets")
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "AssetsHeldForSale", "AssetsHeldForSale")  # financials
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "OtherAssets", "Other Assets")  # financials
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "TotalLiabilities", "Total Liabilities")
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "TotalDeposits", "Total Deposits")  # financials
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "FederalFundsPurchasedAndSecuritiesSoldUnderAgreementToRepurchase",
                         "Federal Funds Purchased and Securities Sold Under Agreement to Repurchase")  # financials
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "SecuritiesLoaned", "SecuritiesLoaned")  # financials
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "TradingLiabilities", "Trading Liabilities")  # financials
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "SecuritiesLoaned", "SecuritiesLoaned")  # financials
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "CurrentLiabilities", "Current Liabilities")
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "PayablesAndAccruedExpenses", "Payables and Accrued Expenses")
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "CurrentProvisions", "Current Provisions")
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "PensionandOtherPostRetirementBenefitPlansCurrent", "Pension and Other Post Retirement Benefit Plans Current")
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "CurrentDebtAndCapitalLeaseObligation", "Current Debt and Capital Lease Obligation")
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "CurrentDeferredLiabilities", "Current Deferred Liabilities")
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "OtherCurrentLiabilities", "Other Current Liabilities")
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "TotalNonCurrentLiabilities", "Total Non Current Liabilities")
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "LongTermProvisions", "Long Term Provisions")
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "LongTermDebtAndCapitalLeaseObligation", "Long Term Debt and Capital Lease Obligation")
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "NonCurrentDeferredLiabilities", "NonCurrentDeferredLiabilities")
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "TradeandOtherPayablesNonCurrent", "Trade and Other Payables Non Current")
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "DuetoRelatedPartiesNonCurrent", "Dueto Related Parties Non Current")
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "NonCurrentAccruedExpenses", "Non Current Accrued Expenses")
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "EmployeeBenefits", "Employee Benefits")
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "DerivativeProductLiabilities", "Derivative Product Liabilities")
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "PreferredSecuritiesOutsideStockEquity", "Preferred Securities Outside Stock Equity")
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "RestrictedCommonStock", "Restricted Common Stock")
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "LiabilitiesHeldforSaleNonCurrent", "Liabilities Held for Sale Non Current")
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "OtherNonCurrentLiabilities", "Other Non Current Liabilities")
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "LiabilitiesOfDiscontinuedOperations", "Liabilities of Discontinued Operations")  # financials
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "OtherLiabilities", "Other Liabilities")  # financials
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "TotalEquityGrossMinority", "Total Equity")
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "StockholdersEquity", "Stockholders Equity")
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "CapitalStock", "Capital Stock")  # tab
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "AdditionalPaidInCapital", "Additional Paid in Capital")
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "RetainedEarnings", "Retained Earnings")
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "TreasuryStock", "Treasury Stock")
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "GainsLossesNotAffectingRetainedEarnings", "Reserves/Accumulated Comprehensive Income/Losse")
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "OtherEquityInterest", "Other Equity Interest")
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "MinorityInterest", "Minority Interest")
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "TotalCapitalization", "Total Capitalization")
        , **checkJsonKey(QuarterlyResponse, "BalanceSheet", currentQuarterBs, "CapitalLeaseObligations", "Capital Lease Obligations")}

        currentQuarterCf = quarter["CashFlow"]
        QuarterlyResponse[count]["CashFlow"] = {}
        QuarterlyResponse[count]["CashFlow"] = {
        **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "OperatingCashFlow", "Operating Cash Flow")
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "CashFlowFromContinuingOperatingActivities", "Cash from Continuing Operating Activities")
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "NetIncomeFromContinuingOperations", "Net Income")  # tab
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "OperatingGainsLosses", "Operating Gains Losses")
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "DepreciationAmortizationDepletion", "Depreciation Amortization Depletion")
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "DeferredTax", "Deferred Tax")
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "AmortizationOfFinancingCostsAndDiscounts", "Amortization of Financing Costs and Discounts")
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "AmortizationOfSecurities", "Amortization of Securities")
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "AssetImpairmentCharge", "Asset Impairment Charge")
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "ProvisionandWriteOffofAssets", "Provision and Write Off of Assets")
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "UnrealizedGainLossOnInvestmentSecuritites", "Unrealized GainLossOnInvestmentSecuritites")
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "StockBasedCompensation", "Stock Based Compensation")
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "ExcessTaxBenefitFromStockBasedCompensation", "Excess Tax Benefit from Stock Based Compensation")
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "ProvisionForLoanLeaseAndOtherLosses", "Provision for Loan Lease and Other Losses")
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "OtherNonCashItems", "Other Non Cash Items")
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "ChangeInWorkingCapital", "Changes in Operating Assets and Liabilities")
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "ChangeInReceivables", "Receivables")  # tab
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "ChangeInInventory", "Inventory")
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "ChangeInPrepaidAssets", "Prepaid Assets")
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "ChangeInPayablesAndAccruedExpense", "Payables and Accrued Expense")
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "ChangeInOtherCurrentAssets", "Other Current Assets")
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "ChangeInOtherCurrentLiabilities", "Other Current Liabilities")
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "ChangeInOtherWorkingCapital", "Other Working Capital")  # untab
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "DividendPaidCFO", "DividendPaidCFO")
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "DividendReceivedCFO", "Dividend Received CFO")
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "InterestPaidCFO", "Interest Paid CFO")
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "InterestReceivedCFO", "Interest Received CFO")
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "TaxesRefundPaid", "Taxes Refund Paid")  # untab
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "CashFromDiscontinuedOperatingActivities", "Cash from Discontinued Operating Activities")
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "InvestingCashFlow", "Investing Cash Flow")
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "CashFlowFromContinuingInvestingActivities", "Cash from Continuing Investing Activities")
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "CapitalExpenditureReported", "Capital Expenditure Reported")
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "ProceedsPaymentFederalFundsSoldAndSecuritiesPurchasedUnderAgreementToResell",
                         "Federal Funds Sold and Securities Purchased Under Agreement to Resell")  # financials
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "ProceedsPaymentInInterestBearingDepositsInBank", "Interest Bearing Deposits in Bank")  # financials
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "NetPPEPurchaseAndSale", "Net PPE Purchase and Sale")
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "PurchaseOfPPE", "Purchase Of PPE")
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "SaleOfPPE", "Sale of PPE")
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "NetBusinessPurchaseAndSale", "Net Business Purchase and Sale")
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "NetInvestmentPropertiesPurchaseAndSale", "Net Investment Properties Purchase and Sale")
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "NetInvestmentPurchaseAndSale", "Net Investment Purchase and Sale")
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "NetProceedsPaymentForLoan", "Net Proceeds Payment for Loan")  # financials
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "DividendsReceivedCFI", "Dividends Received CFI")
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "InterestsReceivedCFI", "Interests Received CFI")
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "NetOtherInvestingChanges", "Net Other Investing Changes")
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "CashFromDiscontinuedInvestingActivities", "Cash from Discontinued Investing Activities")
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "FinancingCashFlow", "Financing Cash Flow")
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "CashFlowFromContinuingFinancingActivities", "Cash from Continuing Financing Activities")
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "ChangeInFederalFundsAndSecuritiesSoldForRepurchase", "Federal Funds and Securities Sold")  # financials
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "IncreaseDecreaseInDeposit", "Increase Decrease in Deposit")  # financials
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "NetIssuancePaymentsOfDebt", "Net Issuance Payments of Debt")
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "NetLongTermDebtIssuance", "Net Long Term Debt Issuance")  # tab
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "LongTermDebtIssuance", "Long Term Debt Issuance")
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "LongTermDebtPayments", "Long Term Debt Payments")  # untab
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "NetShortTermDebtIssuance", "Net Short Term Debt Issuance")  # tab
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "ShortTermDebtIssuance", "Short Term Debt Issuance")
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "ShortTermDebtPayments", "Short Term Debt Payments")
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "NetCommonStockIssuance", "Net Common Stock Issuance")
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "CommonStockIssuance", "Common Stock Issuance")
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "CommonStockPayments", "Common Stock Payments")
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "NetPreferredStockIssuance", "Net Preferred Stock Issuance")
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "CashDividendsPaid", "Cash Dividends Paid")
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "ProceedsFromStockOptionExercised", "Proceeds from Stock Option Exercised")
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "InterestPaidCFF", "Interest Paid CFF")
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "NetOtherFinancingCharges", "Net Other Financing Charges")
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "CashFromDiscontinuedFinancingActivities", "Cash from Discontinued Financing Activities")
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "CashFlowFromDiscontinuedOperation", "Cash Flow from Discontinued Operation")
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "OtherCashAdjustmentInsideChangeInCash", "Other Cash Adjustment Inside Change In Cash")
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "BeginningCashPosition", "Beginning Cash Position")
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "ChangesInCash", "Net Change in Cash")
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "EndCashPosition", "End Cash Position")
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "IncomeTaxPaidSupplementalData", "Income Tax Paid, Supplemental")
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "InterestPaidSupplementalData", "Interest Paid, Supplemental")
        , **checkJsonKey(QuarterlyResponse, "CashFlow", currentQuarterCf, "CapitalExpenditure", "Capital Expenditure")}




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
        **checkJsonKey(AnnualResponse, "IncomeStatement", currentYearIs, "TotalRevenue", "Total Revenue")
        , **checkJsonKey(AnnualResponse, "IncomeStatement", currentYearIs, "CostOfRevenue", "Cost of Revenue")
        , **checkJsonKey(AnnualResponse, "IncomeStatement", currentYearIs, "NetInterestIncome", "Net Interest Income")  # financials
        , **checkJsonKey(AnnualResponse, "IncomeStatement", currentYearIs, "NonInterestIncome", "Non Interest Income")  # financials
        , **checkJsonKey(AnnualResponse, "IncomeStatement", currentYearIs, "CreditLossesProvision", "Credit Losses Provision")  # financials
        , **checkJsonKey(AnnualResponse, "IncomeStatement", currentYearIs, "NonInterestExpense", "Non Interest Expense")  # financials
        , **checkJsonKey(AnnualResponse, "IncomeStatement", currentYearIs, "GrossProfit", "Gross Profit")
        , **checkJsonKey(AnnualResponse, "IncomeStatement", currentYearIs, "OperatingExpense", "Operating Expense")
        , **checkJsonKey(AnnualResponse, "IncomeStatement", currentYearIs, "OccupancyAndEquipment", "Occupancy and Equipment")  # financials
        , **checkJsonKey(AnnualResponse, "IncomeStatement", currentYearIs, "SellingGeneralAndAdministration", "Selling, General and Administration")
        , **checkJsonKey(AnnualResponse, "IncomeStatement", currentYearIs, "ResearchAndDevelopment", "Research and Development")
        , **checkJsonKey(AnnualResponse, "IncomeStatement", currentYearIs, "DepreciationAndAmortization", "Depreciation and Amortization")
        , **checkJsonKey(AnnualResponse, "IncomeStatement", currentYearIs, "Depletion", "Depletion")  # financials
        , **checkJsonKey(AnnualResponse, "IncomeStatement", currentYearIs, "SecuritiesAmortization", "Securities Amortization")  # financials
        , **checkJsonKey(AnnualResponse, "IncomeStatement", currentYearIs, "OtherNonInterestExpense", "Other Non Interest Expense")  # financials
        , **checkJsonKey(AnnualResponse, "IncomeStatement", currentYearIs, "IncomefromAssociatesandOtherParticipatingInterests", "Income from Associates and Other Participating Interests")#financials
        , **checkJsonKey(AnnualResponse, "IncomeStatement", currentYearIs, "OperatingIncome", "Operating Income")
        , **checkJsonKey(AnnualResponse, "IncomeStatement", currentYearIs, "NetNonOperatingInterestIncomeExpense", "Net Interest")
        , **checkJsonKey(AnnualResponse, "IncomeStatement", currentYearIs, "OtherIncomeExpense", "Other Income Expense")
        , **checkJsonKey(AnnualResponse, "IncomeStatement", currentYearIs, "PretaxIncome", "Income before Tax")
        , **checkJsonKey(AnnualResponse, "IncomeStatement", currentYearIs, "TaxProvision", "Provision for Income Tax")
        , **checkJsonKey(AnnualResponse, "IncomeStatement", currentYearIs, "NetIncome", "Net Income")
        , **checkJsonKey(AnnualResponse, "IncomeStatement", currentYearIs, "NetIncomeCommonStockholders", "Net Income Common Shareholders")
        , **checkJsonKey(AnnualResponse, "IncomeStatement", currentYearIs, "BasicEPS", "Basic EPS")
        , **checkJsonKey(AnnualResponse, "IncomeStatement", currentYearIs, "DilutedEPS", "Diluted EPS")
        , **checkJsonKey(AnnualResponse, "IncomeStatement", currentYearIs, "BasicAverageShares", "Basic Average Shares Outstanding")
        , **checkJsonKey(AnnualResponse, "IncomeStatement", currentYearIs, "DilutedAverageShares", "Diluted Average Shares Outstanding")
        , **checkJsonKey(AnnualResponse, "IncomeStatement", currentYearIs, "DividendPerShare", "Dividend Per Share")
        , **checkJsonKey(AnnualResponse, "IncomeStatement", currentYearIs, "EBIT", "EBIT")
        , **checkJsonKey(AnnualResponse, "IncomeStatement", currentYearIs, "EBITDA", "EBITDA")}

        currentYearBs = year["BalanceSheet"]
        AnnualResponse[count]["BalanceSheet"] = {}
        AnnualResponse[count]["BalanceSheet"] = {
        **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "TotalAssets", "Total Assets")
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "CurrentAssets", "Current Assets")
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "CashAndCashEquivalents", "Cash and Cash Equivalents")
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "ShortTermInvestments", "Short Term Investments")
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "RestrictedCashAndInvestments", "Restricted Cash and Investments")  # financials
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "MoneyMarketInvestments", "Money Market Investments")  # financials
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "SecuritiesAndInvestments", "Securities and Investments")  # financials
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "NetLoan", "Net Loan")  # financials
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "Receivables", "Receivables")
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "Inventory", "Inventory")
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "PrepaidAssets", "Prepaid Assets")
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "RestrictedCash", "Restricted Cash")
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "AssetHeldForSaleCurrent", "Asset Held for Sale Current")
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "HedgingAssetsCurrent", "Hedging Assets Current")
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "OtherCurrentAssets", "Other Current Assets")
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "TotalNonCurrentAssets", "Total Non Current Assets")
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "NetPPE", "Net PPE")
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "GrossPPE", "Gross PPE")  # tab
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "AccumulatedDepreciation", "Accumulated Depreciation")
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "Goodwill", "Goodwill")
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "OtherIntangibleAssets", "Intangible Assets")
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "InvestmentAndAdvances", "Investment And Advances")
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "FinancialAssets", "Financial Assets")
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "NonCurrentAccountsReceivable", "Non Current Accounts Receivable")
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "NonCurrentNoteReceivables", "Non Current Note Receivable")
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "DueFromRelatedPartiesNonCurrent", "Due From Related Parties Non Current")
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "NonCurrentDeferredAssets", "Non Current Deferred Assets")
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "NonCurrentPrepaidAssets", "Non Current Deferred Assets")
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "DeferredAssets", "Deferred Assets")  # financials
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "DefinedPensionBenefit", "Defined Pension Benefit")
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "OtherNonCurrentAssets", "Other Non Current Assets")
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "AssetsHeldForSale", "AssetsHeldForSale")  # financials
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "OtherAssets", "Other Assets")  # financials
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "TotalLiabilities", "Total Liabilities")
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "TotalDeposits", "Total Deposits")  # financials
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "FederalFundsPurchasedAndSecuritiesSoldUnderAgreementToRepurchase",
                         "Federal Funds Purchased and Securities Sold Under Agreement to Repurchase")  # financials
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "SecuritiesLoaned", "SecuritiesLoaned")  # financials
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "TradingLiabilities", "Trading Liabilities")  # financials
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "SecuritiesLoaned", "SecuritiesLoaned")  # financials
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "CurrentLiabilities", "Current Liabilities")
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "PayablesAndAccruedExpenses", "Payables and Accrued Expenses")
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "CurrentProvisions", "Current Provisions")
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "PensionandOtherPostRetirementBenefitPlansCurrent", "Pension and Other Post Retirement Benefit Plans Current")
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "CurrentDebtAndCapitalLeaseObligation", "Current Debt and Capital Lease Obligation")
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "CurrentDeferredLiabilities", "Current Deferred Liabilities")
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "OtherCurrentLiabilities", "Other Current Liabilities")
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "TotalNonCurrentLiabilities", "Total Non Current Liabilities")
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "LongTermProvisions", "Long Term Provisions")
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "LongTermDebtAndCapitalLeaseObligation", "Long Term Debt and Capital Lease Obligation")
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "NonCurrentDeferredLiabilities", "NonCurrentDeferredLiabilities")
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "TradeandOtherPayablesNonCurrent", "Trade and Other Payables Non Current")
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "DuetoRelatedPartiesNonCurrent", "Dueto Related Parties Non Current")
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "NonCurrentAccruedExpenses", "Non Current Accrued Expenses")
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "EmployeeBenefits", "Employee Benefits")
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "DerivativeProductLiabilities", "Derivative Product Liabilities")
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "PreferredSecuritiesOutsideStockEquity", "Preferred Securities Outside Stock Equity")
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "RestrictedCommonStock", "Restricted Common Stock")
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "LiabilitiesHeldforSaleNonCurrent", "Liabilities Held for Sale Non Current")
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "OtherNonCurrentLiabilities", "Other Non Current Liabilities")
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "LiabilitiesOfDiscontinuedOperations", "Liabilities of Discontinued Operations")  # financials
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "OtherLiabilities", "Other Liabilities")  # financials
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "TotalEquityGrossMinority", "Total Equity")
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "StockholdersEquity", "Stockholders Equity")
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "CapitalStock", "Capital Stock")  # tab
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "AdditionalPaidInCapital", "Additional Paid in Capital")
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "RetainedEarnings", "Retained Earnings")
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "TreasuryStock", "Treasury Stock")
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "GainsLossesNotAffectingRetainedEarnings", "Reserves/Accumulated Comprehensive Income/Losse")
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "OtherEquityInterest", "Other Equity Interest")
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "MinorityInterest", "Minority Interest")
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "TotalCapitalization", "Total Capitalization")
        , **checkJsonKey(AnnualResponse, "BalanceSheet", currentYearBs, "CapitalLeaseObligations", "Capital Lease Obligations")}

        currentYearCf = year["CashFlow"]
        AnnualResponse[count]["CashFlow"] = {}
        AnnualResponse[count]["CashFlow"] = {
        **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "OperatingCashFlow", "Operating Cash Flow")
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "CashFlowFromContinuingOperatingActivities", "Cash from Continuing Operating Activities")
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "NetIncomeFromContinuingOperations", "Net Income")  # tab
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "OperatingGainsLosses", "Operating Gains Losses")
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "DepreciationAmortizationDepletion", "Depreciation Amortization Depletion")
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "DeferredTax", "Deferred Tax")
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "AmortizationOfFinancingCostsAndDiscounts", "Amortization of Financing Costs and Discounts")
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "AmortizationOfSecurities", "Amortization of Securities")
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "AssetImpairmentCharge", "Asset Impairment Charge")
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "ProvisionandWriteOffofAssets", "Provision and Write Off of Assets")
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "UnrealizedGainLossOnInvestmentSecuritites", "Unrealized GainLossOnInvestmentSecuritites")
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "StockBasedCompensation", "Stock Based Compensation")
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "ExcessTaxBenefitFromStockBasedCompensation", "Excess Tax Benefit from Stock Based Compensation")
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "ProvisionForLoanLeaseAndOtherLosses", "Provision for Loan Lease and Other Losses")
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "OtherNonCashItems", "Other Non Cash Items")
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "ChangeInWorkingCapital", "Changes in Operating Assets and Liabilities")
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "ChangeInReceivables", "Receivables")  # tab
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "ChangeInInventory", "Inventory")
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "ChangeInPrepaidAssets", "Prepaid Assets")
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "ChangeInPayablesAndAccruedExpense", "Payables and Accrued Expense")
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "ChangeInOtherCurrentAssets", "Other Current Assets")
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "ChangeInOtherCurrentLiabilities", "Other Current Liabilities")
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "ChangeInOtherWorkingCapital", "Other Working Capital")  # untab
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "DividendPaidCFO", "DividendPaidCFO")
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "DividendReceivedCFO", "Dividend Received CFO")
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "InterestPaidCFO", "Interest Paid CFO")
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "InterestReceivedCFO", "Interest Received CFO")
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "TaxesRefundPaid", "Taxes Refund Paid")  # untab
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "CashFromDiscontinuedOperatingActivities", "Cash from Discontinued Operating Activities")
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "InvestingCashFlow", "Investing Cash Flow")
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "CashFlowFromContinuingInvestingActivities", "Cash from Continuing Investing Activities")
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "CapitalExpenditureReported", "Capital Expenditure Reported")
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "ProceedsPaymentFederalFundsSoldAndSecuritiesPurchasedUnderAgreementToResell",
                         "Federal Funds Sold and Securities Purchased Under Agreement to Resell")  # financials
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "ProceedsPaymentInInterestBearingDepositsInBank", "Interest Bearing Deposits in Bank")  # financials
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "NetPPEPurchaseAndSale", "Net PPE Purchase and Sale")
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "PurchaseOfPPE", "Purchase Of PPE")
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "SaleOfPPE", "Sale of PPE")
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "NetBusinessPurchaseAndSale", "Net Business Purchase and Sale")
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "NetInvestmentPropertiesPurchaseAndSale", "Net Investment Properties Purchase and Sale")
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "NetInvestmentPurchaseAndSale", "Net Investment Purchase and Sale")
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "NetProceedsPaymentForLoan", "Net Proceeds Payment for Loan")  # financials
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "DividendsReceivedCFI", "Dividends Received CFI")
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "InterestsReceivedCFI", "Interests Received CFI")
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "NetOtherInvestingChanges", "Net Other Investing Changes")
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "CashFromDiscontinuedInvestingActivities", "Cash from Discontinued Investing Activities")
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "FinancingCashFlow", "Financing Cash Flow")
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "CashFlowFromContinuingFinancingActivities", "Cash from Continuing Financing Activities")
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "ChangeInFederalFundsAndSecuritiesSoldForRepurchase", "Federal Funds and Securities Sold")  # financials
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "IncreaseDecreaseInDeposit", "Increase Decrease in Deposit")  # financials
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "NetIssuancePaymentsOfDebt", "Net Issuance Payments of Debt")
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "NetLongTermDebtIssuance", "Net Long Term Debt Issuance")  # tab
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "LongTermDebtIssuance", "Long Term Debt Issuance")
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "LongTermDebtPayments", "Long Term Debt Payments")  # untab
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "NetShortTermDebtIssuance", "Net Short Term Debt Issuance")  # tab
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "ShortTermDebtIssuance", "Short Term Debt Issuance")
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "ShortTermDebtPayments", "Short Term Debt Payments")
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "NetCommonStockIssuance", "Net Common Stock Issuance")
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "CommonStockIssuance", "Common Stock Issuance")
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "CommonStockPayments", "Common Stock Payments")
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "NetPreferredStockIssuance", "Net Preferred Stock Issuance")
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "CashDividendsPaid", "Cash Dividends Paid")
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "ProceedsFromStockOptionExercised", "Proceeds from Stock Option Exercised")
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "InterestPaidCFF", "Interest Paid CFF")
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "NetOtherFinancingCharges", "Net Other Financing Charges")
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "CashFromDiscontinuedFinancingActivities", "Cash from Discontinued Financing Activities")
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "CashFlowFromDiscontinuedOperation", "Cash Flow from Discontinued Operation")
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "OtherCashAdjustmentInsideChangeInCash", "Other Cash Adjustment Inside Change In Cash")
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "BeginningCashPosition", "Beginning Cash Position")
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "ChangesInCash", "Net Change in Cash")
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "EndCashPosition", "End Cash Position")
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "IncomeTaxPaidSupplementalData", "Income Tax Paid, Supplemental")
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "InterestPaidSupplementalData", "Interest Paid, Supplemental")
        , **checkJsonKey(AnnualResponse, "CashFlow", currentYearCf, "CapitalExpenditure", "Capital Expenditure")}

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


def checkJsonKey(annualResponse, statement, json_data, json_keyname, NewKeyname):
    boolkey = json_keyname in json_data
    if boolkey is True:
        return {NewKeyname: json_data[json_keyname]}
    else:
        for year in annualResponse:
            for key in year[statement]:
                if key == json_keyname or key == NewKeyname:
                    return {NewKeyname: "-"}

    boolkey = json_keyname in json_data
    if boolkey is False:
        return {}
