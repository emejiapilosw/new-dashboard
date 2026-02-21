import streamlit as st
import plotly.express as px
from utils.formatting import format_numbers

def render_group_tab(display_name, df, column_name):
    """
    display_name: etiqueta UI (ej 'Plataforma')
    column_name: nombre real de columna en el Excel (ej 'Platform')
    """
    st.subheader(display_name)

    if df is None or len(df) == 0:
        st.info("No hay datos disponibles.")
        return

    if column_name not in df.columns:
        st.error(f"No encuentro la columna '{column_name}' en el Excel.")
        return

    if "Interacciones" not in df.columns:
        st.error("No encuentro la columna 'Interacciones' en el Excel.")
        return

    # Default: ordenar por Interacciones DESC
    df = df.sort_values(by="Interacciones", ascending=False)

    top_n = st.slider(
        "Top N",
        min_value=1,
        max_value=len(df),
        value=min(12, len(df)),
        key=f"topn_{column_name}"
    )

    df_top = df.head(top_n).copy()

    # asegurar numérico para Plotly
    try:
        import pandas as pd
        df_top["Interacciones"] = pd.to_numeric(df_top["Interacciones"], errors="coerce").fillna(0)
    except Exception:
        pass

    # 📊 Barra horizontal
    fig = px.bar(
        df_top,
        x="Interacciones",
        y=column_name,
        orientation="h",
        height=460
    )
    fig.update_layout(
        yaxis=dict(categoryorder="total ascending"),
        margin=dict(l=10, r=10, t=10, b=10),
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#f8fafc"),
        xaxis_title=None,
        yaxis_title=None
    )
    st.plotly_chart(fig, use_container_width=True)

    # 🥧 Pie (top 6)
    pie_df = df_top.head(6).copy()
    pie = px.pie(pie_df, names=column_name, values="Interacciones", hole=0.35)
    pie.update_layout(
        margin=dict(l=10, r=10, t=10, b=10),
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#f8fafc"),
        legend_title_text=""
    )
    st.plotly_chart(pie, use_container_width=True)

    # 📋 Tabla (detalle)
    st.caption("Detalle (ordenado por Interacciones ↓)")
    st.dataframe(format_numbers(df.head(top_n).copy()), use_container_width=True)
