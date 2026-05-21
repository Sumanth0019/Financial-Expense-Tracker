import streamlit as st

from database.db import SessionLocal
from database.models import User

from auth.jwt_auth import (

    create_token

)



def login():


    st.title(

        "Login"

    )


    email = st.text_input(

        "Email"

    )


    password = st.text_input(

        "Password",

        type="password"

    )


    if st.button(

        "Login"

    ):


        # Empty validation
        if (

            not email

            or

            not password

        ):


            st.error(

                "Fill all fields"

            )


            return


        db = SessionLocal()


        user = (

            db.query(User)

            .filter(

                User.email

                ==

                email

            )

            .first()

        )


        if (


            user

            and

            user.password

            ==

            password

        ):


            token = (

                create_token(

                    user.username

                )

            )


            st.session_state[
                "token"
            ] = token


            st.session_state[
                "username"
            ] = (

                user.username

            )


            st.success(

                "Login successful"

            )


            st.rerun()


        else:


            st.error(

                "Invalid credentials"

            )