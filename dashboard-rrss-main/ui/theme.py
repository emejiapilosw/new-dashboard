import streamlit as st

# =========================
# Brand palette (Agency-grade)
# =========================
PRIMARY = "#38bdf8"        # cyan
PRIMARY_2 = "#a78bfa"      # violet accent
SUCCESS = "#22c55e"
WARNING = "#f59e0b"
DANGER = "#fb7185"

BG_0 = "#070b16"
BG_1 = "#0b1220"
BG_2 = "#0f172a"

CARD = "rgba(15, 23, 42, 0.78)"
CARD_SOLID = "#0b1220"
BORDER = "rgba(148, 163, 184, 0.14)"

TEXT = "#f8fafc"
TEXT_2 = "#cbd5e1"
MUTED = "#94a3b8"

RADIUS = "18px"

def apply_theme() -> None:
    """Inject a premium UI theme (CSS) into Streamlit."""
    st.markdown(
        f"""
<style>
/* ===== Fonts ===== */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

:root {{
  --primary: {PRIMARY};
  --primary2: {PRIMARY_2};
  --success: {SUCCESS};
  --warning: {WARNING};
  --danger: {DANGER};

  --bg0: {BG_0};
  --bg1: {BG_1};
  --bg2: {BG_2};

  --card: {CARD};
  --border: {BORDER};
  --text: {TEXT};
  --text2: {TEXT_2};
  --muted: {MUTED};

  --radius: {RADIUS};
  --shadow: 0 10px 30px rgba(0,0,0,.35);
  --shadowSoft: 0 8px 24px rgba(0,0,0,.20);
}}

/* ===== Clean chrome ===== */
#MainMenu {{ visibility: hidden; }}
footer {{ visibility: hidden; }}
header {{ visibility: hidden; }}

/* ===== App background ===== */
[data-testid="stAppViewContainer"] {{
  background:
    radial-gradient(1200px 600px at 10% -10%, rgba(56,189,248,.20) 0%, rgba(56,189,248,0) 55%),
    radial-gradient(900px 500px at 90% 0%, rgba(167,139,250,.18) 0%, rgba(167,139,250,0) 52%),
    linear-gradient(180deg, var(--bg1) 0%, var(--bg2) 100%);
  color: var(--text);
}}

html, body, [class*="css"] {{
  font-family: 'Inter', system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif !important;
}}

/* ===== Layout spacing ===== */
.block-container {{
  padding-top: 1.75rem;
  padding-bottom: 2.5rem;
  max-width: 1400px;
}}

/* ===== Sidebar ===== */
[data-testid="stSidebar"] > div:first-child {{
  background:
    radial-gradient(900px 500px at 30% 0%, rgba(56,189,248,.10) 0%, rgba(56,189,248,0) 60%),
    linear-gradient(180deg, rgba(2,6,23,.82) 0%, rgba(2,6,23,.72) 100%);
  border-right: 1px solid var(--border);
}}

[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3,
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] label {{
  color: var(--text) !important;
}}

[data-testid="stSidebar"] .stButton>button {{
  width: 100%;
}}

/* ===== Typography ===== */
h1, h2, h3, h4 {{
  letter-spacing: -0.02em;
}}

h1 {{
  font-size: 2.15rem !important;
  line-height: 1.15 !important;
}}

[data-testid="stCaptionContainer"], .stCaption {{
  color: var(--muted) !important;
}}

/* ===== Pills & helpers ===== */
.pill {{
  display: inline-flex;
  gap: .5rem;
  align-items: center;
  padding: .35rem .65rem;
  border-radius: 999px;
  border: 1px solid var(--border);
  background: rgba(2,6,23,.45);
  color: var(--text2);
  font-size: .85rem;
}}

.glass {{
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  box-shadow: var(--shadowSoft);
  backdrop-filter: blur(10px);
}}

.hero {{
  padding: 1.1rem 1.15rem;
}}

.hero-title {{
  font-size: 2.05rem;
  font-weight: 700;
  margin: 0;
  color: var(--text);
}}

.hero-sub {{
  margin-top: .35rem;
  color: var(--muted);
}}

/* ===== Inputs ===== */
.stTextInput input,
.stNumberInput input,
.stDateInput input,
.stTextArea textarea {{
  background: rgba(2,6,23,.45) !important;
  border: 1px solid var(--border) !important;
  border-radius: 14px !important;
  color: var(--text) !important;
  padding: .65rem .75rem !important;
}}

.stTextInput input:focus,
.stNumberInput input:focus,
.stDateInput input:focus,
.stTextArea textarea:focus {{
  border-color: rgba(56,189,248,.55) !important;
  box-shadow: 0 0 0 4px rgba(56,189,248,.12) !important;
}}

[data-baseweb="select"] > div {{
  background: rgba(2,6,23,.45) !important;
  border: 1px solid var(--border) !important;
  border-radius: 14px !important;
}}

/* ===== Buttons ===== */
.stButton>button {{
  background: linear-gradient(135deg, rgba(56,189,248,.95) 0%, rgba(167,139,250,.95) 100%) !important;
  border: 0 !important;
  color: #06101a !important;
  font-weight: 700 !important;
  border-radius: 14px !important;
  padding: .6rem .85rem !important;
  box-shadow: 0 10px 24px rgba(56,189,248,.10);
  transition: transform .06s ease, filter .15s ease;
}}

.stButton>button:hover {{
  filter: brightness(1.05);
}}

.stButton>button:active {{
  transform: translateY(1px);
}}

/* Secondary (Streamlit doesn't expose easily, but we style the 'secondary' by adding a class via markdown if needed) */
.btn-secondary {{
  background: rgba(2,6,23,.55) !important;
  border: 1px solid var(--border) !important;
  color: var(--text) !important;
}}

/* ===== File uploader ===== */
[data-testid="stFileUploader"] section {{
  border: 1px dashed rgba(148,163,184,.28) !important;
  background: rgba(2,6,23,.35) !important;
  border-radius: var(--radius) !important;
  padding: 1.0rem !important;
}}

[data-testid="stFileUploader"] section:hover {{
  border-color: rgba(56,189,248,.55) !important;
}}

[data-testid="stFileUploader"] small {{
  color: var(--muted) !important;
}}

/* ===== Metrics (KPI cards) ===== */
[data-testid="metric-container"] {{
  background: var(--card) !important;
  border: 1px solid var(--border) !important;
  padding: 1.0rem 1.0rem !important;
  border-radius: var(--radius) !important;
  box-shadow: var(--shadowSoft);
}}

[data-testid="metric-container"] [data-testid="stMetricLabel"] {{
  color: var(--muted) !important;
  font-weight: 600 !important;
}}

[data-testid="metric-container"] [data-testid="stMetricValue"] {{
  color: var(--text) !important;
  font-weight: 800 !important;
  letter-spacing: -0.02em;
}}

/* ===== Tabs ===== */
button[data-baseweb="tab"] {{
  background: rgba(2,6,23,.35) !important;
  border: 1px solid var(--border) !important;
  border-radius: 999px !important;
  color: var(--text2) !important;
  font-weight: 600 !important;
  padding: .45rem .85rem !important;
  margin-right: .35rem !important;
}}

button[data-baseweb="tab"][aria-selected="true"] {{
  background: linear-gradient(135deg, rgba(56,189,248,.22) 0%, rgba(167,139,250,.18) 100%) !important;
  border-color: rgba(56,189,248,.45) !important;
  color: var(--text) !important;
}}

[data-testid="stTabs"] {{
  margin-top: .25rem;
}}

/* ===== Dataframe ===== */
[data-testid="stDataFrame"] {{
  border-radius: var(--radius) !important;
  overflow: hidden !important;
  border: 1px solid var(--border) !important;
  box-shadow: var(--shadowSoft);
}}

[data-testid="stDataFrame"] * {{
  font-family: 'Inter', system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif !important;
}}

/* ===== Alerts ===== */
[data-testid="stAlert"] {{
  border-radius: var(--radius) !important;
  border: 1px solid var(--border) !important;
  background: rgba(2,6,23,.45) !important;
}}

/* ===== Dividers ===== */
hr {{
  border-color: rgba(148,163,184,.16) !important;
}}

/* ===== Plotly chart container ===== */
.js-plotly-plot, .plotly {{
  border-radius: var(--radius);
}}

</style>
""",
        unsafe_allow_html=True,
    )
