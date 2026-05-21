import pandas as pd
import joblib

from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import mean_absolute_error



df = pd.read_csv(

    "dataset/monthly_spending_dataset.csv"

)


df["Month"] = pd.to_datetime(

    df["Month"]

)


df = df.sort_values(

    "Month"

)


target = (

    "Total Expenditure (₹)"

)


df["lag1"] = (

    df[target]

    .shift(1)

)


df["lag2"] = (

    df[target]

    .shift(2)

)


df["lag3"] = (

    df[target]

    .shift(3)

)


df = (

    df.dropna()

)


X = df[

    [

        "lag1",

        "lag2",

        "lag3"

    ]

]


y = df[

    target

]


train = int(

    len(df)*0.8

)


X_train = X[:train]

X_test = X[train:]

y_train = y[:train]

y_test = y[train:]


model = (

    RandomForestRegressor(

        n_estimators=100,

        random_state=42

    )

)


model.fit(

    X_train,

    y_train

)


pred = (

    model.predict(

        X_test

    )

)


print(

    "MAE:",

    mean_absolute_error(

        y_test,

        pred

    )

)


joblib.dump(

    model,

    "forecast_model.pkl"

)