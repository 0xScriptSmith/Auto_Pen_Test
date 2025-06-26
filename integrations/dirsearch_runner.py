# integrations/dirsearch_runner.py
import subprocess
import shutil

def run_dirsearch(target_url):
    if not shutil.which("dirsearch"):
        return "[!] dirsearch not found. Please install it first."

    cmd = [
        "dirsearch",
        "-u", target_url,
        "-e", "php,html,js",
        "-o", "results/dirsearch.txt"
    ]

    try:
        print(f"[*] Running dirsearch on {target_url}")
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return f"[!] Error running dirsearch: {e}"
