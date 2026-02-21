import streamlit as st
import plotly.express as px
from ui.table_style import format_table


def _metric_options(df):
    # Keep a curated order for UX
    preferred = ["Interacciones", "Impressions", "Reach", "Views", "Posts", "ER"]
    opts = [c for c in preferred if c in df.columns]
    # Add any other numeric columns (just in case)
    for c in df.columns:
        if c not in opts and c != df.columns[0] and str(df[c].dtype).startswith(("int", "float")):
            opts.append(c)
    return opts


def render_group_tab(title: str, df, group_column: str):
    """Premium tab: controls + chart + executive insights + styled table."""

    st.markdown(
        f"""<div class="glass hero">
            <div class="pill">📌 Dimensión</div>
            <div class="hero-title" style="margin-top:.55rem;">{title}</div>
            <div class="hero-sub">Explora performance, detecta winners y compara por métricas clave.</div>
        </div>""",
        unsafe_allow_html=True,
    )

    if df is None or df.empty:
        st.warning("No hay datos disponibles para esta pestaña.")
        return

    metric_opts = _metric_options(df)
    if not metric_opts:
        st.warning("No se encontraron métricas numéricas para graficar.")
        return

    c1, c2, c3, c4 = st.columns([1.25, 1.05, 1.05, 1.15])
    with c1:
        metric = st.selectbox("Métrica", metric_opts, index=0)
    with c2:
        sort_dir = st.selectbox("Orden", ["Descendente", "Ascendente"], index=0)
    with c3:
        top_n = st.slider("Top N", min_value=5, max_value=min(30, len(df)), value=min(12, len(df)))
    with c4:
        show = st.multiselect("Mostrar", ["Gráfica", "Tabla"], default=["Gráfica", "Tabla"])

    asc = sort_dir == "Ascendente"
    work = df.sort_values(metric, ascending=asc).head(top_n) if asc else df.sort_values(metric, ascending=asc).head(top_n)
    # If descending, head() already returns top. If ascending, head() returns lowest.
    # For clearer visuals, keep the bars ordered from high->low left-to-right
    if not asc:
        work = work.sort_values(metric, ascending=True)  # so barh reads nicely
    else:
        work = work.sort_values(metric, ascending=True)

    # Executive insights
    best_row = df.sort_values(metric, ascending=False).iloc[0]
    best_name = best_row[group_column]
    best_value = best_row[metric]

    total = df[metric].sum() if metric in df.columns and metric != "ER" else None
    share_txt = ""
    if total and total != 0 and metric not in ["ER"]:
        share_txt = f" · Share: {(best_value / total):.1%}"

    st.markdown(
        f"""<div class="pill" style="margin-top:.8rem;">
        🏆 Winner: <b style="color:var(--text);">{best_name}</b> · {metric}: <b style="color:var(--text);">{best_value:,.0f}</b>{share_txt}
        </div>""",
        unsafe_allow_html=True,
    )

    if "Gráfica" in show:
        # Prefer horizontal bars for long labels (agency dashboards)
        fig = px.bar(
            work,
            x=metric,
            y=group_column,
            orientation="h",
            text=metric,
        )

        fig.update_traces(
            texttemplate="%{text:,.0f}",
            textposition="outside",
            cliponaxis=False,
        )

        fig.update_layout(
            template="plotly_dark",
            height=520,
            margin=dict(l=10, r=10, t=20, b=10),
            xaxis_title=None,
            yaxis_title=None,
        )

        st.plotly_chart(fig, use_container_width=True)

    if "Tabla" in show:
        st.dataframe(format_table(df), use_container_width=True)
