import pandas as pd


def preprocess():

    df = pd.read_csv(
        "dataset/monthly_spending_dataset.csv"
    )


    df["Month"] = pd.to_datetime(
        df["Month"]
    )


    df["Year"] = (
        df["Month"]
        .dt.year
    )


    df["Month_num"] = (
        df["Month"]
        .dt.month
    )


    X = df[

        [

        "Year",

        "Month_num",

        "Income (₹)",

        "Groceries (₹)",

        "Rent (₹)",

        "Transportation (₹)",

        "Gym (₹)",

        "Utilities (₹)",

        "Healthcare (₹)",

        "Investments (₹)",

        "Savings (₹)",

        "EMI/Loans (₹)",

        "Dining & Entertainment (₹)",

        "Shopping & Wants (₹)"

        ]

    ]


    y = df[
        "Total Expenditure (₹)"
    ]


    return X,y