import pandas as pd


def reconcile_row_count(file_path: str, expected_min_rows: int) -> dict:
    df = pd.read_csv(file_path)
    actual_rows = len(df)
    passed = actual_rows >= expected_min_rows
    return {
        "actual_rows": actual_rows,
        "expected_min_rows": expected_min_rows,
        "passed": passed,
        "message": "Row count check passed" if passed else "Row count below threshold"
    }
