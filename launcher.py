import argparse
from core.dryrun import set_simulate, is_simulate
from core.system_restore import create_restore_point
from core.logger import section, log

# Import modules
from modules import privacy, security, networking, essentials, win11_features, updates, telemetry, debloat, speed_registry

def run_all(simulate=False):
    set_simulate(simulate)
    create_restore_point("Nexus11 - Pre Optimization", simulate)
    privacy.apply(simulate)
    security.apply(simulate)
    networking.apply(simulate)
    essentials.apply(simulate)
    win11_features.apply(simulate)
    updates.apply(simulate)
    telemetry.apply(simulate)
    # Debloat and speed tweaks are run in safe mode by default
    debloat.apply(simulate)
    speed_registry.apply(simulate)
    log("Nexus11 run complete.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--simulate", action="store_true", help="Dry run without applying changes")
    args = parser.parse_args()
    run_all(simulate=args.simulate)
