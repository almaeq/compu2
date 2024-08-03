import os
import signal

def handler(s, f):
    print('Llegó la señal ', s)
    print(f)


#signal.signal(signal.SIGINT, signal.SIG_IGN)#ignora la señal
signal.signal(signal.SIGINT, handler)#con el ctrl c en lugar de termminar el proceso se invoca el handler

input()

