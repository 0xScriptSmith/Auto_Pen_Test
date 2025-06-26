# integrations/ffuf_runner.py
import subprocess
import shutil

def run_ffuf(target_url):
    if not shutil.which("ffuf"):
        return "[!] ffuf not found. Please install it first."

    cmd = [
        "ffuf",
        "-u", f"{target_url}/FUZZ",
        "-w", "utils/wordlists/endpoints.txt",
        "-o", "results/ffuf.json",
        "-of", "json"
    ]

    try:
        print(f"[*] Running ffuf on {target_url}")
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return f"[!] Error running ffuf: {e}"
