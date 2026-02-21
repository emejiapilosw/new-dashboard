from __future__ import annotations
import pandas as pd
from utils.formatting import format_kmb, normalize_er_series, format_percent

def safe_share(part, total):
    try:
        return float(part)/float(total) if total else 0.0
    except Exception:
        return 0.0

def executive_insights(df: pd.DataFrame) -> list[str]:
    if df is None or len(df) == 0:
        return ["No hay datos después de aplicar filtros."]

    total_int = df["Interacciones"].sum() if "Interacciones" in df.columns else 0

    lines = []

    # Dominant platform share
    if "Platform" in df.columns and "Interacciones" in df.columns and total_int:
        g = df.groupby("Platform", dropna=False)["Interacciones"].sum().sort_values(ascending=False)
        top = g.index[0]
        share = safe_share(g.iloc[0], total_int)
        lines.append(f"**{top}** concentra **{share*100:.1f}%** de las interacciones del periodo filtrado.")

    # Winning format
    if "Formato" in df.columns and "Interacciones" in df.columns and total_int:
        g = df.groupby("Formato", dropna=False)["Interacciones"].sum().sort_values(ascending=False)
        top = g.index[0]
        lines.append(f"El formato con mejor desempeño es **{top}** con **{format_kmb(g.iloc[0])}** interacciones.")

    # Top post
    if "Título" in df.columns and "Interacciones" in df.columns and len(df) > 0:
        top_row = df.sort_values("Interacciones", ascending=False).iloc[0]
        title = str(top_row.get("Título", "Top post"))
        val = top_row.get("Interacciones", 0)
        lines.append(f"El contenido #1 es **“{title}”** con **{format_kmb(val)}** interacciones.")

    # Pareto top 5 contribution
    if "Interacciones" in df.columns and total_int and len(df) >= 5:
        top5 = df.sort_values("Interacciones", ascending=False).head(5)["Interacciones"].sum()
        lines.append(f"El **Top 5** posts explica **{safe_share(top5, total_int)*100:.1f}%** de las interacciones totales.")
    
    # ER avg
    if "E.R." in df.columns:
        er = normalize_er_series(df["E.R."])
        if not er.dropna().empty:
            lines.append(f"ER promedio del periodo: **{format_percent(er.mean(), 1)}**.")

    return lines[:5]
