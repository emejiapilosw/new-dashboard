from __future__ import annotations

def format_kmb(value: float, decimals: int = 2) -> str:
    """Abrevia números grandes (K/M/B) con decimales."""
    try:
        v = float(value)
    except Exception:
        return str(value)
    sign = "-" if v < 0 else ""
    v = abs(v)
    if v >= 1_000_000_000:
        return f"{sign}{v/1_000_000_000:.{decimals}f}B"
    if v >= 1_000_000:
        return f"{sign}{v/1_000_000:.{decimals}f}M"
    if v >= 1_000:
        return f"{sign}{v/1_000:.{decimals}f}K"
    if v.is_integer():
        return f"{sign}{int(v)}"
    return f"{sign}{v:.{decimals}f}"

def format_int_thousands(value: float) -> str:
    try:
        v = int(round(float(value)))
    except Exception:
        return str(value)
    return f"{v:,}"

def format_percent(value: float, decimals: int = 1) -> str:
    try:
        v = float(value)
    except Exception:
        return str(value)
    return f"{v:.{decimals}f}%"

def normalize_er_series(series):
    """Heurística: si ER viene como ratio (0-1.x) lo convertimos a %; si ya viene como % (0-100+) lo dejamos."""
    import pandas as pd
    s = pd.to_numeric(series, errors="coerce")
    if s.dropna().empty:
        return s
    q95 = s.dropna().quantile(0.95)
    if q95 <= 1.5:
        return s * 100
    return s

def format_dataframe_for_display(df):
    """
    - ER / E.R. a % (1 decimal)
    - Numéricos a enteros con separador de miles (sin decimales)
    """
    import pandas as pd
    out = df.copy()
    for col in out.columns:
        col_norm = col.strip().upper()
        if col_norm in ("ER", "E.R.", "E.R"):
            er = normalize_er_series(out[col])
            out[col] = er.map(lambda x: format_percent(x, 1) if pd.notna(x) else "")
            continue
        if pd.api.types.is_numeric_dtype(out[col]):
            s = pd.to_numeric(out[col], errors="coerce").fillna(0).round(0).astype(int)
            out[col] = s.map(lambda x: f"{x:,}")
    return out
