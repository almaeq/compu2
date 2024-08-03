import os

fifo_path = '/home/alma/0compu2/my_fifo'
with open(fifo_path, 'w') as fifo:
    fifo.write('Hola desde el escritor!')