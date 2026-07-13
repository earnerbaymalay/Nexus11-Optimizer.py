"""
Windows 11 feature toggles: widgets, chat, copilot, context menu options.
"""
from core.powershell import run_ps
from core.logger import section, log

def apply(simulate=False):
    section("Windows 11 Features")
    # Disable Widgets (example)
    run_ps("reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced /v TaskbarDa /t REG_DWORD /d 0 /f", simulate)
    # Disable Chat
    run_ps("reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Chat /v Enabled /t REG_DWORD /d 0 /f", simulate)
    log("Windows 11 feature toggles applied (or simulated).")
