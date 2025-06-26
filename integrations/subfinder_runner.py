# integrations/subfinder_runner.py
import subprocess
import shutil

def run_subfinder(domain):
    if not shutil.which("subfinder"):
        return "[!] Subfinder not found. Please install it first."

    cmd = [
        "subfinder",
        "-d", domain,
        "-o", "results/subfinder.txt"
    ]

    try:
        print(f"[*] Running Subfinder on {domain}")
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return f"[!] Error running Subfinder: {e}"
