from pathlib import Path


def check_lock(lock_file: str) -> dict:
    path = Path(lock_file)
    locked = path.exists()
    return {
        "lock_file": lock_file,
        "locked": locked,
        "message": "Another run is active" if locked else "No active lock"
    }


def create_lock(lock_file: str) -> None:
    Path(lock_file).write_text("running")


def remove_lock(lock_file: str) -> None:
    path = Path(lock_file)
    if path.exists():
        path.unlink()
