import pandas as pd
import plotly.express as px


def category_chart(expenses):

    df = pd.DataFrame([{

        "Category": e.category,

        "Amount": e.amount

    } for e in expenses])


    if len(df)==0:
        return None


    fig = px.pie(

        df,

        names="Category",

        values="Amount",

        title="Expense Distribution"
    )

    return fig



def trend_chart(expenses):

    df = pd.DataFrame([{

        "Category":e.category,

        "Amount":e.amount

    }

    for e in expenses])


    if len(df)==0:
        return None


    fig = px.bar(

        df,

        x="Category",

        y="Amount",

        title="Category Spending"
    )

    return fig