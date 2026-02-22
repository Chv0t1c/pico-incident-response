Import time
import Scripts.Software_Lock as lock
import Scripts.Terminal_Wipe as wiper

def start_operation():
    print("--- PICO-W INCIDENT RESPONSE UNIT ---")
        
    # 1. Trigger the Authentication Gate
    # This calls the function from Software_Lock.py
    if lock.authenticate_operator():
        print("ACCESS GRANTED.")
        print("READYING PAYLOAD...")
        
        # 2. Give yourself a buffer switch to switch focus to the target window
        time.sleep(5)
        
        # 3. Trigger the Sanitization Payload
        # This calls the function in Terminal_Wipe.py
        wiper.execute_sanitization()
        
        print("OPERATION COMPLETE. DISCONNECTING...")
    else:
        print("AUTHENTICATION FAILED. LOCKING SYSTEM.")
        
