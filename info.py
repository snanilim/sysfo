# https://thispointer.com/python-get-list-of-all-running-processes-and-sort-by-highest-memory-usage/
# https://www.pythoncircle.com/post/535/python-script-9-getting-system-information-in-linux-using-python-script/
# http://www.steves-internet-guide.com/into-mqtt-python-client/
# https://mntolia.com/sample-page/
# https://www.ev3dev.org/docs/tutorials/sending-and-receiving-messages-with-mqtt/
# Python script to fetch system information
# Author -  ThePythonDjango.Com
# Tested with Python3 on Ubuntu 16.04
# 

import platform
import distro
import cpuinfo
import psutil

architecture = platform.architecture()[0]
machine = platform.machine()
user = platform.node()
system = platform.system()
dist = distro.linux_distribution()
dist = " ".join(x for x in dist)

for key, value in cpuinfo.get_cpu_info().items():
    print(f"{key}: {value}")
# print(info)

allInfo: dict = {
    'architecture': architecture, 
    'machine': machine,
    'userName': user,
    'system': system,
    'distribution': dist
}

# print(f"All Info: {allInfo}")

# for proc in psutil.process_iter():
#     try:
#         # Get process name & pid from process object.
#         processName = proc.name()
#         processID = proc.pid
#         print(proc)
#     except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
#         pass

# mem = psutil.virtual_memory()
# disk = psutil.disk_usage('/')
# net = psutil.net_io_counters()
# print(mem)
# print(disk)
# print(net)
