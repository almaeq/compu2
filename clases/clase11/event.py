import threading, random

# Creamos el objeto de evento
event = threading.Event()

# Definimos una función que espera al evento
def wait_for_event():
    print("Esperando al evento...")
    event.wait()
    print("¡El evento ha ocurrido!")

# Definimos una función que desencadena el evento
def trigger_event():
    while True:
        n = random.randint(0, 100)
        print(n)
        if n == 0:
            event.set()
            break

# Creamos los hilos para esperar y desencadenar el evento
wait_thread = threading.Thread(target=wait_for_event)
trigger_thread = threading.Thread(target=trigger_event)

# Iniciamos los hilos
wait_thread.start()
trigger_thread.start()

# Esperamos a que los hilos terminen
wait_thread.join()
trigger_thread.join()

print("Programa finalizado")
