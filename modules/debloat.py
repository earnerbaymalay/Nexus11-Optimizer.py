"""
Debloat module (Safe Mode).
Aggressiveness is intentionally conservative. Office products are protected.
"""
from core.powershell import run_ps
from core.logger import section, log

SAFE_REMOVE = [
    "Microsoft.GetHelp",
    "Microsoft.GetStarted",
    "Microsoft.People",
    "Microsoft.WindowsMaps",
    "Microsoft.XboxApp"
]

PROTECT_PATTERNS = ["Office", "Microsoft.Office", "Microsoft.365"]

def apply(simulate=False):
    section("Debloat Safe Mode")
    for pkg in SAFE_REMOVE:
        log(f"Removing {pkg}")
        run_ps(f"Get-AppxPackage -Name {pkg} | Remove-AppxPackage", simulate)
    log("Debloat safe mode complete. Office products preserved.")
