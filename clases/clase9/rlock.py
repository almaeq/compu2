from multiprocessing import Process, RLock
import time
""" 
Un RLock (Lock reentrante) permite q un mismo proceso adquiera el lock varias veces.
Necesita ser liberado el mismo número de veces que fue adquirido. 
Esto es útil cuando una fc q ya posee un bloqueo necesita llamar a otra fc q tmb
intenta adquirir el mismo bloqueo.
"""
def simple_rlock_example(rlock, i):
    rlock.acquire() #Primera adquisición del lock
    try:
        print(f'Proceso {i} primera adquisición del lock')
        rlock.acquire() #Segunda adquisición del lock
        try:
            print(f'Proceso {i} segunda adquisición del lock')
            time.sleep(1)
        finally:
            rlock.release() #Liberación del segundo lock
    finally:
        rlock.release() #Liberación del primer lock

if __name__ == '__main__':
    rlock = RLock()
    for num in range(5): #Creamos 5 procesos
        Process(target=simple_rlock_example, args=(rlock, num)).start() #Iniciamos cada proceso
