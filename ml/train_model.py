from preprocess import preprocess

from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import (
    mean_absolute_error,
    r2_score
)

import joblib


X,y = preprocess()


X_train,X_test,y_train,y_test = (

    train_test_split(

        X,

        y,

        test_size=0.2,

        random_state=42
    )

)


model = RandomForestRegressor(

    n_estimators=100,

    random_state=42
)


model.fit(

    X_train,

    y_train
)


pred = model.predict(
    X_test
)


print(

"MAE:",

mean_absolute_error(
    y_test,
    pred
)

)


print(

"R2:",

r2_score(
    y_test,
    pred
)

)


joblib.dump(

    model,

    "model.pkl"
)
