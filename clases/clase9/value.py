from multiprocessing import Process, Value
import ctypes #Módulo q proporciona tipos de datos compatibles con C, útiles para la comunicación entre procesos en multiprocessing.
""" 
Value permite compartir una sola variable entre procesos. Es útil para tipos de datos 
simples y básicos como enteros y flotantes. 
"""
def simple_value_example(val):
    val.value += 1 # Incrementar el valor de la variable compartida
    print(f'Valor en proceso: {val.value}')

if __name__ == '__main__':
    shared_value = Value(ctypes.c_int, 0) #crea una variable entera compartida entre procesos, inicializada a 0. ctypes.c_int especifica que la variable es un entero de C.
    processes = [Process(target=simple_value_example, args=(shared_value,)) for _ in range(5)]

    for p in processes:
        p.start()
    for p in processes:
        p.join()

    print(f'Valor final: {shared_value.value}')