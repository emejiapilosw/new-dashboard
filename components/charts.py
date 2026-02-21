from __future__ import annotations
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from utils.formatting import format_kmb

def bar_rank(df: pd.DataFrame, dim: str, metric: str = "Interacciones", top_n: int = 10, title: str | None = None):
    if df is None or len(df) == 0 or dim not in df.columns or metric not in df.columns:
        return None
    g = df.groupby(dim, dropna=False)[metric].sum().sort_values(ascending=False).head(top_n)
    plot_df = g.reset_index().rename(columns={metric: "value", dim: "name"})
    fig = px.bar(plot_df, x="value", y="name", orientation="h", text="value")
    fig.update_traces(texttemplate="%{text:.0f}", textposition="outside", cliponaxis=False)
    fig.update_layout(
        title=title or f"Ranking por {dim}",
        yaxis=dict(categoryorder="total ascending"),
        xaxis_title=None,
        yaxis_title=None,
        height=420,
        margin=dict(l=10, r=10, t=50, b=10),
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#f8fafc")
    )
    # abbreviate tick labels by custom hover/text
    fig.update_traces(hovertemplate=f"{dim}: %{y}<br>{metric}: %{x:,.0f}<extra></extra>")
    return fig

def donut_share(df: pd.DataFrame, dim: str, metric: str = "Interacciones", top_n: int = 6, title: str | None = None):
    if df is None or len(df) == 0 or dim not in df.columns or metric not in df.columns:
        return None
    g = df.groupby(dim, dropna=False)[metric].sum().sort_values(ascending=False).head(top_n)
    plot_df = g.reset_index()
    fig = px.pie(plot_df, names=dim, values=metric, hole=0.45)
    fig.update_layout(
        title=title or f"Distribución (Top {top_n})",
        height=420,
        margin=dict(l=10, r=10, t=50, b=10),
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#f8fafc"),
        legend_title_text=""
    )
    fig.update_traces(hovertemplate=f"{dim}: %{label}<br>{metric}: %{value:,.0f}<br>Share: %{percent}<extra></extra>")
    return fig

def pareto(df: pd.DataFrame, metric: str = "Interacciones", title: str = "Pareto 80/20 (Posts)"):
    if df is None or len(df) == 0 or metric not in df.columns:
        return None
    s = df.sort_values(metric, ascending=False)[metric].reset_index(drop=True)
    total = float(s.sum())
    if total <= 0:
        return None
    cum = s.cumsum() / total * 100.0
    x = list(range(1, len(s) + 1))
    fig = go.Figure()
    fig.add_trace(go.Bar(x=x[:50], y=s.iloc[:50], name=metric))
    fig.add_trace(go.Scatter(x=x[:50], y=cum.iloc[:50], yaxis="y2", mode="lines+markers", name="Acumulado %"))
    fig.update_layout(
        title=title,
        height=420,
        margin=dict(l=10, r=10, t=50, b=10),
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#f8fafc"),
        xaxis_title="Posts (ordenados por performance)",
        yaxis=dict(title=metric),
        yaxis2=dict(title="Acumulado %", overlaying="y", side="right", range=[0,100]),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    return fig
