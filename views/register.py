import streamlit as st

from database.db import SessionLocal
from database.models import User



def register():


    st.title(

        "Register"

    )


    username = st.text_input(

        "Username"

    )


    email = st.text_input(

        "Email"

    )


    password = st.text_input(

        "Password",

        type="password"

    )


    if st.button(

        "Register"

    ):


        if (

            not username

            or

            not email

            or

            not password

        ):


            st.error(

                "Fill all fields"

            )


            return


        db = SessionLocal()


        existing = (

            db.query(User)

            .filter(

                User.email

                ==

                email

            )

            .first()

        )


        if existing:


            st.error(

                "User exists"

            )


            return


        new_user = User(

            username=username,

            email=email,

            password=password

        )


        db.add(

            new_user

        )


        db.commit()


        st.success(

            "Registered"

        )