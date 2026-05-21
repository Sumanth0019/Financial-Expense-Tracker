import os
import streamlit as st

from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


load_dotenv()


DATABASE_URL = (

    st.secrets.get(

        "DATABASE_URL"

    )

    or

    os.getenv(

        "DATABASE_URL"

    )

)


engine = create_engine(

    DATABASE_URL,


    connect_args={

        "sslmode":

        "require"

    },


    pool_pre_ping=True

)


SessionLocal = sessionmaker(

    autocommit=False,

    autoflush=False,

    bind=engine

)
