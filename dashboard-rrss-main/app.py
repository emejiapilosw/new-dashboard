import streamlit as st
import pandas as pd

from analytics.engine import compute_all
from ui.kpi_cards import render_kpis
from ui.render_group_tab import render_group_tab
from ui.theme import apply_theme
from auth import login, logout


st.set_page_config(
    page_title="Dashboard RRSS",
    page_icon="📊",
    layout="wide",
)

apply_theme()

# ======================
# AUTH
# ======================
if not login():
    st.stop()

# ======================
# SIDEBAR (Agency UX)
# ======================
with st.sidebar:
    st.markdown(
        """<div class="glass hero" style="padding:1rem 1rem;">
            <div class="pill">✨ Social Media Agency</div>
            <div style="font-size:1.15rem;font-weight:800;margin-top:.6rem;">Dashboard RRSS</div>
            <div style="color:var(--muted);margin-top:.35rem;font-size:.92rem;">
                Sube tu Excel y obtén un resumen ejecutivo + comparativos por dimensión.
            </div>
        </div>""",
        unsafe_allow_html=True,
    )

    st.markdown("""<div style="height:.65rem;"></div>""", unsafe_allow_html=True)

    uploaded_file = st.file_uploader(
        "📎 Cargar reporte (Excel)",
        type=["xlsx"],
        help="Debe incluir columnas como: Platform, Interacciones, Impressions, Reach, Views, E.R., etc.",
    )

    st.markdown("""<div style="height:.2rem;"></div>""", unsafe_allow_html=True)
    st.caption(f"👤 Sesión: **{st.session_state.get('username','')}**")

    if st.button("Cerrar sesión"):
        logout()

# ======================
# HEADER
# ======================
st.markdown(
    """<div class="glass hero">
        <div class="pill">📈 Performance</div>
        <div class="hero-title" style="margin-top:.55rem;">Dashboard de Redes Sociales</div>
        <div class="hero-sub">KPIs, ranking por dimensión y una lectura rápida de qué contenido está ganando.</div>
    </div>""",
    unsafe_allow_html=True,
)

st.markdown("""<div style="height:.65rem;"></div>""", unsafe_allow_html=True)

if uploaded_file is None:
    st.info("👈 Sube tu archivo Excel desde la barra lateral para comenzar.")
    st.stop()

# ======================
# LOAD DATA
# ======================
try:
    df = pd.read_excel(uploaded_file)
except Exception:
    st.error("No pude leer el archivo. Asegúrate de que sea un Excel (.xlsx) válido.")
    st.stop()

# Basic validation (soft)
required_cols = ["Platform", "Interacciones", "Impressions", "Reach", "Views", "E.R."]
missing = [c for c in required_cols if c not in df.columns]
if missing:
    st.warning(
        "Faltan columnas esperadas en el Excel: "
        + ", ".join(missing)
        + ". Algunas métricas podrían salir vacías o fallar."
    )

results = compute_all(df)

# ======================
# OVERVIEW
# ======================
render_kpis(results)

# Executive summary cards
platform_df = results.get("platform")
format_df = results.get("format")
title_df = results.get("title")

def _best(df_, label_col, metric="Interacciones"):
    if df_ is None or df_.empty or metric not in df_.columns:
        return None, None
    r = df_.sort_values(metric, ascending=False).iloc[0]
    return r[label_col], r[metric]

c1, c2, c3 = st.columns([1, 1, 1])

best_platform, best_platform_val = _best(platform_df, "Platform", "Interacciones")
best_format, best_format_val = _best(format_df, "Formato", "Interacciones")
best_title, best_title_val = _best(title_df, "Título", "Interacciones")

with c1:
    st.markdown(
        f"""<div class="glass hero">
            <div class="pill">🏆 Top Plataforma</div>
            <div style="font-size:1.15rem;font-weight:800;margin-top:.55rem;">{best_platform or "—"}</div>
            <div style="color:var(--muted);margin-top:.25rem;">Interacciones: <b style="color:var(--text);">{(best_platform_val or 0):,.0f}</b></div>
        </div>""",
        unsafe_allow_html=True,
    )

with c2:
    st.markdown(
        f"""<div class="glass hero">
            <div class="pill">🎬 Top Formato</div>
            <div style="font-size:1.15rem;font-weight:800;margin-top:.55rem;">{best_format or "—"}</div>
            <div style="color:var(--muted);margin-top:.25rem;">Interacciones: <b style="color:var(--text);">{(best_format_val or 0):,.0f}</b></div>
        </div>""",
        unsafe_allow_html=True,
    )

with c3:
    st.markdown(
        f"""<div class="glass hero">
            <div class="pill">🏷️ Top Título</div>
            <div style="font-size:1.15rem;font-weight:800;margin-top:.55rem;">{best_title or "—"}</div>
            <div style="color:var(--muted);margin-top:.25rem;">Interacciones: <b style="color:var(--text);">{(best_title_val or 0):,.0f}</b></div>
        </div>""",
        unsafe_allow_html=True,
    )

st.markdown("""<div style="height:.35rem;"></div>""", unsafe_allow_html=True)

# ======================
# TABS
# ======================
tabs = st.tabs(
    [
        "🚀 Plataforma",
        "🧑‍🤝‍🧑 Género",
        "🎬 Formato",
        "🧩 Content Format",
        "🗂️ Content Group",
        "🏷️ Título",
    ]
)

with tabs[0]:
    render_group_tab("Plataforma", results.get("platform"), "Platform")

with tabs[1]:
    render_group_tab("Género", results.get("genre"), "Género")

with tabs[2]:
    render_group_tab("Formato", results.get("format"), "Formato")

with tabs[3]:
    render_group_tab("Content Format", results.get("content_format"), "PV_Content Format")

with tabs[4]:
    render_group_tab("Content Group", results.get("content_group"), "PV_Content Format Group")

with tabs[5]:
    render_group_tab("Título", results.get("title"), "Título")
