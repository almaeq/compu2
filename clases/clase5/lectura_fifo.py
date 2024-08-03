import os

fifo_path = 'my_fifo'
with open(fifo_path, 'r') as fifo:
    message = fifo.read()
    print(f'Mensaje recibido: {message}')