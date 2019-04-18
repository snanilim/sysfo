# https://thispointer.com/python-get-list-of-all-running-processes-and-sort-by-highest-memory-usage/
# https://www.pythoncircle.com/post/535/python-script-9-getting-system-information-in-linux-using-python-script/
# Python script to fetch system information
# Author -  ThePythonDjango.Com
# Tested with Python3 on Ubuntu 16.04
# 

import platform

architecture = platform.architecture()[0]
machine = platform.machine()
user = platform.node()

allInfo = {
    'Architecture': architecture,
    'Machine': machine
}

print(f'All Info: {type(allInfo)}')
