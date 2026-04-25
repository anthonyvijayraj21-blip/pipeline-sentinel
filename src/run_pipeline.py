import yaml
from src.s3_validator import validate_input_file
from src.count_reconciler import reconcile_row_count
from src.anomaly_detector import detect_null_anomalies
from src.lock_checker import check_lock, create_lock, remove_lock
from src.alert_reporter import write_alert_report


def main():
    with open("config.yaml", "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    lock_status = check_lock(config["lock_file"])
    if lock_status["locked"]:
        print("Pipeline aborted: lock exists")
        return

    create_lock(config["lock_file"])
    try:
        file_check = validate_input_file(config["raw_data_path"])
        checks = [file_check]

        if not file_check["exists"]:
            output = write_alert_report(config["alerts_output_path"], checks, anomalies=[])
            print(f"Alert report written to {output}")
            return

        count_check = reconcile_row_count(config["raw_data_path"], config["expected_min_rows"])
        checks.append(count_check)

        anomalies = detect_null_anomalies(
            config["raw_data_path"],
            config["anomaly_threshold_pct"]
        )

        output = write_alert_report(config["alerts_output_path"], checks, anomalies)
        print(f"Pipeline completed. Alert report written to {output}")
    finally:
        remove_lock(config["lock_file"])


if __name__ == "__main__":
    main()
