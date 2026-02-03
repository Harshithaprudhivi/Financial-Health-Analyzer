## to test metrics.py
# from metrics import calculate_metrics

# summary, df = calculate_metrics("sample_sme_financials.csv")

# print("===== SME Financial Summary =====")
# for k, v in summary.items():
#     print(f"{k}: {v}")


# to test risk_analyzer.py
from metrics import calculate_metrics
from risk_analyzer import analyze_risk

summary, df = calculate_metrics("sample_sme_financials.csv")

result = analyze_risk(summary)

print("\n===== RISK & CREDIT ANALYSIS =====\n")
print("Credit Score:", result["credit_score"])
print("Credit Status:", result["credit_status"])

print("\nRisks:")
for r in result["risks"]:
    print("-", r)

print("\nRecommendations:")
for rec in result["recommendations"]:
    print("-", rec)
