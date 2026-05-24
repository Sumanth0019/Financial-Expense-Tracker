import streamlit as st

def load_css():
    st.markdown("""
    <style>
    .stApp{
        background:linear-gradient(135deg,#0f172a,#1e293b,#312e81);
        color:white;
    }

    section[data-testid="stSidebar"]{
        background:linear-gradient(180deg,#111827,#1e3a8a);
        border-right:2px solid #374151;
    }

    .hero{
        background:linear-gradient(90deg,#2563eb,#7c3aed);
        padding:30px;border-radius:25px;
        box-shadow:0 10px 25px rgba(0,0,0,.3);
    }

    /* METRICS */
    [data-testid="metric-container"]{
        background:rgba(255,255,255,.08);
        backdrop-filter:blur(10px);
        border-radius:20px;
        padding:20px;
    }
    [data-testid="stMetricValue"]{
        color:white!important;
        font-weight:700!important;
    }
    [data-testid="stMetricLabel"]{
        color:rgba(255,255,255,.8)!important;
    }

    /* LABELS */
    .stTextInput label,
    .stNumberInput label,
    .stSelectbox label{
        color:white!important;
        font-weight:600!important;
    }

    /* INPUTS */
    .stTextInput input,
    .stNumberInput input{
        background:#111827!important;
        color:white!important;
        border-radius:12px!important;
    }

    /* SELECTBOX FIX */
    .stSelectbox > div > div{
        background:#111827!important;
        color:white!important;
        border-radius:14px!important;
    }

    .stSelectbox span{
        color:white!important;
    }

    .stSelectbox svg{
        fill:white!important;
    }

    div[role="listbox"]{
        background:#111827!important;
    }

    div[role="option"]{
        background:#111827!important;
        color:white!important;
    }

    div[role="option"]:hover{
        background:#2563eb!important;
    }

    .stButton>button{
        background:linear-gradient(90deg,#2563eb,#7c3aed);
        color:white;border:none;border-radius:15px;
    }

    h1{color:#f8fafc;}
    h2{color:#c084fc;}
    h3{color:#93c5fd;}
    </style>
    """, unsafe_allow_html=True)
