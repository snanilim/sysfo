import psutil
import cpuinfo
import pprint
import re, uuid
import os.path, time

def _getCpuInfo():
    cpu_obj: dict = {}
    cpu_info = cpuinfo.get_cpu_info().items()
    for key, value in cpu_info:
        cpu_obj.update({key : value})
    del cpu_obj['flags']
    return cpu_obj


def _getMemoryInfo():
    memory_obj: dict = {}
    memory = psutil.virtual_memory()
    for key in memory._fields:
        value = getattr(memory, key)
        memory_obj.update({key: value})
    return memory_obj


def _getDiskInfo():
    disk_obj: dict = {}
    disk = psutil.disk_usage('/')
    for key in disk._fields:
        value = getattr(disk, key)
        disk_obj.update({key: value})
    return disk_obj


def _getProcessInfo():
    # for x in psutil.process_iter():
    #     print(x)
    process = [p.info for p in psutil.process_iter(attrs=['name', 'username'])]
    return process



def _getNetworkInfo():
    net_obj = {}
    net = psutil.net_io_counters()
    for key in net._fields:
        value = getattr(net, key)
        net_obj.update({key: value})
    return net_obj


def _getStatus():
    return "online"


def _getIdleTime():
    idle_time = time.ctime(os.path.getmtime("idlefile.txt"))
    return idle_time


def mac_addr():
    mac_addr = hex(uuid.getnode()).replace('0x', '')
    mac_addr = ':'.join(mac_addr[i : i + 2] for i in range(0, 11, 2))
    return mac_addr


def info(data):
    # print('msg', msg.split(','))
    all_info = {}

    status_value = data.get("status", "")
    if 'status' in data and status_value == 1:
        # status info
        status_info = _getStatus()
        all_info.update({'status': status_info})


    idle_value = data.get("idle", "")
    if 'idle' in data and idle_value == 1:
        # idle info
        idle_info = _getIdleTime()
        all_info.update({'idle': idle_info})


    cpu_value = data.get("cpu", "")
    if 'cpu' in data and cpu_value == 1:
        # cpu info
        cpu_info = _getCpuInfo()
        all_info.update({'cpu_info': cpu_info})


    memory_value = data.get("memory", "")
    if 'memory' in data and memory_value == 1:
        print('memory')
        # memory info
        memory_info = _getMemoryInfo()
        all_info.update({'memory_info': memory_info})


    disk_value = data.get("disk", "")
    if 'disk' in data and disk_value == 1:
        # disk info
        disk_info = _getDiskInfo()
        all_info.update({'disk_info': disk_info})


    process_value = data.get("process", "")
    if 'process' in data and process_value == 1:
        # process info
        process_info = _getProcessInfo()
        all_info.update({'process_info': process_info})


    network_value = data.get("network", "")
    if 'network' in data and network_value == 1:
        # network info
        network_info = _getNetworkInfo()
        all_info.update({'network_info': network_info})
    
    mac_addr_alue = mac_addr()
    all_info.update({'mac_addr': mac_addr_alue})

    return all_info
    # pp = pprint.PrettyPrinter(indent=4)
    # pp.pprint(all_info)


