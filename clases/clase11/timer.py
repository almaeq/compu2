import threading

def print_message():
    print("¡Hola desde el temporizador!")

# Crear un temporizador que ejecute la función print_message después de 5 segundos
timer = threading.Timer(5, print_message)

# Iniciar el temporizador
timer.start()

# Realizar otras tareas mientras el temporizador está en ejecución
print("Realizando otras tareas...")

# Esperar a que el temporizador finalice su ejecución
timer.join()

# El programa continuará aquí después de que el temporizador haya terminado

print("Fin del programa")