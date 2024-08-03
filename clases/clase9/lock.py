from multiprocessing import Process, Lock
import time
""" 
Un Lock es una primitiva de sincronización simple q permite asegurar q solo un 
proceso acceda a un recurso compartido a la vez. Es similar a un cerrojo: una vez 
adquirido, ningún otro proceso puede adquirirlo hasta que sea liberado. """
def simple_lock_example(lock, i):
    lock.acquire() # bloquea hasta que se libere la sección crítica
    try:
        print(f'Proceso {i} accediendo a la sección crítica') 
        time.sleep(1)
    finally:
        lock.release() # libera la sección crítica

if __name__ == '__main__':
    lock = Lock()
    for num in range(5): # creamos 5 procesos
        Process(target=simple_lock_example, args=(lock, num)).start()