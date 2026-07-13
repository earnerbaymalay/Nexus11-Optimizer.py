import os
from core.logger import log

def ensure_admin():
    # Placeholder: on Windows, check for admin privileges before running destructive actions.
    if os.name != "nt":
        log("Admin check skipped: not running on Windows.")
        return False
    try:
        import ctypes
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    except Exception:
        return False
