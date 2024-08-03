from multiprocessing import Process, Value
import ctypes
import time

class SharedValueResource:
    def __init__(self, value):
        self.value = value

    def increment_value(self):
        with self.value.get_lock():  # Asegurar acceso exclusivo
            temp = self.value.value  # Obtener valor actual
            time.sleep(0.1)
            self.value.value = temp + 1
            print(f'Valor incrementado a: {self.value.value}')

def complex_value_example(resource):
    for _ in range(10):
        resource.increment_value()

if __name__ == '__main__':
    shared_value = Value(ctypes.c_int, 0)
    resource = SharedValueResource(shared_value)
    processes = [Process(target=complex_value_example, args=(resource,)) for _ in range(5)]

    for p in processes:
        p.start()
    for p in processes:
        p.join()

    print(f'Valor final: {shared_value.value}')
