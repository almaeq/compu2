from multiprocessing import Process, BoundedSemaphore
import time

class SharedBoundedResource:
    def __init__(self, semaphore):
        self.semaphore = semaphore

    def access_resource(self, process_id):
        with self.semaphore:
            print(f'Proceso {process_id} está accediendo al recurso')
            time.sleep(1)

def complex_bounded_semaphore_example(shared_resource, i):
    for _ in range(3): #Cada proceso accede al recurso compartido 3 veces.
        shared_resource.access_resource(i)
        time.sleep(0.5)  # Simula tiempo entre accesos

if __name__ == '__main__':
    bounded_semaphore = BoundedSemaphore(3)  # Permitir hasta 3 procesos simultáneamente
    shared_resource = SharedBoundedResource(bounded_semaphore)
    processes = [Process(target=complex_bounded_semaphore_example, args=(shared_resource, i)) for i in range(5)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
