import streamlit as st

def apply_theme():

    st.markdown("""
    <style>

    /* ===== BACKGROUND ===== */
    [data-testid="stAppViewContainer"] {
        background: #0b1220;
    }

    /* ===== TEXTO GLOBAL ===== */
    html, body, [class*="css"]  {
        color: #F1F5F9 !important;
    }

    h1, h2, h3, h4, h5, h6 {
        color: #FFFFFF !important;
        font-weight: 600;
    }

    p, span, label, div {
        color: #CBD5E1 !important;
    }

    /* ===== SIDEBAR ===== */
    [data-testid="stSidebar"] {
        background: #0f172a;
        border-right: 1px solid rgba(255,255,255,0.06);
    }

    /* ===== INPUTS ===== */
    [data-baseweb="input"] > div {
        background: #1e293b !important;
        border-radius: 8px !important;
        border: 1px solid rgba(255,255,255,0.08) !important;
    }

    [data-baseweb="input"] input {
        background: transparent !important;
        color: #FFFFFF !important;
    }

    /* ===== SLIDER LABEL ===== */
    .stSlider label {
        color: #E2E8F0 !important;
    }

    /* ===== TABS ===== */
    button[data-baseweb="tab"] {
        color: #CBD5E1 !important;
        font-weight: 500;
    }

    button[data-baseweb="tab"][aria-selected="true"] {
        color: #06b6d4 !important;
    }

    /* ===== METRICS ===== */
    [data-testid="metric-container"] {
        background: #111827;
        border-radius: 12px;
        padding: 16px;
        border: 1px solid rgba(255,255,255,0.05);
    }

    /* ===== BUTTONS ===== */
    .stButton>button {
        background: linear-gradient(90deg,#06b6d4,#3b82f6);
        border-radius: 10px;
        color: white;
        border: none;
        font-weight: 600;
    }

    /* ===== DATAFRAME ===== */
    [data-testid="stDataFrame"] {
        border-radius: 12px;
    }

    </style>
    """, unsafe_allow_html=True)
