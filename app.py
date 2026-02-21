
import streamlit as st
import pandas as pd

from ui.theme import apply_theme
from components.kpi_cards import render_kpis
from ui.render_group_tab import render_group_tab

st.set_page_config(layout="wide", initial_sidebar_state="expanded")

apply_theme()

# Marca personalizable
CLIENT_NAME = st.sidebar.text_input("Nombre Cliente", "Cliente Premium")

st.title(f"📊 Dashboard Analytics — {CLIENT_NAME}")

with st.sidebar:
    st.header("📂 Cargar archivo")
    uploaded_file = st.file_uploader("Sube tu Excel", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)

    # KPIs ejemplo (espera columnas reales)
    metrics = {
        "Interacciones": df["Interacciones"].sum(),
        "Impresiones": df["Impressions"].sum(),
        "Reach": df["Reach"].sum(),
        "Views": df["Views"].sum()
    }

    render_kpis(metrics)

    tabs = st.tabs(["Plataforma", "Formato", "Título"])

    with tabs[0]:
        render_group_tab("Plataforma", df)

    with tabs[1]:
        render_group_tab("Formato", df)

    with tabs[2]:
        render_group_tab("Título", df)

else:
    st.info("Carga un archivo para comenzar.")
