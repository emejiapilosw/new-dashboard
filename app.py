from __future__ import annotations
import streamlit as st
import pandas as pd

from ui.theme import apply_theme
from utils.data import load_excel, available_values, apply_filters, date_range_filter
from utils.formatting import format_dataframe_for_display
from components.kpis import render_kpis
from components.insights import executive_insights
from components.charts import bar_rank, donut_share, pareto

st.set_page_config(page_title="Agency Social Analytics", layout="wide", initial_sidebar_state="expanded")
apply_theme()

# --- Sidebar: Branding + Data ---
with st.sidebar:
    st.markdown("### 🏷️ Branding")
    client_name = st.text_input("Nombre del Cliente", "Cliente Premium")
    report_title = st.text_input("Título del reporte", "Social Media Analytics Dashboard")
    st.markdown("---")
    st.markdown("### 📂 Datos")
    uploaded = st.file_uploader("Sube tu Excel (.xlsx)", type=["xlsx"])

st.title(f"📊 {report_title}")
st.caption(f"Cliente: **{client_name}**")

if not uploaded:
    st.info("Carga un archivo para comenzar.")
    st.stop()

@st.cache_data(show_spinner=False)
def _load(file):
    return load_excel(file)

df = _load(uploaded)

# --- Sidebar: Filters ---
with st.sidebar:
    st.markdown("---")
    st.markdown("### 🎛️ Filtros")
    # date range
    if "Date" in df.columns and df["Date"].notna().any():
        dmin = df["Date"].min().date()
        dmax = df["Date"].max().date()
        date_start, date_end = st.date_input("Rango de fechas", value=(dmin, dmax))
    else:
        date_start, date_end = None, None

    filter_cols = [
        ("Platform", "Plataforma"),
        ("Formato", "Formato"),
        ("Year", "Año"),
        ("Month", "Mes"),
        ("Cuenta", "Cuenta"),
        ("Tipo", "Tipo"),
        ("Fase Campaña", "Fase Campaña"),
        ("Categoría", "Categoría"),
    ]

    selected = {}
    for col, label in filter_cols:
        if col in df.columns:
            opts = available_values(df, col)
            default = []
            selected[col] = st.multiselect(label, opts, default=default)

# Apply filters
df_f = date_range_filter(df, date_start, date_end)
df_f = apply_filters(df_f, selected)

# --- Executive Summary ---
st.markdown("## Resumen ejecutivo")
left, right = st.columns([1.2, 1])
with left:
    render_kpis(df_f)
    lines = executive_insights(df_f)
    st.markdown("#### Insights (auto)")
    for ln in lines:
        st.markdown(f"- {ln}")
with right:
    fig = pareto(df_f, metric="Interacciones", title="Pareto 80/20 — Interacciones por Post (Top 50)")
    if fig is not None:
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No hay suficientes datos para Pareto.")

st.markdown("---")

# --- Tabs (7) ---
tabs = st.tabs(["📌 Overview", "🧭 Plataforma", "🎞️ Formato", "🧩 Contenido", "📣 Campañas", "👥 Audiencia", "📋 Detalle"])

# Overview
with tabs[0]:
    c1, c2 = st.columns(2)
    with c1:
        fig = bar_rank(df_f, dim="Platform", top_n=10, title="Top Plataformas por Interacciones")
        if fig is not None: st.plotly_chart(fig, use_container_width=True)
        else: st.info("No hay datos para Plataforma.")
    with c2:
        fig = donut_share(df_f, dim="Formato", top_n=6, title="Mix de Formatos (Top 6)")
        if fig is not None: st.plotly_chart(fig, use_container_width=True)
        else: st.info("No hay datos para Formato.")

    st.markdown("#### Top 10 contenidos (por Interacciones)")
    if "Interacciones" in df_f.columns:
        top_posts = df_f.sort_values("Interacciones", ascending=False).head(10)
        st.dataframe(format_dataframe_for_display(top_posts), use_container_width=True)

