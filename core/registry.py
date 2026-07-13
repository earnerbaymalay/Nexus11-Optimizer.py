"""
Registry helper. This file is a safe wrapper for registry operations.
It uses winreg when executed on Windows. In Codespaces it remains a placeholder.
"""
import sys
from core.logger import log, error

def set_reg(hive: str, subkey: str, name: str, value, value_type="DWORD", simulate=False):
    if simulate:
        log(f"[SIMULATE] REG SET {hive}\\{subkey} : {name} = {value} ({value_type})")
        return

    if sys.platform != "win32":
        error("Registry operations require Windows. Skipping on non-Windows host.")
        return

    import winreg
    hive_map = {"HKLM": winreg.HKEY_LOCAL_MACHINE, "HKCU": winreg.HKEY_CURRENT_USER}
    h = hive_map.get(hive.upper())
    if not h:
        error(f"Unsupported hive {hive}")
        return

    try:
        with winreg.CreateKeyEx(h, subkey, 0, winreg.KEY_SET_VALUE) as key:
            if value_type == "DWORD":
                winreg.SetValueEx(key, name, 0, winreg.REG_DWORD, int(value))
            else:
                winreg.SetValueEx(key, name, 0, winreg.REG_SZ, str(value))
        log(f"REG SET {hive}\\{subkey} : {name} = {value}")
    except Exception as e:
        error(f"Failed to set registry: {e}")
