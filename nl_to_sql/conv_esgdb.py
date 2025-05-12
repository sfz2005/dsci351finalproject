from openai import OpenAI
import os

os.environ["OPENAI_API_KEY"] = "your_openai_api_key"

client = OpenAI()

def nl_to_sql(prompt):
    system = """You are a helpful assistant that translates natural language into SQL.
The database has two tables:
1. esg_scores(ticker, name, sector, industry, total_esg_score, environment_risk_score, social_risk_score, governance_risk_score, esg_risk_percentile, esg_risk_level)
2. esg_controversies(ticker, controversy_level, controversy_score, description, address, fulltime_employees)
Also support natural language instructions for modifying data:
- INSERT: "Add a new ESG score record for Apple"
- DELETE: "Delete the ESG controversy record for Tesla"
- UPDATE: "Update the total ESG risk score for Amazon to 20.5"
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
