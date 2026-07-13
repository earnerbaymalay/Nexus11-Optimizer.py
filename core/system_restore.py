"""
System restore helper. Uses PowerShell Checkpoint-Computer on Windows.
"""
from core.powershell import run_ps
from core.logger import log

def create_restore_point(description: str, simulate: bool = False):
    cmd = f"Checkpoint-Computer -Description \"{description}\" -RestorePointType \"MODIFY_SETTINGS\""
    log(f"Creating restore point: {description}")
    return run_ps(cmd, simulate)
