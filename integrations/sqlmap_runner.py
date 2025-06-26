# integrations/sqlmap_runner.py
import subprocess
import shutil

def run_sqlmap(target_url):
    if not shutil.which("sqlmap"):
        return "[!] sqlmap not found. Please install it first."

    cmd = [
        "sqlmap",
        "-u", target_url,
        "--batch",
        "--risk=2",
        "--level=3",
        "--output-dir=results/sqlmap"
    ]

    try:
        print(f"[*] Running sqlmap on {target_url}")
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return f"[!] Error running sqlmap: {e}"
