# import subprocess
# cmd = 'powershell "gps | where {$_.MainWindowTitle } | select Description'
# proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
# for line in proc.stdout:
#     if line.rstrip():
#         # only print lines that are not empty
#         # decode() is necessary to get rid of the binary string (b')
#         # rstrip() to remove `\r\n`
#         print(line.decode().rstrip())

import re, uuid
def mac_addr():
    mac_addr = hex(uuid.getnode()).replace('0x', '')
    mac_addr = ':'.join(mac_addr[i : i + 2] for i in range(0, 11, 2))
    return mac_addr

print(mac_addr())