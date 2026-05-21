from database.db import engine


try:

    conn = (

        engine.connect()

    )


    print(

        "Connected to Supabase"

    )


except Exception as e:


    print(

        e

    )