from multiprocessing import Process, Array
""" 
Array permite compartir una lista de valores entre procesos. Es útil para tipos de datos simples y básicos.
"""
def simple_array_example(arr, i):
    arr[i] = arr[i] ** 2
    print(f'Array en proceso {i}: {arr[:]}')

if __name__ == '__main__':
    shared_array = Array('i', range(5))  # Array de enteros
    processes = [Process(target=simple_array_example, args=(shared_array, i)) for i in range(5)]
    #crea un array de enteros compartido entre procesos, inicializado con los valores [0, 1, 2, 3, 4]
    for p in processes:
        p.start()
    for p in processes:
        p.join()

    print(f'Array final: {shared_array[:]}')