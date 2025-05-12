import pandas as pd
import sqlalchemy
import pymysql

# Step 1: Read CSV
df = pd.read_csv('data/companies.csv')

# Step 2: Filter only needed columns
df = df[['ticker', 'name', 'sector', 'industry', 'exchange', 'city', 'state', 'country']]

# Step 3: Set up connection
engine = sqlalchemy.create_engine('mysql+pymysql://root:Dsci-351@localhost/quantdb')

# Step 4: Load to MySQL
df.to_sql('companies', con=engine, if_exists='append', index=False)
