# Windows registry helper (placeholder). Implement with winreg in Windows runtime.
def set_reg(path,key,value,simulate=False):
    if simulate: print(f"[SIM] REG {path} {key}={value}"); return
    # actual implementation runs on Windows
