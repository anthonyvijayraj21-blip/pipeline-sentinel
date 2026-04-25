# pipeline-sentinel

A Python framework for ELT pipeline data quality validation.

## Overview

`pipeline-sentinel` is a lightweight data quality framework built to simulate real-world validation checks used in ELT and batch data pipelines. It helps detect common operational and data quality issues before bad data moves further downstream.

This project includes modular validation components, automated test coverage, sample data generation, and a GitHub Actions workflow for continuous integration.

## Features

- Validate whether expected input files are present and readable
- Reconcile row counts between expected and actual datasets
- Detect anomalies such as null-heavy or suspicious records
- Check lock conditions to prevent duplicate or unsafe pipeline runs
- Generate alert-style reporting for failed validation checks
- Run automated tests with `pytest`
- Execute CI checks automatically with GitHub Actions

## Tech stack

- Python 3.10
- pandas
- NumPy
- pytest
- GitHub Actions

## Project structure

```text
pipeline-sentinel/
├── .github/
│   └── workflows/
│       └── python-app.yml
├── data/
├── output/
├── src/
│   ├── __init__.py
│   ├── alert_reporter.py
│   ├── anomaly_detector.py
│   ├── count_reconciler.py
│   ├── lock_checker.py
│   └── s3_validator.py
├── tests/
│   ├── __init__.py
│   └── test_count_reconciler.py
├── .gitignore
├── config.yaml
├── createsampledata.py
├── README.md
├── requirements.txt
└── run_pipeline.py
```

## Setup

Clone the repository and install dependencies:

```bash
git clone https://github.com/anthonyvijayraj21-blip/pipeline-sentinel.git
cd pipeline-sentinel
pip install -r requirements.txt
```

## How to run

### 1. Generate sample data

```bash
python createsampledata.py
```

### 2. Run the pipeline checks

```bash
python run_pipeline.py
```

### 3. Run tests

```bash
pytest tests/ -v
```

## Validation modules

### `s3_validator.py`
Validates whether the expected input file exists and can be accessed.

### `count_reconciler.py`
Checks row-count mismatches between expected and actual datasets.

### `anomaly_detector.py`
Detects data quality issues such as unexpected null patterns or anomalies.

### `lock_checker.py`
Prevents unsafe execution by checking whether a lock condition already exists.

### `alert_reporter.py`
Builds a simple alert/report output based on validation results.

## Sample output

```text
--------------------------------------------
PIPELINE SENTINEL - DATA QUALITY REPORT
Run time: 2025-04-25 14:32:01
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

## Testing

This project includes unit testing with `pytest`.

Run the test suite with:

```bash
pytest tests/ -v
```

## CI/CD

GitHub Actions is configured through `.github/workflows/python-app.yml`. Every push and pull request to `main` runs the automated test workflow on Python 3.10. [page:16]

## Why this project matters

This project reflects common data engineering and pipeline support tasks found in production environments, including validation, reconciliation, anomaly detection, and operational safeguards.

It is designed as a practical portfolio project to demonstrate modular Python development, testability, and CI integration for data engineering workflows.

## Future improvements

- Add logging instead of print-based output
- Add support for configurable thresholds by dataset
- Extend tests for all modules
- Export validation results to CSV or HTML
- Add Docker support for reproducible execution
