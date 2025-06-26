import subprocess
import os

RESULTS_DIR = "results"

def run_sublist3r(domain):
    print("[*] Running Sublist3r...")
    try:
        output_file = os.path.join(RESULTS_DIR, "sublist3r.txt")
        subprocess.check_output(
            ["sublist3r", "-d", domain, "-o", output_file],
            stderr=subprocess.DEVNULL
        )
        with open(output_file, "r") as f:
            return f.read()
    except Exception as e:
        return f"[!] Sublist3r failed: {str(e)}"

def run_dnsrecon(domain):
    print("[*] Running dnsrecon...")
    try:
        output = subprocess.check_output(
            ["dnsrecon", "-d", domain],
            stderr=subprocess.DEVNULL
        )
        return output.decode()
    except Exception as e:
        return f"[!] DNSRecon failed: {str(e)}"

def run_theharvester(domain):
    print("[*] Running theHarvester...")
    try:
        output = subprocess.check_output(
            ["theHarvester", "-d", domain, "-b", "all"],
            stderr=subprocess.DEVNULL
        )
        return output.decode()
    except Exception as e:
        return f"[!] theHarvester failed: {str(e)}"

def run_amass(domain):
    print("[*] Running Amass...")
    try:
        output_file = os.path.join(RESULTS_DIR, "amass.txt")
        subprocess.check_output(
            ["amass", "enum", "-d", domain, "-o", output_file],
            stderr=subprocess.DEVNULL
        )
        with open(output_file, "r") as f:
            return f.read()
    except Exception as e:
        return f"[!] Amass failed: {str(e)}"

def run_domain_recon(domain):
    results = {
        "sublist3r": run_sublist3r(domain),
        "dnsrecon": run_dnsrecon(domain),
        "theHarvester": run_theharvester(domain),
        "amass": run_amass(domain),
    }
    return results
