"""
Networking module: safe network hardening options.
"""
from core.powershell import run_ps
from core.logger import section, log

def apply(simulate=False):
    section("Networking Hardening")
    # Disable LLMNR
    run_ps("reg add HKLM\\SYSTEM\\CurrentControlSet\\Services\\Dnscache\\Parameters /v EnableMulticast /t REG_DWORD /d 0 /f", simulate)
    # Disable NetBIOS over TCP/IP on all adapters (example placeholder)
    log("Networking tweaks applied (or simulated). Review adapter-specific settings on Windows.")
