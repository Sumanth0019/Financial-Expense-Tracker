import streamlit as st
import pandas as pd
import datetime
import joblib

from utils.expense import add_expense, get_expenses
from utils.charts import category_chart, trend_chart
from utils.email_report import send_email, create_monthly_report
from utils.styles import load_css
from ml.forecast_predict import predict_next_month
from database.db import SessionLocal
from database.models import User


model = joblib.load("ml/model.pkl")


def dashboard():

    load_css()

    username = st.session_state["username"]

    expenses = get_expenses(username)

    total = sum(e.amount for e in expenses)

    forecast = predict_next_month([total]) or 0


    db = SessionLocal()

    user = (

        db.query(User)

        .filter(

            User.username == username

        )

        .first()

    )

    user_email = user.email if user else ""


    hour = datetime.datetime.now().hour

    greeting = (

        "Morning"

        if hour < 12

        else

        "Afternoon"

        if hour < 18

        else

        "Evening"

    )


    # =========================
    # HERO
    # =========================

    st.markdown(

    f"""

    <div class="hero">

    <h1>

     Good {greeting},

    {username}

    </h1>




    </div>

    """,

    unsafe_allow_html=True

    )


    # =========================
    # METRICS
    # =========================


    c1, c2, c3, c4 = st.columns(4)


    c1.metric(

        "💸 Total Spent",

        f"₹{total:.0f}"

    )


    c2.metric(

        "🔮 Prediction",

        f"₹{forecast:.0f}"

    )


    c3.metric(

        "🧾 Expenses",

        len(expenses)

    )


    avg = (

        total /

        max(

            len(expenses),

            1

        )

    )


    c4.metric(

        "📊 Avg",

        f"₹{avg:.0f}"

    )


    st.divider()


    # =========================
    # ADD EXPENSE
    # =========================


    with st.container(

        border=True

    ):


        st.subheader(

            "➕ Add Expense"

        )


        col1, col2, col3 = st.columns(3)


        amount = (

            col1.number_input(

                "Amount",

                min_value=0.0

            )

        )


        category = (

            col2.selectbox(

                "Category",

                [

                    "Food",

                    "Travel",

                    "Shopping",

                    "Bills",

                    "Other"

                ]

            )

        )


        description = (

            col3.text_input(

                "Description"

            )

        )


        if st.button(

            "Save Expense",

            width="stretch"

        ):


            add_expense(

                username,

                amount,

                category,

                description

            )


            st.success(

                "Expense Added"

            )


            st.rerun()



    # =========================
    # CHARTS + BUDGET
    # =========================


    left, right = st.columns(

        [

            2,

            1

        ]

    )


    with left:


        pie = category_chart(

            expenses

        )


        if pie:


            st.plotly_chart(

                pie,

                width="stretch"

            )


        trend = trend_chart(

            expenses

        )


        if trend:


            st.plotly_chart(

                trend,

                width="stretch"

            )



    with right:


        st.subheader(

            "Budget"

        )


        budget = (

            st.number_input(

                "Monthly Budget",

                value=10000.0

            )

        )


        progress = (

            total /

            max(

                budget,

                1

            )

        )


        st.progress(

            min(

                progress,

                1.0

            )

        )


        remaining = (

            budget -

            total

        )


        st.metric(

            "Remaining",

            f"₹{remaining:.0f}"

        )


        if progress >= 0.8:


            st.warning(

                "⚠ 80% budget used"

            )


        if total > budget:


            st.error(

                "🚨 Budget exceeded"

            )


            send_email(

                user_email,

                "Budget Alert",

                create_monthly_report(

                    username,

                    total,

                    budget,

                    remaining,

                    forecast

                )

            )



    # =========================
    # TABLE
    # =========================


    st.subheader(

        "📋 Recent Expenses"

    )


    df = pd.DataFrame(

        [

            {

                "Category":

                e.category,

                "Amount":

                e.amount,

                "Description":

                e.description

            }

            for e in expenses

        ]

    )


    if len(df):


        st.dataframe(

            df,

            width="stretch"

        )



    # =========================
    # REPORT MAIL
    # =========================


    st.subheader(

        "📧 Send Report"

    )


    recipient = st.text_input(

        "Recipient"

    )


    if st.button(

        "Send Report"

    ):


        report = (

            create_monthly_report(

                username,

                total,

                budget,

                remaining,

                forecast

            )

        )


        send_email(

            recipient,

            "Expense Report",

            report

        )


        st.success(

            "Report Sent"

        )


    db.close()
