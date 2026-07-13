import tkinter as tk
from tkinter import ttk, scrolledtext
import threading
from core.dryrun import set_simulate
from core.logger import log, section
from core.system_restore import create_restore_point
from modules import privacy, security, networking, essentials, win11_features, updates, telemetry, debloat, speed_registry

MODULES = [
    ("Privacy", privacy),
    ("Security", security),
    ("Networking", networking),
    ("Essentials", essentials),
    ("Win11 Features", win11_features),
    ("Updates", updates),
    ("Telemetry", telemetry),
    ("Debloat (Safe)", debloat),
    ("Speed Tweaks (Safe)", speed_registry)
]

class NexusGUI:
    def __init__(self, root):
        self.root = root
        root.title("Nexus11 Optimizer")
        root.geometry("700x520")
        self.simulate_var = tk.BooleanVar(value=True)
        header = ttk.Label(root, text="Nexus11 Optimizer", font=("Segoe UI", 14, "bold"))
        header.pack(pady=8)

        frame = ttk.Frame(root)
        frame.pack(fill="x", padx=12)

        self.check_vars = {}
        for name, _ in MODULES:
            v = tk.BooleanVar(value=True)
            cb = ttk.Checkbutton(frame, text=name, variable=v)
            cb.pack(anchor="w")
            self.check_vars[name] = v

        ttk.Checkbutton(frame, text="Simulate (Dry Run)", variable=self.simulate_var).pack(anchor="w", pady=6)

        btn_frame = ttk.Frame(root)
        btn_frame.pack(fill="x", padx=12, pady=6)
        ttk.Button(btn_frame, text="Run Selected", command=self.run_selected).pack(side="left")
        ttk.Button(btn_frame, text="Create Restore Point", command=self.create_restore_point).pack(side="left", padx=8)
        ttk.Button(btn_frame, text="Rollback (Not Implemented)", command=self.rollback).pack(side="left")

        log_label = ttk.Label(root, text="Log")
        log_label.pack(anchor="w", padx=12)
        self.log_area = scrolledtext.ScrolledText(root, height=15)
        self.log_area.pack(fill="both", expand=True, padx=12, pady=6)

    def append_log(self, text):
        self.log_area.insert(tk.END, text + "\n")
        self.log_area.see(tk.END)

    def run_selected(self):
        t = threading.Thread(target=self._run_selected)
        t.start()

    def _run_selected(self):
        simulate = self.simulate_var.get()
        set_simulate(simulate)
        self.append_log("Starting run (simulate=%s)" % simulate)
        for name, module in MODULES:
            if self.check_vars[name].get():
                self.append_log(f"Applying {name}...")
                try:
                    module.apply(simulate)
                    self.append_log(f"{name} done.")
                except Exception as e:
                    self.append_log(f"Error in {name}: {e}")
        self.append_log("Run complete.")

    def create_restore_point(self):
        simulate = self.simulate_var.get()
        create_restore_point("Nexus11 GUI Restore Point", simulate)
        self.append_log("Restore point requested (simulate=%s)" % simulate)

    def rollback(self):
        self.append_log("Rollback not implemented in GUI. Use CLI rollback script when available.")

def build():
    root = tk.Tk()
    NexusGUI(root)
    root.mainloop()

if __name__ == "__main__":
    build()
