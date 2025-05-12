import pandas as pd
import sqlalchemy
import pymysql

# Step 1: Read CSV
df = pd.read_csv('macro.csv')

# Step 2: Create a shared key
df['record_id'] = pd.to_datetime(df['Date']).dt.strftime('%Y%m%d')
df['date'] = pd.to_datetime(df['Date'])

# Step 3: Split into three simplified tables

# --- Market Activity Table ---
market_activity = df[['record_id', 'date', 'Stock Index', 'Close Price', 'Trading Volume']].copy()
market_activity.columns = ['record_id', 'date', 'stock_index', 'close_price', 'trading_volume']

# --- Economic Indicators Table ---
economic_indicators = df[['record_id', 'date', 'GDP Growth (%)', 'Inflation Rate (%)', 'Interest Rate (%)']].copy()
economic_indicators.columns = ['record_id', 'date', 'gdp_growth', 'inflation_rate', 'interest_rate']

# --- Global Factors Table ---
global_factors = df[['record_id', 'date', 'Crude Oil Price (USD per Barrel)', 'Gold Price (USD per Ounce)', 'Retail Sales (Billion USD)']].copy()
global_factors.columns = ['record_id', 'date', 'crude_oil_price', 'gold_price', 'retail_sales_billion']

# Step 4: Handle NaNs
market_activity = market_activity.where(pd.notnull(market_activity), None)
economic_indicators = economic_indicators.where(pd.notnull(economic_indicators), None)
global_factors = global_factors.where(pd.notnull(global_factors), None)

# Step 5: Connect to MySQL
engine = sqlalchemy.create_engine('mysql+pymysql://root:Dsci-351@localhost/macrodb')

# Step 6: Clear previous data if rerunning (optional)
with engine.begin() as conn:
    conn.execute("DELETE FROM global_factors")
    conn.execute("DELETE FROM economic_indicators")
    conn.execute("DELETE FROM market_activity")

# Step 7: Upload to MySQL
market_activity.to_sql('market_activity', con=engine, if_exists='append', index=False)
economic_indicators.to_sql('economic_indicators', con=engine, if_exists='append', index=False)
global_factors.to_sql('global_factors', con=engine, if_exists='append', index=False)

