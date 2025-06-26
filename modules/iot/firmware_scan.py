# 📁 modules/iot/firmware_scan.py

import subprocess
import os

def analyze_firmware(firmware_path):
    output_dir = "results/firmware_extracted"
    os.makedirs(output_dir, exist_ok=True)

    print("[*] Starting firmware analysis using binwalk...")

    try:
        result = subprocess.run(
            ["binwalk", "-e", firmware_path, "-C", output_dir],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )

        return (
            f"[+] Firmware extracted successfully to: {output_dir}\n"
            f"{result.stdout.strip()}"
        )
    except subprocess.CalledProcessError as e:
        return f"[!] Binwalk failed:\n{e.stderr.strip()}"
    except Exception as ex:
        return f"[!] Unexpected error: {str(ex)}"
