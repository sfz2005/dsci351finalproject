from openai import OpenAI
import os

os.environ["OPENAI_API_KEY"] = "your_open_api_key"

client = OpenAI()

def nl_to_sql(prompt):
    system = """You are a helpful assistant that translates natural language into SQL. 
The database has three tables: 
1. companies(ticker, name, sector, industry, exchange, city, state, country) 
2. financials(id, ticker, price, pe_ratio, dividend_yield, eps, week52_low, week52_high, market_cap, ebitda, price_to_sales, price_to_book) 
3. company_growth(ticker, revenue_growth, employees)
Also support natural language instructions for modifying data:
- INSERT: "Add a company named Tesla in California"
- DELETE: "Delete the company with ticker XYZ"
- UPDATE: "Update the revenue growth for Apple to 0.25"
"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2,
    )

    return response.choices[0].message.content.strip()
