import streamlit as st


def load_css():

    st.markdown(
        """
        <style>

        /* ==========================
           APP BACKGROUND
        ========================== */

        .stApp{

            background:
            linear-gradient(
                135deg,
                #0f172a,
                #1e293b,
                #312e81
            );

            color:
            white;

        }



        /* ==========================
           SIDEBAR
        ========================== */

        section[data-testid="stSidebar"]{

            background:
            linear-gradient(
                180deg,
                #111827,
                #1e3a8a
            );

            border-right:
            1px solid rgba(
                255,
                255,
                255,
                .08
            );

        }


        section[data-testid="stSidebar"] *{

            color:
            white
            !important;

        }



        /* ==========================
           HERO
        ========================== */

        .hero{

            background:
            linear-gradient(
                135deg,
                #2563eb,
                #7c3aed
            );

            padding:
            35px;

            border-radius:
            30px;

            margin-bottom:
            25px;

            box-shadow:
            0 20px 40px rgba(
                0,
                0,
                0,
                .30
            );

        }


        .hero h1{

            color:
            white;

            font-size:
            42px;

            font-weight:
            700;

        }


        .hero p{

            color:
            rgba(
                255,
                255,
                255,
                .85
            );

        }



        /* ==========================
           METRIC CARDS
        ========================== */

        [data-testid="metric-container"]{

            background:
            rgba(
                255,
                255,
                255,
                .06
            );

            backdrop-filter:
            blur(18px);

            border:
            1px solid rgba(
                255,
                255,
                255,
                .08
            );

            border-radius:
            22px;

            padding:
            22px;

            box-shadow:
            0 8px 30px rgba(
                0,
                0,
                0,
                .25
            );

            transition:
            .3s;

        }


        [data-testid="metric-container"]:hover{

            transform:
            translateY(-6px);

        }


        [data-testid="stMetricLabel"]{

            color:
            rgba(
                255,
                255,
                255,
                .75
            )
            !important;

        }



        [data-testid="stMetricValue"]{

            color:
            white
            !important;

            font-size:
            42px
            !important;

            font-weight:
            700
            !important;

        }



        /* ==========================
           INPUTS (FIXED)
        ========================== */


        .stTextInput input,
        .stNumberInput input{

            background:
            rgba(
                17,
                24,
                39,
                .85
            )
            !important;


            color:
            white
            !important;


            border:
            1px solid rgba(
                255,
                255,
                255,
                .08
            )
            !important;


            border-radius:
            14px
            !important;

        }



        .stTextInput input::placeholder,
        .stNumberInput input::placeholder{

            color:
            rgba(
                255,
                255,
                255,
                .45
            )
            !important;

        }



        .stNumberInput button{

            background:
            transparent
            !important;


            color:
            white
            !important;

        }



        div[data-baseweb="select"]{

            background:
            rgba(
                17,
                24,
                39,
                .85
            )
            !important;


            border-radius:
            14px
            !important;

        }



        div[data-baseweb="select"] *{

            color:
            white
            !important;

        }



        input:focus{

            border:
            1px solid #7c3aed
            !important;


            box-shadow:
            0 0 12px rgba(
                124,
                58,
                237,
                .4
            );

        }



        /* ==========================
           BUTTONS
        ========================== */


        .stButton > button{

            background:
            linear-gradient(
                90deg,
                #2563eb,
                #7c3aed
            );


            color:
            white;


            border:
            none;


            border-radius:
            16px;


            padding:
            12px;


            font-weight:
            700;


            transition:
            .25s;

        }



        .stButton > button:hover{

            transform:
            scale(1.03);


            box-shadow:
            0 10px 25px rgba(
                124,
                58,
                237,
                .35
            );

        }



        /* ==========================
           TABLES
        ========================== */


        [data-testid="stDataFrame"]{

            background:
            rgba(
                255,
                255,
                255,
                .04
            );


            border-radius:
            20px;

        }



        /* ==========================
           CHARTS
        ========================== */


        .js-plotly-plot{

            background:
            rgba(
                255,
                255,
                255,
                .03
            );


            border-radius:
            24px;


            padding:
            10px;

        }



        /* ==========================
           ALERTS
        ========================== */


        .stSuccess{

            background:
            rgba(
                34,
                197,
                94,
                .12
            );

        }



        .stWarning{

            background:
            rgba(
                245,
                158,
                11,
                .12
            );

        }



        .stError{

            background:
            rgba(
                239,
                68,
                68,
                .12
            );

        }



        /* ==========================
           PROGRESS
        ========================== */


        .stProgress > div > div{

            background:
            linear-gradient(
                90deg,
                #22c55e,
                #3b82f6
            );

        }



        /* ==========================
           HEADINGS
        ========================== */


        h1{

            color:
            white;

        }



        h2{

            color:
            #c084fc;

        }



        h3{

            color:
            #93c5fd;

        }


        </style>
        """,

        unsafe_allow_html=True

    )
