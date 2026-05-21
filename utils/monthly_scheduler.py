from apscheduler.schedulers.background import (

    BackgroundScheduler

)

from database.db import SessionLocal

from database.models import User

from utils.expense import (

    get_expenses

)

from utils.email_report import (

    send_email,

    create_monthly_report

)


scheduler = (

    BackgroundScheduler()

)



def send_monthly_reports():


    db = SessionLocal()


    users = (

        db.query(User)

        .all()

    )


    for user in users:


        expenses = (

            get_expenses(

                user.username

            )

        )


        total = sum(

            e.amount

            for e in expenses

        )


        budget = 10000


        savings = (

            budget -

            total

        )


        prediction = (

            total * 1.05

        )


        report = (

            create_monthly_report(

                user.username,

                total,

                budget,

                savings,

                prediction

            )

        )


        send_email(

            user.email,

            report

        )


        print(

            f"Report sent to {user.email}"

        )



scheduler.add_job(

    send_monthly_reports,

    trigger="cron",

    day=1,

    hour=9,

    minute=0

)



def start_scheduler():

    scheduler.start()