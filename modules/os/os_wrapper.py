# 📁 modules/os/os_wrapper.py
import subprocess
import os

def run_linpeas(output_path="results/linpeas_output.txt"):
    print("[*] Running linPEAS...")
    script_path = os.path.join(os.path.dirname(__file__), "linpeas.sh")
    try:
        result = subprocess.check_output(["bash", script_path], stderr=subprocess.STDOUT, timeout=600)
        with open(output_path, "wb") as f:
            f.write(result)
        return "[+] linPEAS executed successfully. Output saved."
    except subprocess.CalledProcessError as e:
        return f"[!] linPEAS failed:\n{e.output.decode()}"
    except Exception as ex:
        return f"[!] linPEAS error: {str(ex)}"

def run_linenum(output_path="results/linenum_output.txt"):
    print("[*] Running LinEnum...")
    script_path = os.path.join(os.path.dirname(__file__), "LinEnum.sh")
    try:
        result = subprocess.check_output(["bash", script_path], stderr=subprocess.STDOUT, timeout=600)
        with open(output_path, "wb") as f:
            f.write(result)
        return "[+] LinEnum executed successfully. Output saved."
    except subprocess.CalledProcessError as e:
        return f"[!] LinEnum failed:\n{e.output.decode()}"
    except Exception as ex:
        return f"[!] LinEnum error: {str(ex)}"

def run_all_os_scans():
    return {
        "linPEAS": run_linpeas(),
        "LinEnum": run_linenum()
    }
