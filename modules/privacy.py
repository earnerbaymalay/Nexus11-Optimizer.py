"""
Privacy module: non-destructive privacy hardening.
Avoids changes that break Office or Windows Update.
"""
from core.powershell import run_ps
from core.logger import section, log

def apply(simulate=False):
    section("Privacy Tweaks")
    # Examples: disable advertising ID, disable activity history sync, disable tailored experiences
    run_ps("reg add HKCU\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\AdvertisingInfo /v Enabled /t REG_DWORD /d 0 /f", simulate)
    run_ps("reg add HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\DataCollection /v AllowTelemetry /t REG_DWORD /d 0 /f", simulate)
    run_ps("reg add HKCU\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced /v ShowSyncProviderNotifications /t REG_DWORD /d 0 /f", simulate)
    log("Privacy tweaks applied (or simulated).")
