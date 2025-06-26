# 📁 modules/web/web_wrapper.py

import subprocess
import os

def run_sqlmap(target, output_file="results/sqlmap_output.txt"):
    print("[*] Running sqlmap...")
    try:
        result = subprocess.check_output(
            ["sqlmap", "-u", target, "--batch"],
            stderr=subprocess.STDOUT
        )
        with open(output_file, "wb") as f:
            f.write(result)
        return "[+] SQLMap completed. Output saved."
    except subprocess.CalledProcessError as e:
        return f"[!] SQLMap failed:\n{e.output.decode()}"
    except Exception as ex:
        return f"[!] SQLMap error: {str(ex)}"

def run_wapiti(target, output_dir="results/wapiti_scan/"):
    print("[*] Running Wapiti...")
    try:
        os.makedirs(output_dir, exist_ok=True)
        subprocess.run(
            ["wapiti", "-u", target, "-o", output_dir],
            check=True
        )
        return f"[+] Wapiti completed. Report saved in {output_dir}"
    except subprocess.CalledProcessError as e:
        return f"[!] Wapiti failed:\n{e}"
    except Exception as ex:
        return f"[!] Wapiti error: {str(ex)}"

def run_xsstrike(target, output_file="results/xsstrike_output.txt"):
    print("[*] Running XSStrike...")
    try:
        result = subprocess.check_output(
            ["xsstrike", "-u", target, "--crawl"],
            stderr=subprocess.STDOUT
        )
        with open(output_file, "wb") as f:
            f.write(result)
        return "[+] XSStrike completed. Output saved."
    except subprocess.CalledProcessError as e:
        return f"[!] XSStrike failed:\n{e.output.decode()}"
    except Exception as ex:
        return f"[!] XSStrike error: {str(ex)}"

def run_all_web_scans(target):
    return {
        "SQLMap": run_sqlmap(target),
        "Wapiti": run_wapiti(target),
        "XSStrike": run_xsstrike(target)
    }
