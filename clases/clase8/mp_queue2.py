import multiprocessing
import time, os

def funcion(numbers, q):
#    time.sleep(3)
    for n in numbers:
        if n % 2 == 0:
            q.put("PID: %s, valor: %d" %(os.getpid(), n))
            time.sleep(1)
    print("Terminando hijo %d..." % os.getpid())

if __name__ == "__main__":
    q = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=funcion, args=(range(10), q))
    p2 = multiprocessing.Process(target=funcion, args=(range(10,20), q))
    p1.start()
    p2.start()
    while q:
        print("Padre en el while...")
        try: # intenta leer msj de la cola
            print("P: " + q.get(False, 3)) # si no hay msj en la cola, se espera 3 segundos
        except Exception as e:
            print("Cola vacía... saliendo") # si no aparece nada, se sale
            print(e)
            break

    p1.join()
    p2.join()