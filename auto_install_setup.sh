#!/bin/bash

echo "[*] Starting AutoPenTest auto-installation setup..."

# ─────────────────────────────────────────────
# 1. Update system and install system packages
# ─────────────────────────────────────────────
echo "[*] Installing system dependencies..."
sudo apt update && sudo apt install -y \
    python3 python3-pip git curl wget unzip \
    binwalk amass dnsrecon \
    default-jre \
    zaproxy \
    httpx

# ─────────────────────────────────────────────
# 2. Install Python libraries
# ─────────────────────────────────────────────
echo "[*] Installing Python dependencies..."
pip3 install -r requirements.txt

# ─────────────────────────────────────────────
# 3. Download linpeas.sh
# ─────────────────────────────────────────────
echo "[*] Downloading linPEAS..."
curl -Lo modules/os/linpeas.sh https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh
chmod +x modules/os/linpeas.sh

# ─────────────────────────────────────────────
# 4. Download LinEnum.sh
# ─────────────────────────────────────────────
echo "[*] Downloading LinEnum..."
mkdir -p modules/os/LinEnum
curl -Lo modules/os/LinEnum/LinEnum.sh https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.sh
chmod +x modules/os/LinEnum/LinEnum.sh

# ─────────────────────────────────────────────
# 5. Download MobSF (Optional - Heavy)
# ─────────────────────────────────────────────
read -p "Do you want to auto-install MobSF locally? (y/n): " install_mobsf
if [[ "$install_mobsf" == "y" ]]; then
    echo "[*] Downloading and setting up MobSF..."
    git clone --depth 1 https://github.com/MobSF/Mobile-Security-Framework-MobSF.git mobsf
    cd mobsf
    pip3 install -r requirements.txt
    echo "[*] To start MobSF, run: cd mobsf && ./run.sh"
    cd ..
fi

# ─────────────────────────────────────────────
# 6. Cleanup and verify
# ─────────────────────────────────────────────
echo "[*] Setup complete."
echo "[✓] All necessary tools are installed or downloaded."
