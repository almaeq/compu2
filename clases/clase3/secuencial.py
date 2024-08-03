import time
import os

print('INICIO')
print('PID: %d  --  PPID: %d' % (os.getpid(), os.getppid()))

for i in range(5, 0, -1):
    print(i)
    time.sleep(1)


print('\nFIN')
print('PID: %d  --  PPID: %d' % (os.getpid(), os.getppid()))

"""
Se puede ver como os.system es una función bloqueante. 
Por lo tanto debe esperar a que termine el primer proceso 
para comenzar el siguiente
"""

# for i in range(2):
#     os.system("python3 secuencial.py")