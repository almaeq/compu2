from multiprocessing import Process, Barrier
import time

class SharedBarrierResource:
    def __init__(self, barrier):
        self.barrier = barrier

    def wait_at_barrier(self, process_id): #permite q un proceso espere hasta q todos los procesos en el grupo lleguen a la barrera:
        print(f'Proceso {process_id} esperando en la barrera')
        self.barrier.wait()
        print(f'Proceso {process_id} cruzó la barrera')

def complex_barrier_example(resource, i):
    time.sleep(i) #simula dif tiempos de ejecución para c/proceso antes de llegar a la barrera, demostrando cómo la barrera sincroniza la continuación de todos los procesos una vez q todos han llegado al punto de sincronización.
    resource.wait_at_barrier(i)

if __name__ == '__main__':
    barrier = Barrier(5)
    shared_resource = SharedBarrierResource(barrier)
    processes = [Process(target=complex_barrier_example, args=(shared_resource, i)) for i in range(5)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
