from pynput import keyboard
from pynput import mouse
import os

# get initial capslock state
exit_code = os.system('''xset q 2>/dev/null | grep -q -E 'Caps Lock: +on' ''')
if exit_code == 0:
	capslock = True
else:
	capslock = False

# this function runs each time a key is pressed
def on_press(key): 
	global capslock
	output = str(key)
	if output == 'Key.caps_lock': # if capslock pressed, swap capslock state
		capslock = not capslock
	if output.startswith('Key') == False: # i.e., if output is alphanumeric
		output = output[1:-1] # remove quotes around character
		if capslock:
			output = output.swapcase()
	if output.startswith('Key.shift') == False: # i.e., ignore shift keys (e.g., we want to log a~ not aKey.shift~)
		print(output)

def on_click(x, y, button, pressed):
	button = str(button)
	if pressed:
		if button == 'Button.left':
			print('Key.mousebutton_left')

with mouse.Listener(on_click=on_click) as listener:
	with keyboard.Listener(on_press=on_press) as listener:
		listener.join()