
import streamlit as st
from utils.formatting import format_kpi

def render_kpis(metrics: dict):
    cols = st.columns(len(metrics))
    for col, (name, value) in zip(cols, metrics.items()):
        col.metric(name, format_kpi(value))
