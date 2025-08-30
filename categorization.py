import pandas as pd

# Simple categorization rules (can be replaced by ML)
CATEGORY_RULES = {
    "Starbucks": "Food & Drinks",
    "McDonalds": "Food & Drinks",
    "Uber": "Transport",
    "Amazon": "Shopping",
    "Salary": "Income"
}

def categorize_transactions(df: pd.DataFrame) -> pd.DataFrame:
    def get_category(desc):
        for keyword, category in CATEGORY_RULES.items():
            if keyword.lower() in desc.lower():
                return category
        return "Other"

    df["Category"] = df["Description"].apply(get_category)
    return df
