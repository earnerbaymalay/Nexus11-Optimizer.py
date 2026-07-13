from core.powershell import run_ps
from core.dryrun import is_simulate
def apply(simulate=False):
    apps = [
      "7zip.7zip", "Microsoft.VisualStudioCode", "Git.Git",
      "Python.Python.3", "Mozilla.Firefox", "Google.Drive", "RiseupLabs.RiseupVPN"
    ]
    for a in apps:
        run_ps(f"winget install --id {a} -e --silent", simulate)
