from pathlib import Path


def validate_input_file(file_path: str) -> dict:
    path = Path(file_path)
    exists = path.exists()
    return {
        "file_path": str(path),
        "exists": exists,
        "size_bytes": path.stat().st_size if exists else 0,
        "message": "Input file found" if exists else "Input file missing"
    }
