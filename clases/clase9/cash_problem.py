from multiprocessing import Process, Value
import ctypes
""" 
Hay un problema importante: las operaciones sobre el contador no son atómicas, lo q 
puede llevar a condiciones de carrera. Esto significa q los procesos pueden 
interferir entre sí y el valor final del contador puede no ser el esperado.
"""

# Shared counter
counter = Value(ctypes.c_int, 0)

# Number of increments per process
num_increments = 10000

# Function to increment the counter
def increment_counter(counter):
    for _ in range(num_increments):
        counter.value += 1

def decrement_counter(counter):
    for _ in range(num_increments):
        counter.value -= 1

# Create two processes that increment the counter
process1 = Process(target=increment_counter, args=(counter,))
process2 = Process(target=decrement_counter, args=(counter,))

# Start the processes
process1.start()
process2.start()

# Wait for both processes to finish
process1.join()
process2.join()

# Print the counter
print(counter.value)

###########   SIN CONDITIONES DE CARRERA   ###########
from multiprocessing import Process, Value, Lock
import ctypes

# Shared counter
counter = Value(ctypes.c_int, 0)
lock = Lock()

# Number of increments per process
num_increments = 10000

# Function to increment the counter
def increment_counter(counter, lock):
    for _ in range(num_increments):
        with lock:
            counter.value += 1

def decrement_counter(counter, lock):
    for _ in range(num_increments):
        with lock:
            counter.value -= 1

# Create two processes that increment the counter
process1 = Process(target=increment_counter, args=(counter, lock))
process2 = Process(target=decrement_counter, args=(counter, lock))

# Start the processes
process1.start()
process2.start()

# Wait for both processes to finish
process1.join()
process2.join()

# Print the counter
print(counter.value)
