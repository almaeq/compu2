import signal, os, time

def handler(s, f): #manejador de señales personalizado
    print("Terminando... ")

    signal.signal(signal.SIGINT, signal.SIG_DFL)
    #Estás restaurando el comportamiento predeterminado para la señal SIGINT, lo q significa q el programa responderá a la señal 
    #SIGINT de la misma manera q lo haría normalmente cuando se presiona Ctrl+C.

print(signal.getsignal(signal.SIGINT))

signal.signal(signal.SIGINT, handler)#establece el manejador de señales personalizado

print(signal.getsignal(signal.SIGINT))
# Muestra el manejador de señales personalizado que se acaba de establecer para SIGINT
time.sleep(100)