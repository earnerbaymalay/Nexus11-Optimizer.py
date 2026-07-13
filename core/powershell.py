import subprocess
from core.logger import log, error
def run_ps(cmd, simulate=False):
    if simulate: log(f"[SIMULATE] {cmd}"); return None
    p = subprocess.run(["pwsh","-NoProfile","-ExecutionPolicy","Bypass","-Command",cmd], capture_output=True, text=True)
    log(p.stdout); 
    if p.stderr: error(p.stderr)
    return p
