
import streamlit as st
import plotly.express as px
from utils.formatting import format_numbers

def render_group_tab(title, df):
    st.subheader(title)

    if df is None or len(df) == 0:
        st.info("No hay datos disponibles.")
        return

    # Orden default PRO: Interacciones DESC
    df = df.sort_values(by="Interacciones", ascending=False)

    top_n = st.slider("Top N", 1, len(df), min(10, len(df)))
    df_top = df.head(top_n)

    # Grafico barras principal
    fig = px.bar(df_top, x="Interacciones", y=title, orientation="h", height=400)
    st.plotly_chart(fig, use_container_width=True)

    # Pie chart distribución
    pie = px.pie(df_top.head(6), names=title, values="Interacciones")
    st.plotly_chart(pie, use_container_width=True)

    # Tabla detalle
    st.dataframe(format_numbers(df_top.copy()), use_container_width=True)
