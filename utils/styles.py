import streamlit as st


def load_css():

    st.markdown(

    """

    <style>

    /* MAIN APP */

    .stApp{

    background:
    linear-gradient(
    135deg,
    #0f172a,
    #1e293b,
    #312e81
    );

    color:white;

    }



    /* SIDEBAR */

    section[data-testid="stSidebar"]{

    background:
    linear-gradient(

    180deg,

    #111827,

    #1e3a8a

    );

    color:white;

    border-right:

    2px solid #374151;

    }



    /* HERO SECTION */

    .hero{

    background:

    linear-gradient(

    90deg,

    #2563eb,

    #7c3aed

    );

    padding:

    30px;

    border-radius:

    25px;

    margin-bottom:

    25px;

    box-shadow:

    0 10px 25px rgba(
    0,
    0,
    0,
    0.3
    );

    }


    .hero h1{

    color:white;

    }


    .hero p{

    color:#d1d5db;

    }



    /* METRIC CARDS */

    [data-testid="metric-container"]{

    background:

    rgba(
    255,
    255,
    255,
    0.08
    );

    backdrop-filter:

    blur(
    10px
    );

    padding:

    20px;

    border-radius:

    20px;

    box-shadow:

    0 8px 20px rgba(
    0,
    0,
    0,
    0.2
    );

    transition:
    0.3s;

    }



    [data-testid="metric-container"]:hover{


    transform:

    translateY(

    -5px

    );


    }



    /* BUTTONS */

    .stButton>button{


    background:

    linear-gradient(

    90deg,

    #2563eb,

    #7c3aed

    );


    color:white;


    border:none;


    border-radius:

    15px;


    padding:

    10px 20px;


    font-weight:bold;


    transition:

    0.3s;

    }



    .stButton>button:hover{


    background:

    linear-gradient(

    90deg,

    #7c3aed,

    #2563eb

    );


    transform:

    scale(

    1.03

    );

    }



    /* INPUTS */

    .stTextInput input,

    .stNumberInput input,

    .stSelectbox{


    background:

    #1f2937;


    color:white;

    border-radius:

    12px;

    }



    /* ALERTS */

    .stSuccess{


    background:

    #14532d;

    }


    .stWarning{


    background:

    #92400e;

    }


    .stError{


    background:

    #991b1b;

    }



    /* TABLES */

    [data-testid="stTable"]{

    background:

    rgba(
    255,
    255,
    255,
    0.05
    );

    border-radius:

    20px;

    }



    /* PROGRESS BAR */

    .stProgress > div > div{


    background:

    linear-gradient(

    90deg,

    #22c55e,

    #3b82f6

    );

    }



    /* PLOTLY CHARTS */

    .js-plotly-plot{

    background:

    rgba(
    255,
    255,
    255,
    0.03
    );

    border-radius:

    20px;

    padding:

    15px;

    }



    /* SECTION HEADINGS */

    h1{

    color:

    #f8fafc;

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