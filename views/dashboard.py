import streamlit as st
import pandas as pd
import numpy as np
import datetime
import joblib

from utils.expense import (
    add_expense,
    get_expenses
)

from utils.charts import (
    category_chart,
    trend_chart
)

from utils.email_report import (
    send_email,
    create_monthly_report
)

from utils.styles import (
    load_css
)

from ml.forecast_predict import (

    predict_next_month

)

from database.db import SessionLocal
from database.models import User


model = joblib.load(
    "ml/model.pkl"
)


def dashboard():

    load_css()

    st.markdown(

    f"""

    <div class="hero">

    <h1>

    Financial Expense Tracker

    </h1>



    </div>

    """,

    unsafe_allow_html=True

    )

    if "warning_sent" not in st.session_state:

        st.session_state[
            "warning_sent"
        ] = False


    if "exceeded_sent" not in st.session_state:

        st.session_state[
            "exceeded_sent"
        ] = False


    current_month = (

        datetime.datetime.now()

        .month

    )


    if (

        "last_month"

        not in st.session_state

    ):

        st.session_state[
            "last_month"
        ] = current_month


    if (

        st.session_state[
            "last_month"
        ]

        != current_month

    ):


        st.session_state[
            "warning_sent"
        ] = False


        st.session_state[
            "exceeded_sent"
        ] = False


        st.session_state[
            "last_month"
        ] = current_month


    username = (

        st.session_state[
            "username"
        ]

    )


    st.title(

        f"Welcome {username} 👋"

    )


    amount = st.number_input(

        "Amount",

        min_value=0.0

    )


    category = st.selectbox(

        "Category",

        [

            "Food",

            "Travel",

            "Shopping",

            "Bills",

            "Other"

        ]

    )


    description = st.text_input(

        "Description"

    )


    if st.button(

        "Add Expense"

    ):


        add_expense(

            username,

            amount,

            category,

            description

        )


        st.success(

            "Expense Added "

        )


    expenses = get_expenses(

        username

    )


    total = sum(

        e.amount

        for e in expenses

    )


    monthly_totals = [

        total

    ]


    forecast = (

        predict_next_month(

            monthly_totals

        )

    )


    if forecast is not None:

        with st.container(border=True):

            st.metric(

                " Predicted Next Month Spending",

                f"₹{forecast:.0f}"

            )

            st.caption(

                "Estimated from spending history"

            )

    db = SessionLocal()


    user = (

        db.query(User)

        .filter(

            User.username ==

            username

        )

        .first()

    )


    user_email = user.email


    st.subheader(

        "📋 Recent Expenses"

    )


    for e in reversed(

        expenses

    ):


        col1, col2, col3 = st.columns(

        [2,1,2]
        )


        with col1:


            st.markdown(

                f"""

                ### {e.category}

                """

            )


        with col2:


            st.metric(

                "Amount",

                f"₹{e.amount:.0f}"

            )


        with col3:


            st.markdown(

                f"""

                **Note**

                {e.description

                if e.description

                else "No description"}

                """

            )


    st.divider()


    pie = category_chart(
        expenses
    )


    if pie:

        st.plotly_chart(
            pie,
            use_container_width=True
        )


    bar = trend_chart(
        expenses
    )


    if bar:

        st.plotly_chart(
            bar,
            use_container_width=True
        )


    st.subheader(

        "Budget Tracker"

    )


    budget = st.number_input(

        "Monthly Budget",


        value=10000.0

    )


    total = sum(

        e.amount

        for e in expenses

    )


    remaining = (

        budget -

        total

    )


    progress = (

        total /

        budget

        if budget > 0

        else 0

    )


    saved = (

        budget -

        total

    )


    col1, col2, col3 = st.columns(3)


    with col1:

        st.metric(

            " Total Spent",

            f"₹{total:.2f}"

        )


    with col2:

        st.metric(

            "Remaining",

            f"₹{remaining:.2f}"

        )


    with col3:

        st.metric(

            "Budget",

            f"₹{budget:.2f}"

        )


    st.progress(

        min(

            progress,

            1.0

        )

    )


    prediction = 0


    # =====================
    # 80% Warning
    # =====================

    if progress >= 0.8:


        st.warning(

            "⚠ Used 80% budget"

        )


        if (

            not st.session_state[

                "warning_sent"

            ]

        ):


            monthly_report = (

                create_monthly_report(

                    username,

                    total,

                    budget,

                    saved,

                    prediction

                )

            )


            success = (

                send_email(

                    recipient=

                    user_email,


                    subject=

                    "⚠ Budget Warning",


                    message=

                    monthly_report

                )

            )


            if success:


                st.session_state[

                    "warning_sent"

                ] = True


                st.success(

                    "Warning mail sent"

                )


            else:


                st.error(

                    "Mail failed"

                )



    # =====================
    # Budget Exceeded
    # =====================

    if total > budget:


        st.error(

            "🚨 Budget exceeded"

        )


        if (

            not st.session_state[

                "exceeded_sent"

            ]

        ):


            monthly_report = (

                create_monthly_report(

                    username,

                    total,

                    budget,

                    saved,

                    prediction

                )

            )


            success = (

                send_email(

                    recipient=

                    user_email,


                    subject=

                    "🚨 Budget Exceeded Alert",


                    message=

                    monthly_report

                )

            )


            if success:


                st.session_state[

                    "exceeded_sent"

                ] = True


                st.success(

                    "Budget alert mail sent"

                )


            else:


                st.error(

                    "Mail failed"

                )

    if saved > 0:

        st.success(

            f"You saved ₹{saved:.2f}"

        )

    else:

        st.error(

            f"Overspent ₹{abs(saved):.2f}"

        )


    df = pd.DataFrame([

        {

            "Category":

            e.category,

            "Amount":

            e.amount

        }

        for e in expenses

    ])


    if len(df) > 0:


        top = (

            df.groupby(

                "Category"

            )

            ["Amount"]

            .sum()

            .idxmax()

        )


        st.info(

            f"Highest spending: {top}"

        )


    

    st.subheader(

        "📧 Send Report"

    )


    email = st.text_input(

        "Email"

    )


    if st.button(

        "Send Report"

    ):


        monthly_report = (

            create_monthly_report(

                username,

                total,

                budget,

                saved,

                prediction

            )

        )


        send_email(

            recipient=

            email,


            subject=

            "📊 Monthly Expense Report",


            message=

            monthly_report

        )


        st.success(

            "Email sent "

        )


    db.close()