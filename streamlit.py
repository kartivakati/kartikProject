import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from categorization import categorize_transactions
from insights import calculate_insights

st.set_page_config(page_title="AI Finance Dashboard", layout="wide")

st.title("💰 AI-Powered Personal Finance Dashboard")

# Upload CSV
uploaded_file = st.file_uploader("Upload your bank statement (CSV)", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    # Categorize transactions
    df = categorize_transactions(df)

    # Show table
    st.subheader("📑 Transactions")
    st.dataframe(df)

    # Insights
    st.subheader("📊 Insights")
    insights = calculate_insights(df)
    for k, v in insights.items():
        st.write(f"**{k}:** {v}")

    # Plot expenses by category
    st.subheader("💸 Expenses by Category")
    expense_df = df[df["Amount"] < 0].groupby("Category")["Amount"].sum().abs()
    fig, ax = plt.subplots()
    expense_df.plot(kind="bar", ax=ax)
    st.pyplot(fig)

else:
    st.info("Upload a CSV file to get started.")
