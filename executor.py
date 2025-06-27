# executor.py

from modules.web.web_wrapper import run_sqlmap, run_wapiti, run_xsstrike
from modules.domain.domain_wrapper import (
    run_amass,
    run_theharvester,
    run_dnsrecon,
    run_sublist3r
)
from modules.api.arjun_wrapper import run as run_arjun
from modules.api.zap_wrapper import run as run_zap_scan
from modules.os.os_wrapper import run_linpeas, run_linenum
from modules.iot.iot_wrapper import run_iot_recon
from modules.mobile.mobile_scanner import run_all_mobile_scans
from modules.httpx.httpx_wrapper import run_httpx_analysis



def run_all_web_scans(target_url):
    print("[+] Starting web-based scanning modules...")
    return {
        "sqlmap": run_sqlmap(target_url),
        "wapiti": run_wapiti(target_url),
        "xsstrike": run_xsstrike(target_url),
    }


def run_all_domain_recon(domain):
    print("[+] Starting domain-based recon modules...")
    return {
        "amass": run_amass(domain),
        "sublist3r": run_sublist3r(domain),
        "dnsrecon": run_dnsrecon(domain),
        "theHarvester": run_theharvester(domain),
    }


def run_httpx_analysis(input_file):
    print("[+] Running HTTPX analysis...")
    return run_httpx_analysis(input_file)


def run_all_mobile_scans(apk_path):
    print("[+] Starting mobile app analysis...")
    return run_all_mobile_scans(apk_path)


def run_all_iot_scans(ip=None, shodan_key=None, firmware_path=None):
    print("[+] Starting IoT scans...")
    return run_iot_recon(ip, shodan_key=shodan_key, firmware_path=firmware_path)


def run_all_os_scans():
    print("[+] Starting OS privilege escalation enumeration...")
    return {
        "linPEAS": run_linpeas(),
        "LinEnum": run_linenum(),
    }


def run_all_api_scans(target_url):
    print("[+] Starting API testing tools...")
    return {
        "arjun": run_arjun(target_url),
        "owasp_zap": run_zap_scan(target_url),
    }
