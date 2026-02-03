def analyze_risk(summary):
    risks = []
    recommendations = []
    credit_score = 100  # start from perfect score

    # Profitability check
    if summary['avg_net_profit_margin'] < 0.1:
        risks.append("Low profitability detected.")
        recommendations.append("Reduce operating expenses or increase pricing.")
        credit_score -= 20

    # Liquidity check
    if summary['avg_current_ratio'] < 1.5:
        risks.append("Poor liquidity. Difficulty paying suppliers.")
        recommendations.append("Improve receivables collection and reduce payables delay.")
        credit_score -= 20

    # Debt check
    if summary['avg_debt_to_equity'] > 5:
        risks.append("High dependency on debt financing.")
        recommendations.append("Consider restructuring loans or reducing liabilities.")
        credit_score -= 25

    # Inventory check
    if summary['avg_inventory_turnover'] < 1:
        risks.append("Slow moving inventory.")
        recommendations.append("Optimize inventory and clear dead stock.")
        credit_score -= 15

    # Cash flow check
    if summary['cash_flow_trend'] < 0:
        risks.append("Negative cash flow trend.")
        recommendations.append("Increase cash reserves and reduce unnecessary spending.")
        credit_score -= 20

    # Working capital health
    if summary['total_working_capital'] > 0:
        recommendations.append("Working capital position is healthy.")

    # Creditworthiness level
    if credit_score >= 75:
        credit_status = "Excellent - Eligible for low-interest loans and credit lines."
    elif credit_score >= 50:
        credit_status = "Moderate - Eligible for working capital loans."
    else:
        credit_status = "High Risk - Loan approval may be difficult."

    return {
        "credit_score": credit_score,
        "credit_status": credit_status,
        "risks": risks,
        "recommendations": recommendations
    }
