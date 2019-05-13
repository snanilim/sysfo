# https://askubuntu.com/questions/728157/how-to-get-the-list-of-running-gui-applications-in-the-unity-launcher
# https://thispointer.com/python-get-list-of-all-running-processes-and-sort-by-highest-memory-usage/


# import subprocess
# import sys

# try:
#     listed = sys.argv[1]
# except IndexError:
#     listed = []

# get = lambda cmd: subprocess.check_output(cmd).decode("utf-8").strip()

# def check_wtype(w_id):
#     # check the type of window; only list "NORMAL" windows
#     return "_NET_WM_WINDOW_TYPE_NORMAL" in get(["xprop", "-id", w_id])

# def get_process(w_id):
#     # get the name of the process, owning the window
#     proc = get(["ps", "-p", w_id, "-o", "comm="])
#     proc = "gnome-terminal" if "gnome-terminal" in proc else proc
#     return proc

# wlist = [l.split() for l in subprocess.check_output(["wmctrl", "-lp"])\
#          .decode("utf-8").splitlines()]

# validprocs = set([get_process(w[2]) for w in wlist if check_wtype(w[0]) == True])

# if listed == "-list":
#     for p in validprocs:
#         print('asd', p)
# else:
#     print('dsf', validprocs)

	
# import psutil
 
# def getListOfProcessSortedByMemory():
#     '''
#     Get list of running process sorted by Memory Usage
#     '''
#     listOfProcObjects = []
#     # Iterate over the list
#     for proc in psutil.process_iter():
#        try:
#            # Fetch process details as dict
#            pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
#            pinfo['vms'] = proc.memory_info().vms / (1024 * 1024)
#            # Append dict to list
#            listOfProcObjects.append(pinfo);
#        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
#            pass
 
#     # Sort list of dict by key vms i.e. memory usage
#     listOfProcObjects = sorted(listOfProcObjects, key=lambda procObj: procObj['vms'], reverse=True)
 
#     return listOfProcObjects

# listOfRunningProcess = getListOfProcessSortedByMemory()
# for elem in listOfRunningProcess:
#     print(elem)

    

# import subprocess
# cmd = 'WMIC PROCESS get Caption,Commandline,Processid'
# proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
# for line in proc.stdout:
#     print (line)

