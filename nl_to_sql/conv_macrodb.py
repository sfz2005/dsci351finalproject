from openai import OpenAI
import os

os.environ["OPENAI_API_KEY"] = "your_openai_api_key"

client = OpenAI()

def nl_to_sql(prompt):
    system = """You are a helpful assistant that translates natural language into SQL.
The database has three tables:
1. market_activity(record_id, date, stock_index, close_price, trading_volume)
2. economic_indicators(record_id, date, gdp_growth, inflation_rate, interest_rate)
3. global_factors(record_id, date, crude_oil_price, gold_price, retail_sales_billion)
Also support natural language instructions for modifying data:
- INSERT: "Add a new market activity record for 2022-01-01"
- DELETE: "Delete the record for 2021-05-01 from economic indicators"
- UPDATE: "Update the gold price for 2023-03-01 to 1900"
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
