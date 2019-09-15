# # https://medium.com/@leportella/how-to-run-parallel-processes-8939dafae81e
# import os                                                                       
# from multiprocessing import Pool                                                
                                                                                
                                                                                
# processes = ('process1.py', 'process3.py')                                    
# other = ('process2.py',)
                                                  
                                                                                
# def run_process(process):                                                             
#     os.system('python {}'.format(process))                                       
                                                                                
                                                                                
# pool = Pool(processes=3)                                                        
# pool.map(run_process, processes) 
# pool.map(run_process, other) 



# import os                                                                       
# from multiprocessing import Pool                                                
                                                                                
                                                                                
# processes = ('process1.py', 'process2.py', 'key-stoke.py')                                    
                                                  
                                                                                
# def run_process(process):                                                             
#     os.system('python {}'.format(process))                                       
                                                                                
                                                                                
# pool = Pool(processes=3)                                                        
# pool.map(run_process, processes) 


# import multiprocessing as mp
# print("Number of processors: ", mp.cpu_count())



from multiprocessing import Pool
from time import sleep   

# all your methods declarations above go here
# (...)

def Process1(largefile):
    import process1
    return True

def Process2(bigfile):
    print('Start of process 2')                                                                            
    sleep(10)                                                                       
    print('End of process 2')
    return True

def Process3(integer):
    print('Start of process 3')                                                                            
    sleep(10)                                                                       
    print('End of process 3')
    return True

def FinalProcess(parsed,pattern,calc_results):
    print('Start of process f')                                                                            
    sleep(10)                                                                       
    print('End of process f')
    return True

def main():
    pool = Pool(processes=3)
    parsed = pool.apply_async(Process1, ['largefile'])
    pattern = pool.apply_async(Process2, ['bigfile'])
    calc_res = pool.apply_async(Process3, ['integer'])

    pool.close()
    pool.join()

    final = FinalProcess(parsed.get(), pattern.get(), calc_res.get())

# your __main__ handler goes here
if __name__ == '__main__':
    main()

