# pipeline-sentinel

A Python framework for ELT pipeline data quality validation.

## Features

- Validate whether the input file exists.
- Check minimum row-count thresholds.
- Detect null-percentage anomalies.
- Prevent duplicate runs using a lock file.
- Write alert reports as CSV output.

## Project structure

```text
pipeline-sentinel/
├── src/
│   ├── s3_validator.py
│   ├── count_reconciler.py
│   ├── anomaly_detector.py
│   ├── lock_checker.py
│   └── alert_reporter.py
├── tests/
│   └── test_count_reconciler.py
├── config.yaml
├── requirements.txt
└── run_pipeline.py
```

## Setup

```bash
pip install -r requirements.txt
python run_pipeline.py
```
