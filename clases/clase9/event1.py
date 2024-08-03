from multiprocessing import Process, Event
import time

class SharedEventResource:
    def __init__(self, event):
        self.event = event

    def wait_for_event(self, process_id):
        print(f'Proceso {process_id} esperando evento')
        self.event.wait()
        print(f'Proceso {process_id} detectó el evento')

    def trigger_event(self): #establece el evento y notifica a todos los procesos q están esperando en event.wait().
        print('Evento establecido')
        self.event.set()

def complex_event_example(resource, i):
    if i == 0:
        time.sleep(2)
        resource.trigger_event() #establece el evento y notifica a todos los procesos q están esperando en event.wait().
    else:
        resource.wait_for_event(i) #espera a que el evento se establezca.

if __name__ == '__main__':
    event = Event()
    shared_resource = SharedEventResource(event)
    processes = [Process(target=complex_event_example, args=(shared_resource, i)) for i in range(5)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
