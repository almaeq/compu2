from multiprocessing import Process, Queue
""" 
Una Queue es una cola FIFO q permite a los procesos comunicarse entre sí de manera segura y eficiente. 
"""
def simple_queue_example(queue, i):
    queue.put(f'Dato del proceso {i}') #Cada proceso coloca una cadena en la cola que contiene su identificador.

def simple_queue_consumer(queue): #se ejecutará en un proceso separado para consumir los datos de la cola.
    while not queue.empty(): #El proceso consume datos de la cola mientras no esté vacía. Cada dato extraído de la cola se imprime.
        data = queue.get()
        print(f'Consumidor recibió: {data}')

if __name__ == '__main__':
    queue = Queue()
    for num in range(5):
        Process(target=simple_queue_example, args=(queue, num)).start()

    consumer_process = Process(target=simple_queue_consumer, args=(queue,)) #proceso q consume los datos de la cola
    consumer_process.start()
    consumer_process.join() #espera a que el consumidor termine de consumir los datos de la cola.


