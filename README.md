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
4. Create and activate a virtual environment
`python -m venv venv`
`source venv/bin/activate`
5. Install dependencies
`pip install -r requirements.txt`
6. Load data using the scripts in 'data_loading' directory
eg. `python load_companies.py`
7. Add your OpenAI API key in 'conv_quantdb.py', 'conv_esgdb.py', and 'conv_macrodb.py'
Look for this line: `os.environ["OPENAI_API_KEY"] = "your_openai_api_key"`
8. Run the system by entering:
eg.`python3 query_quantdb.py` from the 'query_interface' directory
You'll see: '❓Ask me a question (or type 'exit'):'
Type a query like: 'Show me the tables in the database.'
You'll receive the translated SQL and tabular results.
