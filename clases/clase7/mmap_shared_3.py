import mmap
import os
import time


area = mmap.mmap(-1, 16)

pid = os.fork()

if pid == 0:
    print("pid1:",pid)
    area.write(b'soy el hijo')
    area.seek(0)#0: sets the reference point at the beginning of the file 
    #1: sets the reference point at the current file position 
    #2: sets the reference point at the end of the file 
    time.sleep(2)
    print(area.read(16))
    exit()

time.sleep(1)
leido = area.read(16)
print(leido)
area.seek(0)
area.write(leido.decode().upper().encode())
os.wait()
print('pid2: ',pid)
print(leido)