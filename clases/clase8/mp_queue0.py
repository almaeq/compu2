from multiprocessing import Process, Queue
import os, time

""" 
Queue permite la comunicación segura entre procesos. Los elementos 
colocados en la cola por un proceso pueden ser recuperados por otro proceso.
"""

def f(q):
    q.put([42, None, 'hello', os.getppid(), os.getpid()])
    q.put("hijo escribiendo otro mensaje...")
    time.sleep(1)
    print("Hijo muriendo....")

if __name__ == '__main__':
    q = Queue() # crea una cola
    q.put("hola mundo") 
    q.put("hola mundo2")

    p = Process(target=f, args=(q,))
    p.start()
    p.join() # espera a que el proceso hijo termine
    print("El contenido de la cola es:")
    for i in range(4): # imprime el contenido de la cola esperando recibir 4 mensajes
        print(q.get())   