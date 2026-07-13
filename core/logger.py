from rich.console import Console
console = Console()

def log(msg):
    console.print(msg)

def error(msg):
    console.print(f"[red]{msg}")

def section(title):
    console.print(f"\n[bold cyan]{title}[/bold cyan]\n")
