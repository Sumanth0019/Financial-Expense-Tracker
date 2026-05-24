import streamlit as st


def load_css():

    st.markdown(
    """
    <style>

    /* =========================
       MAIN BACKGROUND
    ========================== */

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


    /* =========================
       SIDEBAR
    ========================== */

    section[data-testid="stSidebar"]{
        background:
        linear-gradient(
        180deg,
        #111827,
        #1e3a8a
        );
        border-right:1px solid rgba(255,255,255,.08);
    }


    /* =========================
       HERO
    ========================== */

    .hero{
        background:
        linear-gradient(
        135deg,
        #2563eb,
        #7c3aed
        );
        padding:35px;
        border-radius:28px;
        box-shadow:
        0 20px 40px rgba(0,0,0,.25);
    }

    .hero h1{
        color:white;
        font-size:42px;
        font-weight:700;
    }

    .hero p{
        color:rgba(255,255,255,.85);
    }


    /* =========================
       METRICS (FIXED TEXT)
    ========================== */

    [data-testid="metric-container"]{
        background:
        rgba(255,255,255,.06);
        backdrop-filter:blur(18px);
        border:1px solid rgba(255,255,255,.08);
        border-radius:24px;
        padding:22px;
        box-shadow:
        0 8px 30px rgba(0,0,0,.25);
        transition:.25s;
    }

    [data-testid="metric-container"]:hover{
        transform:translateY(-6px);
    }

    /* THIS FIXES YOUR DARK TEXT */
    [data-testid="metric-container"] label{
        color:
        rgba(255,255,255,.75)
        !important;
    }

    [data-testid="metric-container"] div{
        color:
        white
        !important;
    }

    [data-testid="metric-container"] svg{
        fill:white !important;
    }


    /* =========================
       BUTTONS
    ========================== */

    .stButton>button{
        background:
        linear-gradient(
        90deg,
        #2563eb,
        #7c3aed
        );
        color:white;
        border:none;
        border-radius:16px;
        font-weight:700;
    }


    /* INPUTS */

    .stTextInput input,
    .stNumberInput input{
        background:#111827;
        color:white;
        border-radius:14px;
    }


    /* TABLE */

    [data-testid="stDataFrame"]{
        background:
        rgba(255,255,255,.05);
        border-radius:20px;
    }


    /* CHARTS */

    .js-plotly-plot{
        background:
        rgba(255,255,255,.03);
        border-radius:24px;
        padding:10px;
    }


    h1,h2,h3{
        color:white;
    }

    </style>
    """,
    unsafe_allow_html=True
    )
