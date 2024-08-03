import multiprocessing
import time

def worker(num):
    """Función que será ejecutada por cada proceso."""
    print(f'Worker: {num} iniciando.')
    time.sleep(3)
    print(f'Worker: {num} terminando.')

if __name__ == '__main__':
    # Lista para mantener los procesos
    processes = []

    # Crear procesos
    for i in range(9):  # Crear 5 procesos
        p = multiprocessing.Process(target=worker, args=(i,))
        """ 
        target: objeto que se ejecutará en el proceso
        args: argumentos que se pasarán al objeto target
        """ 
        processes.append(p)
        p.start()

    # Esperar a que todos los procesos terminen
    for p in processes:
        p.join()

    print("Procesamiento completado.")