SIMULATE = False

def set_simulate(v: bool):
    global SIMULATE
    SIMULATE = bool(v)

def is_simulate() -> bool:
    return SIMULATE
