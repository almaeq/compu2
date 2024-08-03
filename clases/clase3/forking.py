import os
import sys
import time

def main():
    fd = open('./archivo.txt', 'w+')
    pid = os.fork()

    if (pid): # Este es el proceso padre
        print('PADRE (PID: %d)' % os.getpid())
        time.sleep(1)
#      fd.seek(0)
        print(fd.read())
    #dado que el read() se realiza inmediatamente después de un sleep() y sin un
    #seek(0) previo que reposicione el cursor al inicio del archivo, no podrá leer lo
    #que el hijo escribió a menos que se descomente el fd.seek(0).

#    fd.write('Esto es una línea del PADRE')
#    fd.flush() #Cuando se escribe en un archivo se escribe sobre un buffer. Para que
#    el contenido del buffer sea escrito en el archivo se debe usar flush o cerrar el 
#    archivo o terminar el proceso correctamente

    else: # Proceso hijo
        print('HIJO (PID: %d)' % os.getpid())
        fd.write('Esto es una línea del HIJO')
        fd.flush()#para asegurar que el cambio se guarde en el archivo antes de que el proceso termine
        sys.exit(0)

#  time.sleep(60) # Los files descriptors se comparten. Por ese motivo ambos pueden
#  ver lo que esta pasando en el archivo. sudo ls -l /proc/pid/fd

if __name__ == "__main__":
    main()