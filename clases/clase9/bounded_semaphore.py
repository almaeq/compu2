from multiprocessing import Process, BoundedSemaphore
import time

""" 
Un BoundedSemaphore es similar a un Semaphore, pero con la restricción adicional de 
q no permite incrementos por encima del valor inicial. 
"""

def simple_bounded_semaphore_example(semaphore, i):
    semaphore.acquire()
    try:
        print(f'Proceso {i} accediendo al recurso')
        time.sleep(1)
    finally:
        semaphore.release()

if __name__ == '__main__':
    bounded_semaphore = BoundedSemaphore(2)  # Permitir hasta 2 procesos simultáneamente
    for num in range(5):
        Process(target=simple_bounded_semaphore_example, args=(bounded_semaphore, num)).start()