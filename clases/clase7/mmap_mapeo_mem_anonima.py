import mmap
import os

# Se define la longitud de la región de memoria a asignar
# mem_size = os.sysconf('SC_PAGE_SIZE') * 10
mem_size = 64
# Se crea un objeto mmap que representa la región de memoria mapeada
mem = mmap.mmap(-1, mem_size, mmap.MAP_ANONYMOUS | mmap.MAP_SHARED) #mmap.MAP_ANONYMOUS se utiliza para asignar memoria sin un archivo asociado, y
#mmap.MAP_SHARED se utiliza para indicar que la memoria es compartida entre procesos.
# -1 indica q no hay archivo subyacente

# Se escribe en la región de memoria compartida
mem.write(b'Hola, esta es una prueba de memoria compartida.')

# Se lee de la región de memoria compartida
mem.seek(0)#0: sets the reference point at the beginning of the file 
#1: sets the reference point at the current file position 
#2: sets the reference point at the end of the file 
data = mem.read(mem_size)

print(data)

# Se libera la región de memoria compartida
mem.close()
# Cierra el objeto mmap y libera el área de memoria asociada, asegurando que no haya fugas de memoria.