# Plataforma
with tabs[1]:
    c1, c2 = st.columns(2)
    with c1:
        fig = bar_rank(df_f, dim="Platform", top_n=12, title="Ranking por Plataforma (Interacciones)")
        if fig is not None: st.plotly_chart(fig, use_container_width=True)
    with c2:
        fig = donut_share(df_f, dim="Platform", top_n=6, title="Share de Interacciones por Plataforma")
        if fig is not None: st.plotly_chart(fig, use_container_width=True)

# Formato
with tabs[2]:
    c1, c2 = st.columns(2)
    with c1:
        fig = bar_rank(df_f, dim="Formato", top_n=12, title="Ranking por Formato (Interacciones)")
        if fig is not None: st.plotly_chart(fig, use_container_width=True)
    with c2:
        fig = donut_share(df_f, dim="PV_Content Format Group" if "PV_Content Format Group" in df_f.columns else "Formato", top_n=6,
                          title="Distribución por Grupo de Formato")
        if fig is not None: st.plotly_chart(fig, use_container_width=True)

# Contenido
with tabs[3]:
    c1, c2 = st.columns(2)
    with c1:
        fig = bar_rank(df_f, dim="Título", top_n=12, title="Top Títulos por Interacciones")
        if fig is not None: st.plotly_chart(fig, use_container_width=True)
        else: st.info("No hay datos para Título.")
    with c2:
        fig = pareto(df_f, metric="Interacciones", title="Pareto — Concentración por Post (Top 50)")
        if fig is not None: st.plotly_chart(fig, use_container_width=True)
    st.markdown("#### Detalle de top contenidos")
    if "Título" in df_f.columns and "Interacciones" in df_f.columns:
        top = df_f.sort_values("Interacciones", ascending=False).head(25)
        cols = [c for c in ["Platform","Formato","Título","Interacciones","E.R.","Impressions","Reach","Views","Date","URL"] if c in top.columns]
        st.dataframe(format_dataframe_for_display(top[cols]), use_container_width=True)

# Campañas
with tabs[4]:
    camp_col = "Fase Campaña" if "Fase Campaña" in df_f.columns else None
    if camp_col:
        c1, c2 = st.columns(2)
        with c1:
            fig = bar_rank(df_f, dim=camp_col, top_n=12, title="Ranking por Fase de Campaña")
            if fig is not None: st.plotly_chart(fig, use_container_width=True)
        with c2:
            fig = donut_share(df_f, dim=camp_col, top_n=6, title="Share por Fase de Campaña")
            if fig is not None: st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No encuentro la columna 'Fase Campaña' en el archivo.")

# Audiencia
with tabs[5]:
    if "Seguidores" in df_f.columns:
        # Show follower distribution by platform (avg)
        tmp = df_f.copy()
        tmp["Seguidores"] = pd.to_numeric(tmp["Seguidores"], errors="coerce").fillna(0)
        if "Platform" in tmp.columns:
            g = tmp.groupby("Platform")["Seguidores"].mean().sort_values(ascending=False).reset_index()
            import plotly.express as px
            fig = px.bar(g.head(10), x="Seguidores", y="Platform", orientation="h", title="Seguidores promedio por Plataforma (Top 10)")
            fig.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)", font=dict(color="#f8fafc"))
            st.plotly_chart(fig, use_container_width=True)
        st.dataframe(format_dataframe_for_display(tmp.sort_values("Seguidores", ascending=False).head(50)), use_container_width=True)
    else:
        st.info("No encuentro la columna 'Seguidores' en el archivo.")

# Detalle
with tabs[6]:
    st.markdown("#### Tabla completa (filtrada) — orden por Interacciones ↓")
    if "Interacciones" in df_f.columns:
        df_d = df_f.sort_values("Interacciones", ascending=False).copy()
    else:
        df_d = df_f.copy()
    # Show a curated set first if exists
    preferred = [c for c in ["Platform","Cuenta","Tipo","Formato","PV_Content Format Group","Título","Interacciones","E.R.","Impressions","Reach","Views","Date","URL"] if c in df_d.columns]
    show = df_d[preferred] if preferred else df_d
    st.dataframe(format_dataframe_for_display(show), use_container_width=True)
