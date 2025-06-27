# Auto_Pen_Test
# 🔐 AutoPenTest - AI-Integrated Automated Pentesting Framework

AutoPenTest is an all-in-one automated penetration testing toolkit enhanced with AI (OpenAI API) to assist red teamers, bug bounty hunters, and cybersecurity professionals. It supports a range of testing modules:

- 🌍 Domain & Subdomain Recon
- 🌐 Web Application Testing
- 📡 API Security Testing
- 📱 Mobile App Analysis
- 📦 IoT Firmware Analysis
- 🖥️ OS Privilege Escalation Enumeration

> ⚠️ AI summaries are experimental and not fully functional at this stage.

---

## 📁 Project Structure

```
AutoPenTest/
├── autopentest.py             # Main entry point
├── executor.py                # Dispatches scans by mode
├── config/
│   └── settings.yaml          # Configuration file (API keys, tool paths, etc.)
├── modules/                   # All scanning logic grouped by type
│   ├── api/
│   ├── domain/
│   ├── httpx/ 
│   ├── web/
│   ├── mobile/
│   ├── iot/
│   └── os/
├── integrations/              # Lightweight wrappers around each external tool
├── results/                   # Output directory
├── auto_install_setup.sh      # One-time setup script to install all tools
├── requirements.txt           # Python dependencies
└── README.md                  # This documentation
```

---

## 🚀 Quick Start

### 🔧 Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/AutoPenTest.git
cd AutoPenTest
```

---

### 📦 Step 2: Install Python Requirements

```bash
pip install -r requirements.txt
```

---

### ⚙️ Step 3: Auto Install All External Tools

Run the auto-setup script to automatically download and install third-party tools like `sqlmap`, `amass`, `xsstrike`, `linpeas`, etc.

```bash
chmod +x auto_install_setup.sh
./auto_install_setup.sh
```

The script will:
- Download external tools from GitHub or use package managers like `apt`, `go`, and `pip`
- Make tools globally accessible or place them in the `tools/` folder
- Ensure tools like `amass`, `subfinder`, `sqlmap`, `wapiti`, `xsstrike`, etc. work without manual setup

---

### 🔐 Step 4: Add API Keys

Open and edit the file:  
`config/settings.yaml`

```yaml
# AI Support (optional)
openai_api_key: "your-openai-key-here"

# MobSF for Mobile Scanning
mobsf_api_key: "your-mobsf-api-key"
mobsf_url: "http://localhost:8000"

# Shodan for IoT Analysis
shodan_api_key: "your-shodan-api-key"
```

#### How to Get Keys:
- 🔑 OpenAI: https://platform.openai.com/account/api-keys
- 🔍 Shodan: https://account.shodan.io/
- 📱 MobSF: http://localhost:8000 (API key is shown on the dashboard)

---

## ▶️ Running the Tool

```bash
python3 autopentest.py
```

Then follow the interactive prompts:

```
Select the type of test to run:
[1] Domain
[2] Web
[3] API
[4] Mobile
[5] Operating System
[6] IoT Device
```

After entering the test type and target, AutoPenTest will automatically:
- Run related scans
- Save results in the `results/` directory
- Optionally generate an AI summary (if OpenAI API is configured)

---

## ⚙️ Advanced Configuration (`config/settings.yaml`)

You can customize tool paths, output format, proxy settings, and more:

```yaml
# === OUTPUT CONFIGURATION ===
output: results/scan_results.txt
report_format: both                # txt, html, or both
report_dir: results/reports

# === PROXY (Optional for intercepting traffic) ===
proxy: "http://127.0.0.1:8080"

# === TIMEOUTS ===
timeout: 15                        # Seconds

# === ENVIRONMENT ===
python_path: python3
```

---

## 🛠️ Supported Tools (Auto Installed)

The following tools are downloaded and configured via `auto_install_setup.sh`:

- `sqlmap` – SQL Injection Scanner
- `wapiti` – Web Vulnerability Scanner
- `XSStrike` – XSS Scanner
- `amass` – Subdomain Enumeration
- `subfinder` – Passive Recon
- `httpx` – Probe domains
- `linPEAS` – Linux privilege escalation
- `LinEnum` – Linux enumeration
- `binwalk` – Firmware analysis
- `zap-cli` – OWASP ZAP (CLI wrapper)
- `arjun` – API parameter scanner

> 🧠 AI support (OpenAI) and MobSF are optional but configurable.

---

## 🧪 Notes for Developers

- All tool logic is abstracted into `integrations/` and dispatched via `executor.py`
- Results are centralized in the `results/` folder
- Add new tools by:
  - Writing a wrapper in `integrations/`
  - Hooking it into `executor.py`
  - Updating `auto_install_setup.sh` if it requires downloading

---

## 🧱 Limitations

- AI summaries via OpenAI are currently **not fully stable** — outputs may vary or fail.
- MobSF must be **self-hosted** locally on port `8000` for APK analysis to function.
- Some tools may require **Linux-based systems** for full compatibility.

---

## 🤝 Contributions

We welcome contributions!
- Fork the repo
- Add new tools or enhancements
- Submit a pull request

---

## 📜 License

MIT License – Free to use, modify, and distribute under open-source terms.

---

## 📢 Disclaimer

AutoPenTest is intended for **educational and authorized** use only.  
Unauthorized scanning or exploitation is **strictly prohibited**.

---
