import os
import streamlit as st

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


load_dotenv()


DATABASE_URL = (

    st.secrets["DATABASE_URL"]

    if "DATABASE_URL"

    in st.secrets

    else

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


    pool_pre_ping=True,


    pool_recycle=300

)


SessionLocal = sessionmaker(

    autocommit=False,

    autoflush=False,

    bind=engine

)
