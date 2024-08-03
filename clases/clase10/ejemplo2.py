import threading

# Recurso compartido
counter = 0
lock = threading.Lock() #evita la condicion de carrera

def increment_counter():
    global counter
    for _ in range(1000):
        lock.acquire()
        counter += 1
        lock.release()

# Creación de los hilos
threads = [] #para almacenar los objtos de los hilos
for _ in range(10):
    thread = threading.Thread(target=increment_counter)
    threads.append(thread)
    thread.start()

# Espera a que todos los hilos terminen
for thread in threads: #espera a que cada hilo termine
    thread.join()

print(f"Valor final del contador: {counter}")