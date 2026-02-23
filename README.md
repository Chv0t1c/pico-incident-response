# Pico-W Incident Response & Stealth Sanitizer

A Raspberry Pi Pico W-based security tool designed for rapid data mitigation and forensic sanitization in compromised environments.

## 🛡️ Technical Project Summary
This project transforms a Raspberry Pi Pico W into a hardware-based **Incident Response & Stealth Sanitizer**. It acts as a physical "fail-safe" for security professionals to isolate and wipe sensitive data.

### 🛠️ Core Capabilities
* **Two-Factor Physical Authentication**: Implements a PIN-gate via `Software_Lock.py`, ensuring the HID payload cannot be triggered by unauthorized users.
* **Network Isolation (Air-Gapping)**: Leverages `nmcli` to programmatically disable the host's networking stack, preventing remote intervention or data exfiltration during sanitization.
* **Forensic-Grade Sanitization**: Utilizes the Linux `shred` utility to perform secure overwriting of target directories, followed by recursive deletion to eliminate metadata.
* **Stealth Execution**: Chained bash commands with output redirection to `/dev/null` ensure a minimal visual footprint on the target system.

## ✨ Features
* **Modular Authentication Gate**: Implements a 2-stage PIN authentication (`Software_Lock.py`) before payload delivery.
* **Stealth Sanitization**: Utilizes `shred` with output redirection to `/dev/null` to eliminate digital fingerprints.
* **Auto-Self-Destruct**: Chained Linux commands ensure the terminal closes and the target directory is removed instantly after wiping.

## 📂 Project Structure
* `main.py`: The central controller/orchestrator.
* `Scripts/Software_Lock.py`: Authentication logic.
* `Scripts/Terminal_Wipe.py`: The HID payload for network isolation and data destruction.
* `.gitignore`: Prevents the leakage of local libraries and sensitive tokens.

## 🚀 Usage
1.  Plug the Pico-W into the target analyst machine.
2.  Enter the 4-digit PIN when prompted by the serial console.
3.  Observe the LED sequence for 'Payload Delivered' confirmation.

## ⚠️ Security Disclaimer
This tool is for authorized security testing and incident response only.
