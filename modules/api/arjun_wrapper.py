# 📁 modules/api/arjun_wrapper.py
import subprocess

def run(target):
    print("[*] Running Arjun for API parameter discovery...")
    try:
        result = subprocess.run(
            ["arjun", "-u", target],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return result.stdout + "\n" + result.stderr
    except FileNotFoundError:
        return "[!] Arjun is not installed. Please install it using: pip install arjun"
