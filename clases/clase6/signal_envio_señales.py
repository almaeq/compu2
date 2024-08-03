import os
import signal

def enviar_senal(pid, senal):
    try:
        os.kill(pid, senal)
        print(f"Señal {signal.Signals(senal).name} enviada al proceso con PID {pid}")
    except ProcessLookupError:
        print("Error: No se encontró el proceso.")
    except PermissionError:
        print("Error: Permiso denegado.")

# Ejemplo de uso
pid = 75442  # Reemplazar con el PID real del proceso
senal = signal.SIGTERM  # Señal para terminar el proceso

enviar_senal(pid, senal)
