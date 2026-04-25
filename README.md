# pipeline-sentinel

A Python framework that automates ELT pipeline data quality validation.

## What it does

| Check | Description |
|-------|-------------|
| S3 Path Validation | Confirms inbound files exist, are non-empty, and arrived on time |
| Count Reconciliation | Compares source vs target row counts and flags any delta |
| Anomaly Detection | Detects statistical outliers in numeric columns using IQR |
| Lock Detection | Flags files stuck in inbound path past the expected window |

## Tech Stack

- Python 3.x
- pandas
- NumPy
- pytest

## Project Structure

```
pipeline-sentinel/
|-- .github/workflows/
|   |-- python-app.yml
|-- data/
|   |-- orders_source.csv
|   |-- orders_target.csv
|-- src/
|   |-- __init__.py
|   |-- s3_validator.py
|   |-- count_reconciler.py
|   |-- anomaly_detector.py
|   |-- lock_checker.py
|   |-- alert_reporter.py
|-- tests/
|   |-- __init__.py
|   |-- test_count_reconciler.py
|-- .gitignore
|-- config.yaml
|-- createsampledata.py
|-- requirements.txt
|-- run_pipeline.py
```

## How to run

```bash
pip install -r requirements.txt
python createsampledata.py
python run_pipeline.py
pytest tests/ -v
```

## Sample output

```
--------------------------------------------
PIPELINE SENTINEL - DATA QUALITY REPORT
Run time 2025-04-25 14:32:01
--------------------------------------------

---- CHECK 1: S3 Path Validation ----
[OK] file_exists
[OK] file_nonempty
[OK] file_is_recent
-- Overall: PASS

---- CHECK 2: Lock Detection ----
File age: 0.1 minutes
Threshold: 30 minutes
-- Overall: OK

---- CHECK 3: Count Reconciliation ----
Source rows: 1,000
Target rows: 998
Delta: 2
Source dupes: 0
Source nulls: 0
-- Overall: FAIL

---- CHECK 4: Anomaly Detection ----
Column checked: payment_value
Total rows: 1,000
Outliers found: 5 (0.5%)
Valid range: -126.84 to 434.77
-- Overall: WARN

--------------------------------------------
OVERALL PIPELINE STATUS: FAIL
--------------------------------------------
```

## Background

Built from hands-on experience working on enterprise healthcare data pipelines. This project automates the validation checks that are typically done manually in ops-heavy pipelines, turning reactive support into proactive engineering.

## CI/CD

This project uses GitHub Actions for continuous integration. Every push and pull request to `main` automatically runs the test suite with `pytest` on Python 3.10.
