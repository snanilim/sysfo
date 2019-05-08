from pynput import mouse, keyboard
from datetime import datetime
import os.path, time
print("last modified: %s" % time.ctime(os.path.getmtime("demofile2.txt")))
print("created: %s" % time.ctime(os.path.getctime("demofile2.txt")))

# Set time on Global Variables
time = 0

def _update_time():
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    global time
    time = timestamp

    f = open("demofile2.txt", "w")
    f.write("Now the file has more content!")
    f.close()

    return timestamp

def _on_press(key):
    _update_time()
    print('ZSd', time)
    return time
    

# Collect events until released
key_listener = keyboard.Listener(on_press = _on_press)
key_listener.start()




def _on_click(x, y, button, pressed):
    _update_time()
    print('aaa', time)
    return time

with mouse.Listener(
    on_click = _on_click,
) as listener:
    listener.join()


# ...or, in a non-blocking fashion:
listener = mouse.Listener(on_click = _on_click)
listener.start()


def get_idle_time():
    now = datetime.now()
    timestamp = datetime.timestamp(now)

    idle_time = timestamp - time
    return idle_time