from multiprocessing import Process, Array
import time

class SharedArrayResource:
    def __init__(self, array):
        self.array = array

    def modify_array(self, index, value):
        with self.array.get_lock():  # Asegurar acceso exclusivo
            self.array[index] = value #Modifica el valor en el índice index del array compartido
            print(f'Array modificado en índice {index}: {self.array[:]}')

def complex_array_example(resource, i):
    for idx in range(len(resource.array)):
        time.sleep(0.1 * i)  # Diferente tiempo de espera para cada proceso
        resource.modify_array(idx, i * idx)  # Modifica el valor en el índice index del array compartido

if __name__ == '__main__':
    shared_array = Array('i', [0] * 5)  # Array de enteros inicializado a ceros
    resource = SharedArrayResource(shared_array)
    processes = [Process(target=complex_array_example, args=(resource, i)) for i in range(5)]

    for p in processes:
        p.start()
    for p in processes:
        p.join()

    print(f'Array final: {shared_array[:]}')
    #El resultado final del array dependerá de los tiempos de espera y del orden en que los procesos terminan

