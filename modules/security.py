"""
Security module: enable/verify Defender, SmartScreen, firewall rules, and ransomware protection.
"""
from core.powershell import run_ps
from core.logger import section, log

def apply(simulate=False):
    section("Security Hardening")
    # Enable SmartScreen
    run_ps("Set-MpPreference -EnableNetworkProtection Enabled", simulate)
    # Enable Controlled Folder Access (requires Defender)
    run_ps("Set-MpPreference -EnableControlledFolderAccess Enabled", simulate)
    # Ensure firewall is enabled
    run_ps("Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled True", simulate)
    log("Security hardening applied (or simulated).")
