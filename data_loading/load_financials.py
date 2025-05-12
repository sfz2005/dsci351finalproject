import pandas as pd
import sqlalchemy

# Load both datasets
financials = pd.read_csv("financials.csv")
companies = pd.read_sql("SELECT ticker FROM companies", sqlalchemy.create_engine('mysql+pymysql://root:Dsci-351@localhost/quantdb'))

# Filter only matching tickers
valid_tickers = set(companies["ticker"])
financials = financials[financials["ticker"].isin(valid_tickers)]

financials = financials[['ticker', 'price', 'pe_ratio', 'dividend_yield', 'eps',
                         'week52_low', 'week52_high', 'market_cap', 'ebitda',
                         'price_to_sales', 'price_to_book']]

# Insert into MySQL
engine = sqlalchemy.create_engine('mysql+pymysql://root:Dsci-351@localhost/quantdb')
financials.to_sql("financials", con=engine, if_exists="append", index=False)

print("✅ Clean financials inserted successfully!")