import os, mmap

mem = mmap.mmap(-1, 16)

pid = os.fork()

if not pid:
    #proceso hijo
    mem.write(b'Linea')
    print('Offset del hijo', mem.tell()) #Imprime el desplazamiento actual (offset) en la memoria compartida después de la escritura. 
    # mem.tell() devuelve la posición actual del puntero de escritura/lectura.
    exit()

os.wait()
print('Offset del padre', mem.tell())
#Dado q los procesos padre e hijo comparten la misma mem, pero no el mismo puntero de desplazamiento, el desplazamiento impreso por el padre será dif del impreso por el hijo.