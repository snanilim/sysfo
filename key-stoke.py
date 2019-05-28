from pynput import mouse, keyboard
from datetime import datetime
# import os.path, time
# print("last modified: %s" % time.ctime(os.path.getmtime("demofile2.txt")))
# print("created: %s" % time.ctime(os.path.getctime("demofile2.txt")))



def _update_time(key):
    time = datetime.strptime(format(datetime.now()), '%Y-%m-%d %H:%M:%S.%f')
    year = str(time.year)
    month = str(time.month)
    hour = str(time.hour)
    date_time = year + "-" + month + "-" + hour


    f = open(f"./idlefile-{date_time}.txt", "a")
    f.write(str(key))
    f.close()
    return True


def _on_press(key):
    check_char = hasattr(key, 'char')
    if check_char:
        _update_time(key.char)
    else:
        _update_time(key)
    return True
    

# Collect events until released
key_listener = keyboard.Listener(on_press = _on_press)
key_listener.start()




def _on_click(x, y, button, pressed):
    _update_time(button)
    return True

with mouse.Listener(
    on_click = _on_click,
) as listener:
    listener.join()


# ...or, in a non-blocking fashion:
listener = mouse.Listener(on_click = _on_click)
listener.start()
