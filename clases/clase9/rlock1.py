from multiprocessing import Process, RLock
import time

class SharedCounterRLock:
    def __init__(self, rlock):
        self.rlock = rlock
        self.value = 0

    def increment(self):
        with self.rlock:
            self.rlock.acquire()
            try:
                temp = self.value
                time.sleep(0.1)  # Simula una operación compleja
                self.value = temp + 1
            finally:
                self.rlock.release()

def complex_rlock_example(counter, i):
    for _ in range(10):
        counter.increment()
    print(f'Proceso {i} valor del contador: {counter.value}')

if __name__ == '__main__':
    rlock = RLock()
    counter = SharedCounterRLock(rlock)
    processes = [Process(target=complex_rlock_example, args=(counter, i)) for i in range(5)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    print(f'Valor final del contador: {counter.value}')
