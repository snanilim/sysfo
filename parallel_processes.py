# https://medium.com/@leportella/how-to-run-parallel-processes-8939dafae81e
import os                                                                       
from multiprocessing import Pool                                                
                                                                                
                                                                                
processes = ('process1.py', 'process3.py')                                    
other = ('process2.py',)
                                                  
                                                                                
def run_process(process):                                                             
    os.system('python {}'.format(process))                                       
                                                                                
                                                                                
pool = Pool(processes=3)                                                        
pool.map(run_process, processes) 
pool.map(run_process, other) 



# import os                                                                       
# from multiprocessing import Pool                                                
                                                                                
                                                                                
# processes = ('process1.py', 'process2.py', 'process3.py')                                    
                                                  
                                                                                
# def run_process(process):                                                             
#     os.system('python {}'.format(process))                                       
                                                                                
                                                                                
# pool = Pool(processes=3)                                                        
# pool.map(run_process, processes) 