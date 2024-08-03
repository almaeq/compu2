import mmap
import os
import signal
import time

def lee(s, f):
    leido = area.read(16) # 4)
    area.seek(0)
    area.write(leido.decode().upper().encode()) # 5)
    os.kill(pid, signal.SIGUSR1) # 6)
    # Lee 16 bytes del área de memoria compartida, convierte el contenido a mayúsculas y escribe el resultado de nuevo en la memoria. 
    #Luego, envía la señal SIGUSR1 al proceso hijo.

def lee_upper(s, f):
    print(area.read(16)) # 8)


signal.signal(signal.SIGUSR1, lee) # 3)

area = mmap.mmap(-1, 16)

pid = os.fork()

if pid == 0:    
    signal.signal(signal.SIGUSR1, lee_upper)  # 7)
    area.write(b'soy el hijo') # 1)
    os.kill(os.getppid(), signal.SIGUSR1) #Envía la señal SIGUSR1 al proceso padre  
    area.seek(0)
    # time.sleep(2)
    signal.pause()# Espera hasta recibir la señal del padre SIGUS
    exit()

time.sleep(1)
os.wait()