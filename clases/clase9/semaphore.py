from multiprocessing import Process, Semaphore
import time

""" 
Un Semaphore es una variable de sincronización q controla el acceso a un recurso 
con un contador. Los semáforos permiten q hasta un nº fijo de procesos accedan
simultáneamente a un recurso.
"""

def simple_semaphore_example(semaphore, i):
    semaphore.acquire()
    try:
        print(f'Proceso {i} accediendo al recurso')
        time.sleep(1)
    finally:
        semaphore.release()

if __name__ == '__main__':
    semaphore = Semaphore(2)  # Permitir hasta 2 procesos simultáneamente
    for num in range(5):
        Process(target=simple_semaphore_example, args=(semaphore, num)).start()
