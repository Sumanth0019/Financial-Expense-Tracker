import streamlit as st
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DATABASE_URL = st.secrets["DATABASE_URL"]

print("DATABASE URL loaded:", DATABASE_URL[:30], "...")

try:

    engine = create_engine(

        DATABASE_URL,

        connect_args={

            "sslmode":

            "require"

        },

        pool_pre_ping=True

    )


    conn = engine.connect()

    print(

        "DB CONNECTED SUCCESSFULLY"

    )

    conn.close()


except Exception as e:

    print(

        "REAL DB ERROR:",

        repr(e)

    )

    raise


SessionLocal = sessionmaker(

    autocommit=False,

    autoflush=False,

    bind=engine

)
