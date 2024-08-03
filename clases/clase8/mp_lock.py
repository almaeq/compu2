from multiprocessing import Process, Lock
import os
import time

def f(l, n): #l: objeto Lock, n: numero de proceso
    l.acquire()
    print("Lanzando proceso: %d, PID %d" % (n, os.getpid()))
    for i in range(3):
        print ("hello world %d %d" % (n,i)) 
        time.sleep(1)
    l.release() #libera el bloqueo

if __name__ == '__main__':
    lock = Lock()
    procs=[] #lista de procesos

    for num in range(10): #crea 10 procesos
        procs.append(Process(target=f, args=(lock, num)))
        procs[num].start()

    for num in range(10): #espera a que cada proceso termine
        procs[num].join()