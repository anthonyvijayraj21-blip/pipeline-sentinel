import pandas as pd
from src.count_reconciler import reconcile_row_count


def test_reconcile_row_count_pass(tmp_path):
    file_path = tmp_path / "sample.csv"
    pd.DataFrame({"id": [1, 2, 3]}).to_csv(file_path, index=False)
    result = reconcile_row_count(str(file_path), 2)
    assert result["passed"] is True
    assert result["actual_rows"] == 3
