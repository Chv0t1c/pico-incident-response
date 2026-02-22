# Pico-W Incident Response & Sanitization Tool
A hardware-based utility for secure environment resets during malware analysis.

## Features
* **Dual-Stage Safety:** Requires a digital PIN to 'ARM' the device before execution.
* **HID Stealth:** Utilizes standard stream redirection (`/dev/null`) to minimize terminal artifacts.
* **NIST-Aligned:** Employs `shred` logic for logical clear of target directories.

## Repository Structure
* **firmware/**: Essential .uf2 files for environment recovery.
* **scripts/**: Core logic modules (LED indicators, Terminal automation).
* **main.py**: The central 'Command Center' integrating safety gates and payloads.

## Usage
1. Plug the Pico-W into the target analyst machine.
2. Enter the 4-digit PIN when prompted by the serial console.
3. Observe the LED sequence for 'Payload Delivered' confirmation.
