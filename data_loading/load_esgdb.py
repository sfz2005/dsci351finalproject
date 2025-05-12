import pandas as pd
import sqlalchemy
import pymysql

# Step 1: Read CSV
df = pd.read_csv('risk_ratings.csv')

# Step 2a: Prepare esg_scores table
esg_scores = df[['Symbol', 'Name', 'Sector', 'Industry', 'Total ESG Risk score',
                 'Environment Risk Score', 'Social Risk Score', 'Governance Risk Score',
                 'ESG Risk Percentile', 'ESG Risk Level']].copy()

esg_scores.columns = ['ticker', 'name', 'sector', 'industry', 'total_esg_score',
                      'environment_risk_score', 'social_risk_score', 'governance_risk_score',
                      'esg_risk_percentile', 'esg_risk_level']

# Convert "50th percentile" → 50.0
esg_scores['esg_risk_percentile'] = (
    esg_scores['esg_risk_percentile']
    .str.extract(r'(\d+)', expand=False)
    .astype(float)
)

# Clean NaNs
esg_scores = esg_scores.where(pd.notnull(esg_scores), None)

# Step 2b: Prepare esg_controversies table
esg_controversies = df[['Symbol', 'Controversy Level', 'Controversy Score', 'Description',
                        'Address', 'Full Time Employees']].copy()

esg_controversies.columns = ['ticker', 'controversy_level', 'controversy_score', 'description',
                             'address', 'fulltime_employees']

# Fix "12,000" → 12000
esg_controversies['fulltime_employees'] = (
    esg_controversies['fulltime_employees']
    .str.replace(',', '')
    .astype(float)
)

# Clean NaNs
esg_controversies = esg_controversies.where(pd.notnull(esg_controversies), None)

# Step 3: MySQL connection to esgdb
engine = sqlalchemy.create_engine('mysql+pymysql://root:Dsci-351@localhost/esgdb')

# Step 4: Upload to MySQL
esg_scores.to_sql('esg_scores', con=engine, if_exists='append', index=False)
esg_controversies.to_sql('esg_controversies', con=engine, if_exists='append', index=False)
