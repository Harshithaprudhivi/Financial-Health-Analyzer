def calculate_metrics_from_df(df):

    df['gross_profit'] = df['revenue'] - df['cogs']
    df['net_profit'] = df['gross_profit'] - df['operating_expense']
    df['working_capital'] = df['receivables'] + df['inventory'] - df['payables']

    df['gross_profit_margin'] = df['gross_profit'] / df['revenue']
    df['net_profit_margin'] = df['net_profit'] / df['revenue']
    df['current_ratio'] = (df['receivables'] + df['inventory']) / df['payables']
    df['debt_to_equity'] = df['loan_outstanding'] / (df['revenue'] - df['cogs'])
    df['inventory_turnover'] = df['cogs'] / df['inventory']
    df['cash_flow'] = df['net_profit'] - df['tax_paid']

    recent = df.tail(30)

    summary = {
    "avg_revenue": float(recent['revenue'].mean()),
    "avg_net_profit_margin": float(recent['net_profit_margin'].mean()),
    "avg_current_ratio": float(recent['current_ratio'].mean()),
    "avg_debt_to_equity": float(recent['debt_to_equity'].mean()),
    "avg_inventory_turnover": float(recent['inventory_turnover'].mean()),
    "total_working_capital": float(recent['working_capital'].mean()),
    "cash_flow_trend": float(recent['cash_flow'].sum())
}


    return summary
