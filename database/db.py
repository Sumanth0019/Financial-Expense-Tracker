import os
import streamlit as st

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DATABASE_URL = st.secrets["DATABASE_URL"]


# IMPORTANT:
DATABASE_URL = DATABASE_URL.replace(

    "postgresql://",

    "postgresql+psycopg2://",

    1

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
