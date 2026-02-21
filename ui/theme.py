
import streamlit as st

def apply_theme():
    st.markdown("""
    <style>
      /* KPI cards */
      [data-testid="metric-container"]{
        background: rgba(15,23,42,0.78);
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 14px;
        padding: 14px;
      }

      /* Inputs */
      [data-baseweb="input"] > div{
        background: rgba(15,23,42,0.80) !important;
        border: 1px solid rgba(255,255,255,0.12) !important;
        border-radius: 10px !important;
      }
      [data-baseweb="input"] input{
        color: #f8fafc !important;
      }

      /* Tabs */
      button[data-baseweb="tab"]{ color:#cbd5e1 !important; font-weight: 600; }
      button[data-baseweb="tab"][aria-selected="true"]{ color:#06b6d4 !important; }

      /* Sidebar border */
      [data-testid="stSidebar"]{
        border-right: 1px solid rgba(255,255,255,0.08);
      }
    </style>
    """, unsafe_allow_html=True)
