import mmap
import os

# Abre un archivo para lectura y escritura
file_path = 'example.dat'
with open(file_path, 'r+b') as f:
    # Mapea todo el archivo en memoria
    mm = mmap.mmap(f.fileno(), 0)
    
    # Lee algunos bytes del archivo mapeado
    print('Contenido original:', mm[:10].decode('utf-8'))
    
    # Modifica algunos bytes en la memoria
    mm[0:5] = b'Hello'
    
    # Sincroniza los cambios con el archivo original
    mm.flush()
    
    # Lee los cambios del archivo mapeado
    print('Contenido modificado:', mm[:10].decode('utf-8'))
    
    # Cierra el mapeo de memoria
    mm.close()