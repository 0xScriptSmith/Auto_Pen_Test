# integrations/httpx_runner.py
import subprocess
import shutil

def run_httpx(input_file):
    if not shutil.which("httpx"):
        return "[!] HTTPX not found. Please install it first."

    cmd = [
        "httpx",
        "-l", input_file,
        "-o", "results/httpx.txt",
        "--tech-detect",
        "--status-code",
        "--title"
    ]

    try:
        print(f"[*] Running HTTPX on URLs from {input_file}")
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return f"[!] Error running HTTPX: {e}"
