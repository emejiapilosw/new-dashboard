
import streamlit as st

def apply_theme():
    st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background: #020617;
        color: #f8fafc;
    }
    h1,h2,h3,h4,h5 { color:#ffffff !important; }
    p, span, label { color:#cbd5f5 !important; }

    [data-testid="stSidebar"] {
        background: #020617;
        border-right: 1px solid rgba(255,255,255,0.05);
    }

    [data-baseweb="input"] > div {
        background: rgba(15,23,42,0.85) !important;
        border-radius: 10px !important;
    }

    .stButton>button {
        border-radius: 12px;
        border: none;
        background: linear-gradient(90deg,#06b6d4,#6366f1);
        color: white;
        font-weight: 600;
    }

    [data-testid="metric-container"] {
        background: rgba(15,23,42,0.6);
        border-radius: 14px;
        padding: 15px;
    }
    </style>
    """, unsafe_allow_html=True)
