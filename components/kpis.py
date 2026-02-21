from __future__ import annotations
import streamlit as st
import pandas as pd
from utils.formatting import format_kmb, normalize_er_series, format_percent

def compute_kpis(df: pd.DataFrame) -> dict:
    k = {}
    if df is None or len(df) == 0:
        return {"Interacciones": 0, "Impressions": 0, "Reach": 0, "Views": 0, "ER Promedio": 0}
    k["Interacciones"] = df["Interacciones"].sum() if "Interacciones" in df.columns else 0
    for col in ["Impressions", "Reach", "Views"]:
        k[col] = df[col].sum() if col in df.columns else 0
    if "E.R." in df.columns:
        er = normalize_er_series(df["E.R."])
        k["ER Promedio"] = float(er.mean(skipna=True)) if not er.dropna().empty else 0
    else:
        k["ER Promedio"] = 0
    return k

def render_kpis(df: pd.DataFrame):
    k = compute_kpis(df)
    cols = st.columns(5)
    cols[0].metric("Interacciones", format_kmb(k["Interacciones"]))
    cols[1].metric("Impressions", format_kmb(k["Impressions"]))
    cols[2].metric("Reach", format_kmb(k["Reach"]))
    cols[3].metric("Views", format_kmb(k["Views"]))
    cols[4].metric("ER Prom.", format_percent(k["ER Promedio"], 1))
