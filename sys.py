import psutil
import cpuinfo
import pprint

def getCpuInfo():
    cpu_obj: dict = {}
    cpu_info = cpuinfo.get_cpu_info().items()

    for key, value in cpu_info:
        cpu_obj.update({key : value})
    
    del cpu_obj['flags']
    return cpu_obj

def getMemoryInfo():
    memory_obj: dict = {}
    memory = psutil.virtual_memory()
    # for key, value in memory:
    #     memory_obj.update({key: value})
    print(type(memory))

# def getDiskInfo():

# def getProcessInfo():

# def getNetworkInfo():

def main():
    all_info: dict = {}

    # cpu info
    cpu_info = getCpuInfo()
    all_info.update({'cpu_info': cpu_info})

    # memory info
    memory_info = getMemoryInfo()
    all_info.update({'memory_info': memory_info})

    # disk info
    disk_info = getDiskInfo()
    all_info.update({'disk_info': disk_info})

    # process info
    process_info = getProcessInfo()
    all_info.update({'process_info': process_info})

    # network info
    network_info = getNetworkInfo()
    all_info.update({'network_info': network_info})
    

    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(all_info)

main()
