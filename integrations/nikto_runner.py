# integrations/nikto_runner.py
import subprocess
import shutil

def run_nikto(target_url):
    if not shutil.which("nikto"):
        return "[!] nikto not found. Please install it first."

    cmd = [
        "nikto",
        "-h", target_url
    ]

    try:
        print(f"[*] Running nikto on {target_url}")
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return f"[!] Error running nikto: {e}"
