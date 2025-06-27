# 📁 modules/httpx/httpx_wrapper.py

import subprocess

def run_httpx_analysis(input_file):
    print("[*] Running HTTPX on targets from file...")
    try:
        output_file = "results/httpx_output.txt"
        result = subprocess.run(
            ["httpx", "-l", input_file, "-o", output_file],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return f"[+] HTTPX scan complete. Output saved to {output_file}\n\n{result.stdout}"
    except FileNotFoundError:
        return "[!] httpx is not installed. Please install it via:\n    go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest"
    except Exception as e:
        return f"[!] HTTPX error: {str(e)}"
