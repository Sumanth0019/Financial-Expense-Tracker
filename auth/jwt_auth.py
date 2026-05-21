import jwt
import datetime
import os

from dotenv import load_dotenv


load_dotenv()


SECRET = (

    os.getenv(

        "JWT_SECRET"

    )

)



def create_token(

        username

):


    payload = {


        "username":

        username,


        "exp":

        datetime.datetime.utcnow()

        +

        datetime.timedelta(

            hours=3

        )

    }


    return jwt.encode(

        payload,

        SECRET,

        algorithm="HS256"

    )



def verify_token(

        token

):


    try:


        decoded = (

            jwt.decode(

                token,

                SECRET,

                algorithms=[

                    "HS256"

                ]

            )

        )


        return decoded


    except:


        return None