import os

# def main():
#     print(f"Proceso padre PID: {os.getpid()}")
#     pid = os.fork() #se crea un proceso hijo
#     print(pid)
#     if pid == 0:
#         #cod ejeutado por el proceso hijo
#         print(f"Este es el proceso hijo: {os.getpid()}")
#     elif pid > 0:
#         #cod ejecutado por el proceo padre
#         print(f"Este es el proceso padre, PID todavia: {os.getpid()}")
#         os.wait() # El padre espera a que el hijo termine
#     else:
#         #fork fallo
#         print("fork fallo")

# if __name__== "__main__":
#     main()

import sys
import time

var = 100
print("PADRE: Soy el proceso padre y mi pid es: %d" % os.getpid())

pid = os.fork()

for i in range(10):
    if (pid): # Este es el proceso padre
        var += 1
        print("PADRE var: %d  --- %d" % (var, id(var)))
        time.sleep(1)

    else: # Proceso hijo
        var -= 1
        print("HIJO var: %d  --- %d" % (var, id(var)))
        time.sleep(1)