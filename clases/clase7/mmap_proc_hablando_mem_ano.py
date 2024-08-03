import os, mmap, time

mem = mmap.mmap(-1,16)

pid = os.fork()

if pid == 0:
    time.sleep(1)
    mem.seek(0)
    print('hijo lee: ', mem.read(16).decode().strip('/x00'))
    mem.seek(0)
    mem.write(b'Hola padre')
    exit()

else:
    mem.write(b'hola hijo')
    time.sleep(2)
    mem.seek(0)
    print('padre lee: ', mem.read(16).decode().strip('/x00'))
    os.wait()