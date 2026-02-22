import time

# --- SAFETY PARAMETERS ---
SYSTEM_ARMED = False
SECRET_PIN = "7788"  # You can change this later

print("--- PICO-W INCIDENT RESPONSE SYSTEM ---")
print("Status: STANDBY (Safety Engaged)")

while True:
    if not SYSTEM_ARMED:
        # Stage 1: The "Wake Up" Command
        cmd = input("Type 'ARM' to begin authentication: ").strip().upper()
        if cmd == "ARM":
            SYSTEM_ARMED = True
            print("SYSTEM ARMED. Awaiting PIN...")
        else:
            print("Invalid Command. System remains in STANDBY.")

    else:
        # Stage 2: The Identity Check
        pin_attempt = input("ENTER 4-DIGIT AUTHORIZATION PIN: ")
        
        if pin_attempt == SECRET_PIN:
            print("AUTH GRANTED. Targeted wipe initiating in 5 seconds...")
            print("Press Ctrl+C now to ABORT.")
            time.sleep(5)
            
            # --- YOUR WIPE LOGIC GOES HERE ---
            print(">>> EXECUTING SHRED COMMANDS <<<")
            # (Insert your HID keyboard commands here)
            
            # Reset after finish
            SYSTEM_ARMED = False 
            print("\nSanitization Complete. System returning to STANDBY.")
        else:
            print("ACCESS DENIED. Disarming system for security.")
            SYSTEM_ARMED = False # Force them to start over
            time.sleep(2)
