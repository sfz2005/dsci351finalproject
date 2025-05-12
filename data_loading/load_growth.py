import pandas as pd
import sqlalchemy

# Load both datasets
growth = pd.read_csv("company_growth.csv")
companies = pd.read_sql("SELECT ticker FROM companies", sqlalchemy.create_engine('mysql+pymysql://root:Dsci-351@localhost/quantdb'))

# Filter only matching tickers
valid_tickers = set(companies["ticker"])
growth = growth[growth["ticker"].isin(valid_tickers)]

# Keep only the necessary columns
growth = growth[['ticker', 'revenue_growth', 'employees']]

# Insert into MySQL
engine = sqlalchemy.create_engine("mysql+pymysql://root:Dsci-351@localhost/quantdb")
growth.to_sql("company_growth", con=engine, if_exists="append", index=False)

print("✅ Clean company_growth inserted successfully!")