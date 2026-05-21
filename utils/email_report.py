import os
import smtplib
import streamlit as st
from email.mime.text import MIMEText
from dotenv import load_dotenv


load_dotenv()


EMAIL = (

    st.secrets.get(

        "EMAIL"

    )

    or

    os.getenv(

        "EMAIL"

    )

)


EMAIL_PASSWORD = (

    st.secrets.get(

        "EMAIL_PASSWORD"

    )

    or

    os.getenv(

        "EMAIL_PASSWORD"

    )

)


def create_monthly_report(

        username,

        total,

        budget,

        saved,

        prediction

):


    report = f"""

Hello {username},


Monthly Expense Summary


---------------------------------

Total Expenses:

₹{total:.2f}


Budget:

₹{budget:.2f}


Saved:

₹{saved:.2f}


Predicted Next Month:

₹{prediction:.2f}


---------------------------------


Track expenses wisely.


"""


    return report




def send_email(

        recipient,

        subject,

        message

):


    try:


        msg = MIMEText(

            message

        )


        msg["Subject"] = subject
        msg["From"] = EMAIL
        msg["To"] = recipient


        print(

            "Sender:",

            EMAIL

        )


        print(

            "Recipient:",

            recipient

        )


        server = smtplib.SMTP(

            "smtp.gmail.com",

            587

        )


        server.starttls()


        print(

            "Logging in..."

        )


        server.login(

            EMAIL,

            EMAIL_PASSWORD

        )


        print(

            "Login successful"

        )


        server.sendmail(

            EMAIL,

            recipient,

            msg.as_string()

        )


        print(

            "Mail sent"

        )


        server.quit()


        return True


    except Exception as e:


        print(

            "EMAIL ERROR:",

            e

        )


        return False
