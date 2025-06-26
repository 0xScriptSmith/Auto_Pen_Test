# integrations/wpscan_runner.py
import subprocess
import shutil

def run_wpscan(target_url):
    if not shutil.which("wpscan"):
        return "[!] WPScan not found. Please install it first."

    cmd = [
        "wpscan",
        "--url", target_url,
        "--no-banner"
    ]

    try:
        print(f"[*] Running WPScan on {target_url}")
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return f"[!] Error running WPScan: {e}"
