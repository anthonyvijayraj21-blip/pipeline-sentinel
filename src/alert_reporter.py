from pathlib import Path
import pandas as pd


def write_alert_report(output_path: str, checks: list, anomalies: pd.DataFrame) -> str:
    rows = []
    for item in checks:
        rows.append(item)
    if not anomalies.empty:
        rows.extend(anomalies.to_dict(orient="records"))
    report_df = pd.DataFrame(rows)
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    report_df.to_csv(output_path, index=False)
    return output_path
