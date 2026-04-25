import pandas as pd


def detect_null_anomalies(file_path: str, threshold_pct: float) -> pd.DataFrame:
    df = pd.read_csv(file_path)
    rows = []
    for col in df.columns:
        null_pct = round(df[col].isna().mean() * 100, 2)
        if null_pct >= threshold_pct:
            rows.append({
                "column_name": col,
                "null_pct": null_pct,
                "threshold_pct": threshold_pct,
                "status": "ALERT"
            })
    return pd.DataFrame(rows)
