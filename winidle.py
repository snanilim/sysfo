# from ctypes import Structure, windll, c_uint, sizeof, byref

# class LASTINPUTINFO(Structure):
#     _fields_ = [
#         ('cbSize', c_uint),
#         ('dwTime', c_uint),
#     ]

# def get_idle_duration():
#     lastInputInfo = LASTINPUTINFO()
#     lastInputInfo.cbSize = sizeof(lastInputInfo)
#     windll.user32.GetLastInputInfo(byref(lastInputInfo))
#     millis = windll.kernel32.GetTickCount() - lastInputInfo.dwTime
#     return millis / 1000.0

# print(get_idle_duration())


# if platform.system() == 'Linux' :
#     from ctypes import cdll
#     self.lib = cdll.LoadLibrary("lib" + self.LIBNAME + ".so")
# elif platform.system() == 'Darwin' :
#     from ctypes import cdll
#     self.lib = cdll.LoadLibrary("lib" + self.LIBNAME + ".dylib")
# else:
#     from ctypes import windll
#     self.lib = windll.LoadLibrary(self.LIBNAME + ".dll")

import platform
if platform.system() == 'Linux':
    print('linux')
elif platform.system() == 'Windows':
    from ctypes import Structure, windll, c_uint, sizeof, byref
    
    class LASTINPUTINFO(Structure):
        _fields_ = [
            ('cbSize', c_uint),
            ('dwTime', c_uint),
        ]

    def get_idle_duration():
        lastInputInfo = LASTINPUTINFO()
        lastInputInfo.cbSize = sizeof(lastInputInfo)
        windll.user32.GetLastInputInfo(byref(lastInputInfo))
        millis = windll.kernel32.GetTickCount() - lastInputInfo.dwTime
        return millis / 1000.0

    print(get_idle_duration())