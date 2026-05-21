import streamlit as st

from views.login import login
from views.register import register
from views.dashboard import dashboard

from database.db import (
    engine,
    SessionLocal
)

from database.models import (
    Base,
    User
)

from auth.google_auth import (
    google_login
)


Base.metadata.create_all(

    bind=engine

)



def handle_google_login():

    google_user = (

        google_login()

    )


    if google_user:


        db = SessionLocal()


        existing = (

            db.query(User)

            .filter(

                User.email

                ==

                google_user[
                    "email"
                ]

            )

            .first()

        )


        if not existing:


            new_user = User(

                username=

                google_user[
                    "name"
                ],


                email=

                google_user[
                    "email"
                ],


                password=

                "google_auth"

            )


            db.add(

                new_user

            )


            db.commit()


        st.session_state[
            "token"
        ] = True


        st.session_state[
            "username"
        ] = (

            google_user[
                "name"
            ]

        )


        st.rerun()



if "token" not in st.session_state:


    choice = (

        st.sidebar.selectbox(

            "Menu",

            [

                "Login",

                "Register"

            ]

        )

    )


    if choice == "Login":


        login()


        st.markdown("---")


        st.markdown(

            "### Continue with Google"

        )


        handle_google_login()



    else:


        register()


        st.markdown("---")


        st.markdown(

            "### Continue with Google"

        )


        handle_google_login()



else:


    dashboard()


    if st.sidebar.button(

        "Logout"

    ):


        st.session_state.clear()


        st.rerun()