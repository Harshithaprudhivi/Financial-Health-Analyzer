import pandas as pd
import random
from datetime import datetime, timedelta

rows = []
start_date = datetime(2024, 1, 1)

for i in range(180):  # 6 months data
    date = start_date + timedelta(days=i)

    revenue = random.randint(20000, 80000)
    cogs = random.randint(8000, 30000)
    operating_expense = random.randint(5000, 20000)
    inventory = random.randint(10000, 50000)
    receivables = random.randint(5000, 25000)
    payables = random.randint(3000, 20000)
    loan_outstanding = random.randint(100000, 300000)
    tax_paid = random.randint(1000, 5000)

    rows.append([
        date.strftime('%Y-%m-%d'),
        revenue,
        cogs,
        operating_expense,
        inventory,
        receivables,
        payables,
        loan_outstanding,
        tax_paid
    ])

df = pd.DataFrame(rows, columns=[
    "date",
    "revenue",
    "cogs",
    "operating_expense",
    "inventory",
    "receivables",
    "payables",
    "loan_outstanding",
    "tax_paid"
])

df.to_csv("sample_sme_financials.csv", index=False)
print("Dataset created: sample_sme_financials.csv")
