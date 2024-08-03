# import os

# r,w = os.pipe()

# r = os.fdopen(r)
# w = os.fdopen(w, 'w')

# msg = input('Ingrese un mensaje: ')

# w.write(msg)
# w.close()

# print('Mensaje leido: ', r.readline())

# r.close()

import os


r,w = os.pipe()

pid = os.fork()

if pid:
    print('P: ',os.getpid())
    os.close(w)
    r = os.fdopen(r)
    print('P: leyendo')
    string = r.readline()
    print('P: text = ', string)
    os.wait()

    input()
    exit()

else:
    print('H: ', os.getpid())
    os.close(r)
    w = os.fdopen(w, 'w')
    print('H: escribiendo ')
    w.write('Texto escrito por el hijo\n')
    w.close()
    print('H: Hijo cerrado')
    input()
    exit()