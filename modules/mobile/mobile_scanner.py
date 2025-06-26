# 📁 modules/mobile/mobile_scanner.py

import subprocess
import os
import requests
import yaml

CONFIG_FILE = "config/settings.yaml"

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return yaml.safe_load(f)
    else:
        return {}

def run_apkleaks(target_apk_path):
    print("[*] Running ApkLeaks...")
    try:
        result = subprocess.run([
            "apkleaks",
            "-f", target_apk_path,
            "-o", "results/apkleaks_result.json"
        ], capture_output=True, text=True)

        return result.stdout + "\n" + result.stderr
    except Exception as e:
        return f"[!] ApkLeaks failed: {e}"

def run_mobsf_analysis(target_apk_path):
    print("[*] Running MobSF analysis...")

    config = load_config()
    api_key = config.get("mobsf_api_key")
    if not api_key:
        return "[!] MobSF API key not found in config/settings.yaml"

    try:
        # Upload APK
        with open(target_apk_path, 'rb') as f:
            files = {'file': (os.path.basename(target_apk_path), f)}
            headers = {'Authorization': api_key}
            upload_url = "http://localhost:8000/api/v1/upload"
            res = requests.post(upload_url, files=files, headers=headers)
            res.raise_for_status()
            scan_hash = res.json().get("hash")

        # Scan APK
        scan_url = "http://localhost:8000/api/v1/scan"
        res = requests.post(scan_url, data={"hash": scan_hash}, headers=headers)
        res.raise_for_status()

        return res.text
    except Exception as e:
        return f"[!] MobSF analysis failed: {e}"

def run_all_mobile_scans(target_apk_path):
    results = {
        "apkleaks": run_apkleaks(target_apk_path),
        "mobsf": run_mobsf_analysis(target_apk_path)
    }
    return results
