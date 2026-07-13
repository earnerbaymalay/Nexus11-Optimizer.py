"""
Essentials installer module.
Installs core apps via winget on Windows. Respects simulate flag.
Includes Google Drive and RiseupVPN entries.
"""
from core.powershell import run_ps
from core.logger import section, log

def apply(simulate=False):
    section("Essentials Installer")
    apps = [
        ("7zip", "7zip.7zip"),
        ("VSCode", "Microsoft.VisualStudioCode"),
        ("Git", "Git.Git"),
        ("Python3", "Python.Python.3"),
        ("Firefox", "Mozilla.Firefox"),
        ("Google Drive", "Google.Drive"),
        ("RiseupVPN", "RiseupLabs.RiseupVPN")
    ]
    for name, pkg in apps:
        log(f"Installing {name} ({pkg})")
        run_ps(f"winget install --id {pkg} -e --silent", simulate)
