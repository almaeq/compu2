import threading
import time

def worker(number, delay):
    for _ in range(5):
        print(f"Trabajador {number} está trabajando")
        time.sleep(delay) #delay:tiempo de espera entre cada iteración

# Creación de hilos con argumentos
threads = []
for i in range(3):
    thread = threading.Thread(target=worker, args=(i, i + 1), daemon=True)
    #daemon=True significa que el hilo se ejcutara en segundo plano no impiden q el prograna principal termine
    threads.append(thread)
    thread.start() #comienza la ejecucion de worker en paralelo

# Espera a que todos los hilos no daemon terminen
for thread in threads:
    if not thread.daemon:
        thread.join()

print("Programa principal completado. Los hilos daemon pueden seguir ejecutándose.")
