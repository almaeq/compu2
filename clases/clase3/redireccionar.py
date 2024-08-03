# import sys, os


# print('PID: %d' %os.getpid())


# fh = open('test.txt', 'w')


# input('Antes de redireccionar')
# sys.stderr = fh
# print('Esta línea va a test.txt', file=sys.stderr)

# sys.Popen('ccc')

# input('Despues de redireccionar')


# sys.stderr = sys.__stderr__

# fh.close()

import sys, os

# Imprimir el PID del proceso actual
print('PID: %d' % os.getpid())

# Abrir (o crear) un archivo en modo de escritura
fh = open('test.txt', 'w')

# Pausa antes de la redirección, esperando entrada del usuario
input('Antes de redireccionar')

# Redirigir stderr al archivo abierto
sys.stderr = fh

# Escribir un mensaje en stderr, que ahora apunta a 'test.txt'
print('Esta línea va a test.txt', file=sys.stderr)

# Provocar intencionadamente un error para demostrar la redirección de stderr
try:
    sys.Popen('ccc')
except AttributeError as e:
    print(f"Error capturado: {e}", file=sys.stderr)

# Pausa después de la redirección, esperando entrada del usuario
input('Después de redireccionar')

# Restaurar stderr a su flujo estándar original
sys.stderr = sys.__stderr__

# Cerrar el archivo
fh.close()