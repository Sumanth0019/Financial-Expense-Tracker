import os
import joblib


BASE_DIR = os.path.dirname(
    __file__
)


MODEL_PATH = os.path.join(

    BASE_DIR,

    "forecast_model.pkl"

)


try:

    model = joblib.load(

        MODEL_PATH

    )

except:

    model = None



def predict_next_month(

        monthly_totals

):


    # No data

    if len(

        monthly_totals

    ) == 0:

        return None


    # Only 1 month

    if len(

        monthly_totals

    ) == 1:


        return (

            monthly_totals[0]

        )


    # 2 months → trend estimate

    if len(

        monthly_totals

    ) == 2:


        trend = (

            monthly_totals[-1]

            -

            monthly_totals[-2]

        )


        prediction = (

            monthly_totals[-1]

            +

            trend

        )


        return max(

            prediction,

            0

        )


    # 3+ months → ML prediction


    if model:


        prediction = (

            model.predict(

                [[

                    monthly_totals[-3],

                    monthly_totals[-2],

                    monthly_totals[-1]

                ]]

            )[0]

        )


        return max(

            prediction,

            0

        )


    # fallback if model missing


    avg = (

        sum(

            monthly_totals[-3:]

        )

        /

        3

    )


    return avg