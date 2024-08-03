from multiprocessing import Pool #para crear un grupo de procesos
import os
import time
""" 
Se utiliza para administrar un grupo de procesos q pueden ejecutar tareas en paralelo 
Facilita la paralelización de la ejecución de una fc en múltiples entradas, distribuyendo 
el trabajo entre varios procesos.
"""
def f(x):
    time.sleep(5)
    return x*x, os.getpid()
#    return x*x

print(os.getpid())
with Pool(processes=4) as pool:
    x = range(10)
    print(list(x))
    input()
    print(pool.map(f, range(10))) #para aplicar la fc f a cada valor en el rango de 0 a 9. pool.map divide el trabajo entre los procesos en el pool y recolecta los resultados en una lista.