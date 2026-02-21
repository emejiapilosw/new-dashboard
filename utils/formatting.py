
def format_kpi(value):
    try:
        value = float(value)
    except Exception:
        return str(value)

    abs_v = abs(value)
    if abs_v >= 1_000_000_000:
        return f"{value/1_000_000_000:.2f}B"
    if abs_v >= 1_000_000:
        return f"{value/1_000_000:.2f}M"
    if abs_v >= 1_000:
        return f"{value/1_000:.2f}K"
    if abs_v.is_integer():
        return f"{int(value)}"
    return f"{value:.2f}"

def format_numbers(df):
    """
    - ER / E.R. se muestra como porcentaje con 1 decimal
    - El resto de numéricos: sin decimales y separador de miles
    """
    import pandas as pd

    for col in df.columns:
        col_norm = col.strip().upper()

        # ER (en tu archivo viene como "E.R.")
        if col_norm in ("ER", "E.R.", "E.R"):
            # si ya viene en porcentaje (ej 5.2) no lo sabemos; asumimos 0-1 como ratio
            s = pd.to_numeric(df[col], errors="coerce")
            if s.dropna().empty:
                continue
            # Heurística: si el 95% es <= 1.5 asumimos ratio y multiplicamos por 100
            q95 = s.dropna().quantile(0.95)
            if q95 <= 1.5:
                df[col] = (s * 100).map(lambda x: f"{x:.1f}%" if pd.notna(x) else "")
            else:
                df[col] = s.map(lambda x: f"{x:.1f}%" if pd.notna(x) else "")
            continue

        if pd.api.types.is_numeric_dtype(df[col]):
            s = pd.to_numeric(df[col], errors="coerce").fillna(0).round(0).astype(int)
            df[col] = s.map(lambda x: f"{x:,}")

    return df
