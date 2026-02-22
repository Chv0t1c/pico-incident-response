# Pico-W Incident Response & Stealth Sanitizer

A Raspberry Pi Pico W-based security tool designed for rapid data mitigation and forensic sanitization in compromised environments.

## Features
* **Modular Authentication Gate:** Implements a 2-stage PIN authentication (`Software_Lock.py`) before payload delivery.
* **Stealth Sanitization:** Utilizes `shred` with output redirection to `/dev/null` to eliminate digital fingerprints.
* **Auto-Self-Destruct:** Chained Linux commands ensure the terminal closes and the target directory is removed instantly after wiping.

## Project Structure
* `main.py`: The central controller/orchestrator.
* `Scripts/Software_Lock.py`: Authentication logic.
* `Scripts/Terminal_Wipe.py`: The HID payload for data destruction.

## Usage
1. Plug the Pico-W into the target analyst machine.
2. Enter the 4-digit PIN when prompted by the serial console.
3. Observe the LED sequence for 'Payload Delivered' confirmation

## Security Disclaimer
This tool is for authorized security testing and incident response only.
