"""
Telemetry module: disable common telemetry services that are safe to disable.
"""
from core.powershell import run_ps
from core.logger import section, log

def apply(simulate=False):
    section("Telemetry Controls")
    # Disable Connected User Experiences and Telemetry service (safe mode)
    run_ps("sc config DiagTrack start= disabled", simulate)
    run_ps("sc stop DiagTrack", simulate)
    log("Telemetry services disabled (or simulated).")
