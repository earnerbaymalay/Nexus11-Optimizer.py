"""
Speed registry tweaks (Safe Profile).
These are conservative registry changes. Provide profiles for Safe/Balanced/Extreme in future.
"""
from core.registry import set_reg
from core.logger import section, log

def apply(simulate=False):
    section("Speed Registry Tweaks (Safe)")
    # Example safe tweaks
    set_reg("HKLM", r"SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management", "LargeSystemCache", 0, simulate=simulate)
    set_reg("HKCU", r"Control Panel\\Desktop", "MenuShowDelay", 100, simulate=simulate)
    log("Speed registry tweaks applied (or simulated).")
