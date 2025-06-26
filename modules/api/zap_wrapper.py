# 📁 modules/api/zap_wrapper.py
import subprocess

def run(target):
    print("[*] Running OWASP ZAP Spider scan using zap-cli...")

    try:
        result = subprocess.run(
            [
                "zap-cli",
                "quick-scan",
                "--self-contained",
                "--start-options",
                "-config", "api.disablekey=true",
                target
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        return result.stdout + "\n" + result.stderr

    except FileNotFoundError:
        return "[!] Error: 'zap-cli' not found. Make sure ZAP is installed and in your PATH."

    except Exception as e:
        return f"[!] Unexpected error running ZAP: {e}"
