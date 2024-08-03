import os

r,w = os.pipe()

r = os.fdopen(r)
w = os.fdopen(w, 'w') #abre la tubería para escritura

msg = input('Ingrese un mensaje: ')

w.write(msg) #escribe el mensaje en el extremo de escritura de la tubería.
w.close()

print('Mensaje leido: ', r.readline())

r.close()