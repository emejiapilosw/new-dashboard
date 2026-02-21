from __future__ import annotations
import pandas as pd

DATE_COL = "Date"
INT_COL = "Interacciones"
ER_COL = "E.R."

def load_excel(file) -> pd.DataFrame:
    df = pd.read_excel(file)
    # normalize Date
    if DATE_COL in df.columns:
        df[DATE_COL] = pd.to_datetime(df[DATE_COL], errors="coerce")
    # ensure numeric interacciones
    if INT_COL in df.columns:
        df[INT_COL] = pd.to_numeric(df[INT_COL], errors="coerce").fillna(0)
    # ER numeric
    if ER_COL in df.columns:
        df[ER_COL] = pd.to_numeric(df[ER_COL], errors="coerce")
    return df

def available_values(df: pd.DataFrame, col: str):
    if col not in df.columns:
        return []
    vals = df[col].dropna().astype(str).unique().tolist()
    vals.sort()
    return vals

def apply_filters(df: pd.DataFrame, filters: dict) -> pd.DataFrame:
    out = df.copy()
    for col, selected in filters.items():
        if not selected or col not in out.columns:
            continue
        out = out[out[col].astype(str).isin([str(x) for x in selected])]
    return out

def date_range_filter(df: pd.DataFrame, start, end) -> pd.DataFrame:
    if "Date" not in df.columns:
        return df
    out = df.copy()
    if start is not None:
        out = out[out["Date"] >= pd.to_datetime(start)]
    if end is not None:
        out = out[out["Date"] <= pd.to_datetime(end)]
    return out
