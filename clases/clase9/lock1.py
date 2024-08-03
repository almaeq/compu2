from multiprocessing import Process, Lock,Value
import time
""" 
El valor final del contador es 0
"""
class SharedCounter:
    def __init__(self, lock):
        self.lock = lock
        self.value = 0

    def increment(self):
        with self.lock:  # Bloquea hasta que se libere la sección crítica
            temp = self.value
            time.sleep(0.1)  # Simula una operación compleja
            self.value = temp + 1

def complex_lock_example(counter, i):
    for _ in range(10): #Cada proceso incrementa el contador compartido 10 veces.
        counter.increment()
    print(f'Proceso {i} valor del contador: {counter.value}') #Imprimimos el valor del contador del proceso

if __name__ == '__main__':
    lock = Lock()
    counter = SharedCounter(lock)
    processes = [Process(target=complex_lock_example, args=(counter, i)) for i in range(5)] #Creamos 5 procesos
    for p in processes:
        p.start()
    for p in processes:
        p.join() #Esperamos a que cada proceso termine
    print(f'Valor final del contador: {counter.value}') #Imprimimos el valor final del contador

############################################################################################################################
"""
El valor final del contador es 50, porque cada proceso incrementa el contador compartido 10 veces.
"""

class SharedCounter:
    def __init__(self, lock, value):
        self.lock = lock
        self.value = value

    def increment(self):
        with self.lock:
            temp = self.value.value
            time.sleep(0.1)  # Simula una operación compleja
            self.value.value = temp + 1

def complex_lock_example(counter, i):
    for _ in range(10):
        counter.increment()
    print(f'Proceso {i} valor del contador: {counter.value.value}')

if __name__ == '__main__':
    lock = Lock()
    counter_value = Value('i', 0)  # 'i' es para entero
    counter = SharedCounter(lock, counter_value)
    processes = [Process(target=complex_lock_example, args=(counter, i)) for i in range(5)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    print(f'Valor final del contador: {counter.value.value}')
