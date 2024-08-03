import os

def main():
    print("Ejecutando 'ls' para listar directorios...")

    # Reemplaza el proceso actual con 'ls'
    # Nota: Este código no se ejecutará más allá de este punto en el proceso actual
    os.execlp('ls', 'ls', '-l')#Reemplaza el proceso actual por uno nuevo
    #El primer argumento ('ls') es el nombre del ejecutable a buscar en la variable
    #PATH, y el segundo argumento ('ls') es el nombre del comando que se pasa al 
    #nuevo proceso. El tercer argumento ('-l') es un argumento adicional que se pasa
    #al comando ls

    # Esta línea no se ejecutará
    print("Esta línea no se mostrará.")

if __name__ == "__main__":
    main()