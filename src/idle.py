from pynput import mouse, keyboard
from datetime import datetime
# import os.path, time
# print("last modified: %s" % time.ctime(os.path.getmtime("demofile2.txt")))
# print("created: %s" % time.ctime(os.path.getctime("demofile2.txt")))



def _update_time():
    now = datetime.now()
    timestamp = datetime.timestamp(now)

    f = open("./idlefile.txt", "w")
    f.write(str(timestamp))
    f.close()
    return True

def _on_press(key):
    _update_time()
    return True
    

# Collect events until released
key_listener = keyboard.Listener(on_press = _on_press)
key_listener.start()




def _on_click(x, y, button, pressed):
    _update_time()
    return True

with mouse.Listener(
    on_click = _on_click,
) as listener:
    listener.join()


# ...or, in a non-blocking fashion:
listener = mouse.Listener(on_click = _on_click)
listener.start()
