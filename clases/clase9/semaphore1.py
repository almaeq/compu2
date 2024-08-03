from multiprocessing import Process, Semaphore
import time

class SharedResource:
    def __init__(self, semaphore):
        self.semaphore = semaphore

    def access_resource(self, process_id):
        with self.semaphore:  # Adquirir y liberar automáticamente el recurso
            print(f'Proceso {process_id} está accediendo al recurso')
            time.sleep(1)
    """ with self.semaphore asegura Q el semáforo se adquiera antes de acceder al 
    recurso y se libere automáticamente después. """
    
def complex_semaphore_example(shared_resource, i):
    for _ in range(3): #cada proceso accede al recurso 3 veces
        shared_resource.access_resource(i)
        time.sleep(0.5)  # Simula tiempo entre accesos

if __name__ == '__main__':
    semaphore = Semaphore(3)  # Permitir hasta 3 procesos simultáneamente
    shared_resource = SharedResource(semaphore)
    processes = [Process(target=complex_semaphore_example, args=(shared_resource, i)) for i in range(5)]
    # Se crea una lista de procesos y cada uno ejecuta la fc complex_semaphore_example
    for p in processes:
        p.start()
    for p in processes:
        p.join()