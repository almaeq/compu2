from multiprocessing import Process, Barrier
import time
""" 
Una Barrier es una sincronización de punto de encuentro q bloquea un conj de 
procesos hasta q un nº específico de procesos hayan llegado al punto de encuentro.
eEs útil para sincronizar procesos en aplicaciones donde es necesario q todos los 
procesos alcancen un punto de ejecución específico antes de continuar.
"""
def simple_barrier_example(barrier, i):
    print(f'Proceso {i} esperando en la barrera')
    barrier.wait() #bloquea hasta q un nº específico de procesos hayan llegado al punto de encuentro.
    print(f'Proceso {i} cruzó la barrera')

if __name__ == '__main__':
    barrier = Barrier(5)
    for num in range(5):
        Process(target=simple_barrier_example, args=(barrier, num)).start()
