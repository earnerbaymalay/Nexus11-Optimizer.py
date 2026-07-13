"""
PowerShell execution wrapper.
This file is intended to be run on Windows (in Python) and calls pwsh or powershell.
When executed on Linux (Codespaces) it is only stored in the repo.
"""
import subprocess
from core.logger import log, error

def run_ps(command: str, simulate: bool = False):
    """
    Run a PowerShell command. Use 'pwsh' if available, otherwise 'powershell'.
    On Windows, ensure the script runs with admin privileges when needed.
    """
    if simulate:
        log(f"[SIMULATE] PowerShell: {command}")
        return None

    exe = "pwsh"  # prefer PowerShell Core; fallback handled by caller if needed
    try:
        p = subprocess.run([exe, "-NoProfile", "-ExecutionPolicy", "Bypass", "-Command", command],
                           capture_output=True, text=True, check=False)
    except FileNotFoundError:
        # Fallback to Windows PowerShell name; on Windows this will work in many environments
        p = subprocess.run(["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-Command", command],
                           capture_output=True, text=True, check=False)

    if p.stdout:
        log(p.stdout.strip())
    if p.stderr:
        error(p.stderr.strip())
    return p
