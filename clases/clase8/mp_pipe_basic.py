from multiprocessing import Process, Pipe
import time

def f(conn):
    while True:
        msg = conn.recv() # recibe un mensaje
        if msg == 'end':
            break
        
        print("H: " + msg.upper())# imprime el mensaje en mayusculas
    
    conn.close()

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=f, args=(child_conn,))
    p.start()
    
    while True:
        msg = input() # lee un mensaje
        parent_conn.send(msg) # envía el mensaje al proceso hijo
        if msg == 'end':
            break
    
    p.join()