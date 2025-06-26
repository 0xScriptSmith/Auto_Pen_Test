# integrations/nuclei_runner.py
import subprocess
import shutil

def run_nuclei(target_url):
    if not shutil.which("nuclei"):
        return "[!] nuclei not found. Please install it first."

    cmd = [
        "nuclei",
        "-u", target_url,
        "-o", "results/nuclei.txt"
    ]

    try:
        print(f"[*] Running nuclei on {target_url}")
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return f"[!] Error running nuclei: {e}"
