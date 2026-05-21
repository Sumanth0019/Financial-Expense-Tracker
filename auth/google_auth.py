import os
import requests
import streamlit as st
from dotenv import load_dotenv

from streamlit_oauth import (

    OAuth2Component

)


load_dotenv()


CLIENT_ID = (

    st.secrets.get(

        "GOOGLE_CLIENT_ID"

    )

    or

    os.getenv(

        "GOOGLE_CLIENT_ID"

    )

)


CLIENT_SECRET = (

    st.secrets.get(

        "GOOGLE_CLIENT_SECRET"

    )

    or

    os.getenv(

        "GOOGLE_CLIENT_SECRET"

    )

)


AUTHORIZE_URL = (

    "https://accounts.google.com/o/oauth2/auth"

)


TOKEN_URL = (

    "https://oauth2.googleapis.com/token"

)


USERINFO = (

    "https://www.googleapis.com/oauth2/v1/userinfo"

)



def google_login():


    oauth = (

        OAuth2Component(

            CLIENT_ID,

            CLIENT_SECRET,

            AUTHORIZE_URL,

            TOKEN_URL

        )

    )


    result = (

        oauth.authorize_button(

            "🔵 Continue with Google",

            redirect_uri=

            "http://localhost:8501",

            scope=

            "openid email profile",

            key="google"

        )

    )


    if result:


        token = (

            result["token"]

            [

                "access_token"

            ]

        )


        user = (

            requests.get(

                USERINFO,

                headers={

                    "Authorization":

                    f"Bearer {token}"

                }

            )

            .json()

        )


        return {

            "email":

            user["email"],

            "name":

            user["name"]

        }


    return None
