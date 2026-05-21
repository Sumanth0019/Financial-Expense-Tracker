import joblib


model = joblib.load("model.pkl")


future = [[

2026,

6,

60000,

7000,

12000,

3000,

1000,

2000,

1800,

6000,

8000,

2000,

3000,

2500

]]


pred = model.predict(
    future
)


print(

"Predicted Expense:",

pred[0]

)