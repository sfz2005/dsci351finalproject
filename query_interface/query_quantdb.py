import sqlalchemy
import pandas as pd
from conv_quantdb import nl_to_sql 
import re

# Connect to MySQL
engine = sqlalchemy.create_engine("mysql+pymysql://root:Dsci-351@localhost/quantdb")

def run_nl_query(nl_input):
    print(f"\n🔤Input: {nl_input}")
    sql = nl_to_sql(nl_input).strip()

    # Remove markdown fences and any GPT preamble
    if "```sql" in sql:
        sql = sql.split("```sql")[-1]
    if "```" in sql:
        sql = sql.split("```")[0]
    sql = sql.strip()
    
    

    # Convert: OFFSET 10 LIMIT 5  -->  LIMIT 5 OFFSET 10
    pattern = r"offset\s+(\d+)\s+limit\s+(\d+)"
    match = re.search(pattern, sql, flags=re.IGNORECASE)
    if match:
        offset_val = match.group(1)
        limit_val = match.group(2)
        sql = re.sub(pattern, f"LIMIT {limit_val} OFFSET {offset_val}", sql, flags=re.IGNORECASE)


    # Split into individual statements
    sql_statements = [s.strip() for s in sql.split(";") if s.strip()]

    # Check first line to see if it's actual SQL
    first_line = sql_statements[0].lower()
    if not any(first_line.startswith(kw) for kw in ("select", "show", "desc", "insert", "update", "delete")):
        print(sql)
        return None

    print(f"\n ======📊Cleaned SQL:\n{sql}======\n")

    try:
        for stmt in sql_statements:
            lowered = stmt.lower()

            if lowered.startswith(("insert", "update", "delete")):
                with engine.begin() as conn:
                    result = conn.execute(sqlalchemy.text(stmt))
                print(f"Modification executed successfully. Rows affected: {result.rowcount}")


            else:
                df = pd.read_sql(stmt, engine)
                print("======📒Query Results:======")
                print(df)
                print()

    except Exception as e:
        print("Error running SQL:", e)

# CLI interaction loop
if __name__ == "__main__":
    while True:
        user_input = input("\n❓Ask me a question (or type 'exit'): ")
        if user_input.lower() == "exit":
            break
        run_nl_query(user_input)
