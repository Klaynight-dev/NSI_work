import multiprocessing
from multiprocessing import Process
import os

def info(title):
    print(title)
    print(f'processus :', multiprocessing.current_process().name)
    print('process id :', os.getppid())
    print('nombre de processeur :', multiprocessing.cpu_count())
    print('*'*60)

def f(name):
    info('fonction f')
    print('bonjour', name)
    
if __name__=="__main__":
    info('main')
    p1=Process(target=f, args=('David',))
    p2=Process(target=f, args=('Louise',))
    p1.start()
    p2.start()
    p1.join()
    p2.join()