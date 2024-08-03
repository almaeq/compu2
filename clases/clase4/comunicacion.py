# import os

# # Crear un pipe
# r, w = os.pipe()

# # Crear un proceso hijo
# pid = os.fork()
# if pid > 0:
#     # Proceso padre
#     os.close(r)  # Cerrar el extremo de lectura en el padre
#     w = os.fdopen(w, 'w')
#     print("Proceso padre escribiendo")
#     w.write("Hola desde el padre")
#     w.close()
# else:
#     # Proceso hijo
#     os.close(w)  # Cerrar el extremo de escritura en el hijo
#     r = os.fdopen(r)
#     print("Proceso hijo leyendo")
#     print(r.read())
#     r.close()

import os

# Crear dos pipes, uno para la comunicación del padre al hijo y otro para la comunicación del hijo al padre
pipe_parent_to_child = os.pipe()
pipe_child_to_parent = os.pipe()

# Crear un proceso hijo
pid = os.fork()

if pid > 0:
    # Proceso padre
    os.close(pipe_parent_to_child[0])  # Cerrar el extremo de lectura del pipe de padre a hijo
    os.close(pipe_child_to_parent[1])  # Cerrar el extremo de escritura del pipe de hijo a padre
    
    # Leer el mensaje del usuario y enviarlo al hijo
    message_to_child = input("Mensaje para el hijo: ")
    os.write(pipe_parent_to_child[1], message_to_child.encode())
    
    # Esperar a la respuesta del hijo
    response_from_child = os.read(pipe_child_to_parent[0], 1024).decode()
    print("Respuesta del hijo:", response_from_child)
else:
    # Proceso hijo
    os.close(pipe_parent_to_child[1])  # Cerrar el extremo de escritura del pipe de padre a hijo
    os.close(pipe_child_to_parent[0])  # Cerrar el extremo de lectura del pipe de hijo a padre
    
    # Leer el mensaje del padre
    message_from_parent = os.read(pipe_parent_to_child[0], 1024).decode()
    print("Mensaje del padre:", message_from_parent)
    
    # Responder al padre
    response_to_parent = "Hola, soy el hijo"
    os.write(pipe_child_to_parent[1], response_to_parent.encode())