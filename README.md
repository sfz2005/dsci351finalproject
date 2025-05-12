# DSCI 351 Final Project: QuantDB - Natural Language Interface for Financial Market Analysis

QuantDB is a command-line application that allows users to interact with structured financial data using natural language. By using OpenAI’s GPT-3.5 model, user input in plain English is translated into SQL queries, executed on a MySQL database, and the results are displayed in a readable tabular format.

## Prerequisites
Make sure you have the following installed:
1. Python 3.8
2. MySQL Server running locally on an EC2 Instance
3. OpenAI API Key via https://platform.openai.com/api-keys (See where to put the API key in step 7 of the instructions below)

## Setup Instructions
1. Download all five datasets from 'data' directory and all .py files from the other directories.
2. Put all datasets and code files in one directory in the terminal.
3. Create three MySQL databases named quantdb, esgdb, and macrodb.
4. quantdb tables:
sql
Copy
Edit
USE quantdb;

CREATE TABLE companies (
  ticker VARCHAR(10) NOT NULL PRIMARY KEY,
  name VARCHAR(100),
  sector VARCHAR(50),
  industry VARCHAR(100),
  exchange VARCHAR(20),
  city VARCHAR(50),
  state VARCHAR(50),
  country VARCHAR(50)
);

CREATE TABLE company_growth (
  ticker VARCHAR(10) NOT NULL PRIMARY KEY,
  revenue_growth FLOAT,
  employees INT,
  FOREIGN KEY (ticker) REFERENCES companies(ticker)
);

CREATE TABLE financials (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  ticker VARCHAR(10),
  price FLOAT,
  pe_ratio FLOAT,
  dividend_yield FLOAT,
  eps FLOAT,
  week52_low FLOAT,
  week52_high FLOAT,
  market_cap VARCHAR(30),
  ebitda VARCHAR(30),
  price_to_sales FLOAT,
  price_to_book FLOAT,
  FOREIGN KEY (ticker) REFERENCES companies(ticker)
);
esgdb tables:
sql
Copy
Edit
USE esgdb;

CREATE TABLE esg_scores (
  ticker VARCHAR(10) NOT NULL PRIMARY KEY,
  name VARCHAR(100),
  sector VARCHAR(50),
  industry VARCHAR(100),
  total_esg_score FLOAT,
  environment_risk_score FLOAT,
  social_risk_score FLOAT,
  governance_risk_score FLOAT,
  esg_risk_percentile FLOAT,
  esg_risk_level VARCHAR(30)
);

CREATE TABLE esg_controversies (
  ticker VARCHAR(10) NOT NULL PRIMARY KEY,
  controversy_level VARCHAR(30),
  controversy_score FLOAT,
  description TEXT,
  address VARCHAR(150),
  fulltime_employees INT,
  FOREIGN KEY (ticker) REFERENCES esg_scores(ticker)
);
macrodb tables:
sql
Copy
Edit
USE macrodb;

CREATE TABLE economic_indicators (
  record_id VARCHAR(8) NOT NULL PRIMARY KEY,
  date DATE,
  gdp_growth FLOAT,
  inflation_rate FLOAT,
  interest_rate FLOAT
);

CREATE TABLE global_factors (
  record_id VARCHAR(8) NOT NULL PRIMARY KEY,
  date DATE,
  crude_oil_price FLOAT,
  gold_price FLOAT,
  retail_sales_billion FLOAT
);

CREATE TABLE market_activity (
  record_id VARCHAR(8) NOT NULL PRIMARY KEY,
  date DATE,
  stock_index VARCHAR(50),
  close_price FLOAT,
  trading_volume BIGINT
);
5. Create and activate a virtual environment
`python -m venv venv`
`source venv/bin/activate`
6. Install dependencies
`pip install -r requirements.txt`
7. Load data using the scripts in 'data_loading' directory
eg. `python load_companies.py`
8. Add your OpenAI API key in 'conv_quantdb.py', 'conv_esgdb.py', and 'conv_macrodb.py'
- Look for this line: `os.environ["OPENAI_API_KEY"] = "your_openai_api_key"`
8. Run the system by entering:
- eg.`python3 query_quantdb.py` from the 'query_interface' directory
- You'll see: '❓Ask me a question (or type 'exit'):'
- Type a query like: 'Show me the tables in the database.'
- You'll receive the translated SQL and tabular results.
