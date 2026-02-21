import streamlit as st

def apply_theme():
    st.markdown("""
    <style>

    /* HIGH CONTRAST GLOBAL TEXT */
    html, body, [class*="css"] {
        color:#FFFFFF !important;
    }

    h1,h2,h3,h4,h5 {
        color:#FFFFFF !important;
        font-weight:700 !important;
    }

    p, span, label {
        color:#E2E8F0 !important;
        font-size:15px !important;
    }

    /* Make KPI readable */
    [data-testid="metric-container"]{
        background:#0f172a !important;
        border:1px solid rgba(255,255,255,0.15);
        border-radius:14px;
        padding:16px;
    }

    /* Improve plot visibility */
    .js-plotly-plot{
        background:#020617 !important;
    }

    /* Sidebar stronger contrast */
    [data-testid="stSidebar"]{
        background:#020617 !important;
    }

    </style>
    """, unsafe_allow_html=True)
