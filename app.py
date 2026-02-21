
import streamlit as st
import pandas as pd

from ui.theme import apply_theme
from components.kpi_cards import render_kpis
from ui.render_group_tab import render_group_tab

st.set_page_config(layout="wide", initial_sidebar_state="expanded")
apply_theme()

with st.sidebar:
    st.header("🏷️ Branding")
    client_name = st.text_input("Nombre del Cliente", "Cliente Premium")
    subtitle = st.text_input("Subtítulo", "Social Media Performance Dashboard")

    st.divider()
    st.header("📂 Datos")
    uploaded_file = st.file_uploader("Sube tu Excel (.xlsx)", type=["xlsx"])

st.title(f"📊 {subtitle}")
st.caption(f"Cliente: **{client_name}**")

if not uploaded_file:
    st.info("Carga un archivo para comenzar.")
    st.stop()

df = pd.read_excel(uploaded_file)

# KPIs (con fallback si alguna columna no existe)
def safe_sum(col):
    return float(df[col].sum()) if col in df.columns else 0

metrics = {
    "Interacciones": safe_sum("Interacciones"),
    "Impressions": safe_sum("Impressions"),
    "Reach": safe_sum("Reach"),
    "Views": safe_sum("Views"),
}
render_kpis(metrics)

tabs = st.tabs(["Plataforma", "Formato", "Título"])

with tabs[0]:
    render_group_tab("Plataforma", df, "Platform")

with tabs[1]:
    render_group_tab("Formato", df, "Formato")

with tabs[2]:
    render_group_tab("Título", df, "Título")
