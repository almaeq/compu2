from multiprocessing import Process, Queue
import time

class SharedQueueResource:
    def __init__(self, queue):
        self.queue = queue

    def produce_data(self, process_id):
        for i in range(3): #Coloca 3 elementos en la cola, cada uno con un identificador del proceso.
            data = f'Dato {i} del proceso {process_id}'
            print(f'Produciendo: {data}')
            self.queue.put(data)
            time.sleep(1)

    def consume_data(self): #Extrae elementos de la cola hasta q recibe un None, lo que indica q no hay más datos por procesar.
        while True:
            data = self.queue.get()
            if data is None:
                break
            print(f'Consumiendo: {data}')

def complex_queue_producer(resource, i):
    resource.produce_data(i)

def complex_queue_consumer(resource):
    resource.consume_data()

if __name__ == '__main__':
    queue = Queue()
    shared_resource = SharedQueueResource(queue)
    producers = [Process(target=complex_queue_producer, args=(shared_resource, i)) for i in range(3)] #3 procesos produciendo datos en la cola.
    consumer = Process(target=complex_queue_consumer, args=(shared_resource,)) #Se crea e inicia un proceso consumidor

    for p in producers:
        p.start()
    consumer.start()

    for p in producers:
        p.join() #El proceso principal espera a que todos los procesos productores terminen.
    queue.put(None)  # Señal para detener el consumidor
    consumer.join()

