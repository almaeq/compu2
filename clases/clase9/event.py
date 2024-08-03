from multiprocessing import Process, Event
import time
""" 
Un Event es una señal de sincronización q permite a los procesos esperar hasta q se 
establezca (set) o restablezca (clear) una señal.
"""
def simple_event_example(event, i):
    print(f'Proceso {i} esperando evento')
    event.wait() #hace q el proceso espere hasta q el evento se establezca.
    print(f'Proceso {i} detectó el evento')

if __name__ == '__main__':
    event = Event()
    for num in range(5):
        Process(target=simple_event_example, args=(event, num)).start()

    time.sleep(2)
    print('Evento establecido')
    event.set() #establece el evento y notifica a todos los procesos q están esperando en event.wait().