
def format_kpi(value):
    if value >= 1_000_000_000:
        return f"{value/1_000_000_000:.2f}B"
    if value >= 1_000_000:
        return f"{value/1_000_000:.2f}M"
    if value >= 1_000:
        return f"{value/1_000:.2f}K"
    return f"{value}"

def format_numbers(df):
    import pandas as pd
    for col in df.columns:
        if col.upper() == "ER":
            df[col] = (df[col] * 100).map(lambda x: f"{x:.1f}%")
        elif pd.api.types.is_numeric_dtype(df[col]):
            df[col] = df[col].fillna(0).round(0).astype(int).map(lambda x: f"{x:,}")
    return df
