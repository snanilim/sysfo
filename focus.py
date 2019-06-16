# import sys
# import os
# import subprocess
# import re

# def get_active_window_title():
#     root = subprocess.Popen(['xprop', '-root', '_NET_ACTIVE_WINDOW'], stdout=subprocess.PIPE)
#     stdout, stderr = root.communicate()
    

#     m = re.search(b'^_NET_ACTIVE_WINDOW.* ([\w]+)$', stdout)
#     if m != None:
#         window_id = m.group(1)
#         window = subprocess.Popen(['xprop', '-id', window_id, 'WM_NAME'], stdout=subprocess.PIPE)
#         stdout, stderr = window.communicate()
#     else:
#         return None

#     match = re.match(b"WM_NAME\(\w+\) = (?P<name>.+)$", stdout)
#     print(match)
#     if match != None:
#         title = match.group("name")
#         print(type(title))
#         return match.group("name").strip(b'"')

#     return None

# if __name__ == "__main__":
#     print(get_active_window_title())



# import win32gui
# w=win32gui
# w.GetWindowText (w.GetForegroundWindow())


# import Xlib
# import Xlib.display

# disp = Xlib.display.Display()
# root = disp.screen().root

# NET_WM_NAME = disp.intern_atom('_NET_WM_NAME')
# NET_ACTIVE_WINDOW = disp.intern_atom('_NET_ACTIVE_WINDOW')

# root.change_attributes(event_mask=Xlib.X.FocusChangeMask)
# while True:
#     try:
#         window_id = root.get_full_property(NET_ACTIVE_WINDOW, Xlib.X.AnyPropertyType).value[0]
#         window = disp.create_resource_object('window', window_id)
#         window.change_attributes(event_mask=Xlib.X.PropertyChangeMask)
#         window_name = window.get_full_property(NET_WM_NAME, 0).value
#     except Xlib.error.XError:
#         window_name = None
#     print(window_name)
#     event = disp.next_event()


# import Xlib
# import Xlib.display

# display = Xlib.display.Display()
# screen = display.screen()
# root = screen.root
# tree = root.query_tree()
# wins = tree.children

# for win in wins:
#     print(win.get_wm_name())