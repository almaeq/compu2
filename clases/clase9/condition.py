from multiprocessing import Process, Condition, Lock
import time

""" 
Una Condition es una variable de sincronización avanzada q permite a los procesos 
esperar hasta q una condición específica se cumpla. Se utiliza junto con un Lock o RLock.
"""

def simple_condition_example(cond, i):
    with cond: #para adquirir el lock asociado a la condición
        print(f'Proceso {i} esperando la condición')
        cond.wait() #libera el Lock y hace q el proceso espere hasta q otro proceso llame a notify() o notify_all().
        print(f'Proceso {i} condición cumplida')

if __name__ == '__main__':
    condition = Condition(Lock()) #se crea un objeto condition asociado a un lock
    for num in range(5):
        Process(target=simple_condition_example, args=(condition, num)).start()

    time.sleep(2) #espera 2 segundos para que todos los procesos se pongan en espera en cond.wait()
    with condition:
        print('Condición cumplida, notificando a todos')
        condition.notify_all() #notifica a todos los procesos que la condición se cumple

