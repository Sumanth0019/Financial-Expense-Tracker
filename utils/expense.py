from database.db import SessionLocal
from database.models import Expense


def add_expense(
        username,
        amount,
        category,
        description
):

    db=SessionLocal()

    expense=Expense(

        username=username,

        amount=amount,

        category=category,

        description=description
    )

    db.add(expense)

    db.commit()



def get_expenses(username):

    db=SessionLocal()

    return db.query(
        Expense
    ).filter(
        Expense.username==
        username
    ).all()