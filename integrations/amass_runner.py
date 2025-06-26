# integrations/amass_runner.py
import subprocess
import shutil

def run_amass(domain):
    if not shutil.which("amass"):
        return "[!] Amass not found. Please install it first."

    cmd = [
        "amass",
        "enum",
        "-d", domain,
        "-o", "results/amass.txt"
    ]

    try:
        print(f"[*] Running Amass on {domain}")
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return f"[!] Error running Amass: {e}"
