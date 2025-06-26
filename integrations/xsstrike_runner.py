# integrations/xsstrike_runner.py
import subprocess
import shutil

def run_xsstrike(target_url):
    if not shutil.which("xsstrike"):
        return "[!] XSStrike not found. Please install it first."

    cmd = [
        "xsstrike",
        "-u", target_url,
        "--crawl"
    ]

    try:
        print(f"[*] Running XSStrike on {target_url}")
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return f"[!] Error running XSStrike: {e}"
