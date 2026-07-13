import tkinter as tk
from tkinter import ttk
def build():
    root = tk.Tk(); root.title("Nexus11")
    ttk.Label(root, text="Nexus11 Optimizer").pack()
    simulate = tk.BooleanVar()
    ttk.Checkbutton(root, text="Simulate (Dry Run)", variable=simulate).pack()
    ttk.Button(root, text="Run Selected").pack()
    root.mainloop()
if __name__=="__main__": build()
