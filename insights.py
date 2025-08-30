import pandas as pd

def calculate_insights(df: pd.DataFrame) -> dict:
    total_income = df[df["Amount"] > 0]["Amount"].sum()
    total_expense = df[df["Amount"] < 0]["Amount"].sum()
    net_savings = total_income + total_expense

    top_category = (
        df[df["Amount"] < 0]
        .groupby("Category")["Amount"]
        .sum()
        .abs()
        .sort_values(ascending=False)
        .head(1)
    )

    return {
        "Total Income": round(total_income, 2),
        "Total Expenses": round(abs(total_expense), 2),
        "Net Savings": round(net_savings, 2),
        "Biggest Expense Category": top_category.index[0] if not top_category.empty else "None",
    }
