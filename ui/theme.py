import streamlit as st

def apply_theme():
    st.markdown("""
    <style>
      /* Compact top padding */
      .block-container { padding-top: 1.2rem; }

      /* Card component */
      .card {
        background: rgba(255,255,255,0.03);
        border: 1px solid rgba(255,255,255,0.07);
        border-radius: 16px;
        padding: 14px 14px;
      }
      .muted { color: rgba(248,250,252,0.75); }

      /* KPI cards */
      [data-testid="metric-container"]{
        background: rgba(255,255,255,0.03);
        border: 1px solid rgba(255,255,255,0.07);
        border-radius: 16px;
        padding: 14px;
      }

      /* Make dataframe corners softer */
      [data-testid="stDataFrame"] {
        border-radius: 14px;
        overflow: hidden;
      }

      /* Tabs - more spacing */
      button[data-baseweb="tab"] { font-weight: 650; }
    </style>

    <style>
      [data-testid="stAppViewContainer"]{
        background: radial-gradient(1200px 600px at 10% 0%, rgba(6,182,212,0.10), rgba(0,0,0,0)) ,
                    radial-gradient(1200px 600px at 90% 10%, rgba(99,102,241,0.10), rgba(0,0,0,0)) ,
                    #071022 !important;
      }
      /* Slightly brighter headings */
      h1,h2,h3 { letter-spacing: -0.02em; }
      /* Subtle divider */
      hr { border-color: rgba(255,255,255,0.08) !important; }
    </style>

    """, unsafe_allow_html=True)
