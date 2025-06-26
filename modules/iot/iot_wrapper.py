# 📁 modules/iot/iot_wrapper.py

from modules.iot.firmware_scan import analyze_firmware
from modules.iot.shodan_scan import shodan_lookup

def run_iot_recon(target=None, shodan_key=None, firmware_path=None):
    results = {}

    if firmware_path and firmware_path.strip():
        print("[*] Running firmware analysis...")
        results["firmware_analysis"] = analyze_firmware(firmware_path)
    
    if shodan_key and target:
        print("[*] Running Shodan analysis...")
        results["shodan"] = shodan_lookup(target, shodan_key)
    elif shodan_key and not target:
        results["shodan"] = "[!] Shodan key provided but target is missing."

    if not results:
        results["info"] = "[!] No analysis ran. Please provide a firmware path or a Shodan API key + target."

    return results
