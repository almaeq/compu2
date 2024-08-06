from PIL import Image, ImageFilter
import multiprocessing
import signal
import sys
from image_utils import *

def apply_filter(image):
    """
    Aplica un filtro de detección de bordes a una imagen.

    Esta función utiliza el filtro FIND_EDGES de la biblioteca PIL (Pillow)
    para aplicar un efecto de detección de bordes a la imagen proporcionada.

    Args:
        image (PIL.Image.Image): La imagen a la que se le aplicará el filtro. Debe ser un objeto de imagen válido de PIL.

    Returns:
        PIL.Image.Image: La imagen con el filtro de detección de bordes aplicado.
    return image.filter(ImageFilter.FIND_EDGES)
    """
    return image.filter(ImageFilter.FIND_EDGES)


def worker(index, start, end, width_part, height_part, array, pipe, apply_findedges):
    """
    Procesa una parte de la imagen aplicando un filtro de detección de bordes opcionalmente y actualiza la parte en un array compartido.

    Args:
        index (int): Índice de la parte de la imagen a procesar.
        start (int): Índice de inicio en el array compartido para esta parte de la imagen.
        end (int): Índice de fin en el array compartido para esta parte de la imagen.
        width_part (int): Ancho de la parte de la imagen.
        height_part (int): Altura de la parte de la imagen.
        array (multiprocessing.Array): Array compartido que contiene la imagen.
        pipe (multiprocessing.Pipe): Pipe para la comunicación entre procesos.
        apply_findedges (bool): Indica si se debe aplicar el filtro de detección de bordes a esta parte de la imagen.

    Returns:
        None
    """
    try:
        part = Image.frombytes('RGB', (width_part, height_part), bytes(array[start:end]))
        if apply_findedges:
            part = apply_filter(part)
        array[start:end] = part.tobytes()
        pipe.send(index)
    except Exception as e:
        pipe.send((index, str(e)))
    finally:
        pipe.close()


def signal_handler(sig, frame):
    """
    Manejador de señales para permitir la interrupción controlada del procesamiento.

    Args:
        sig (int): Número de señal.
        frame (frame object): Frame actual.
    """
    print('Interrupción recibida. Finalizando...')
    sys.exit(0)


def prepare_image_and_array(image, num_parts):
    """
    Prepara la imagen y el array compartido para el procesamiento paralelo.

    Args:
        imagen (Image): Objeto de la imagen a procesar.
        num_parts (int): Número de partes en las que dividir la imagen.

    Returns:
        tuple: Tupla que contiene el ancho y alto de la imagen, las partes de la imagen, el array compartido y el tamaño de cada parte.
    """
    width, height = image.size
    parts = split_image(image, num_parts)
    total_size = width * height * 3 # Tamaño total de la imagen en bytes
    part_size = total_size // num_parts
    shared_array = multiprocessing.Array('B', total_size)
    for index, part in enumerate(parts):
        start = index * part_size
        shared_array[start:start + part_size] = part.tobytes()
    return width, height, parts, shared_array, part_size


def manage_processes(parts, part_size, shared_array, num_parts, findedges_parts_count):
    """
    Crea y gestiona procesos para aplicar el filtro de detección de bordes a partes de una imagen en paralelo.

    Args:
        parts (list of PIL.Image.Image): Lista de partes de la imagen a procesar.
        part_size (int): Tamaño en bytes de cada parte de la imagen.
        shared_array (multiprocessing.Array): Array compartido que contiene la imagen.
        num_parts (int): Número total de partes en las que se divide la imagen.
        findedges_parts_count (int): Número de partes a las que se les aplicará el filtro de detección de bordes.

    Returns:
        tuple: Una tupla que contiene:
            - processes (list of multiprocessing.Process): Lista de procesos creados.
            - parent_conns (list of multiprocessing.Pipe): Lista de conexiones de comunicación entre procesos.
    """
    processes = []
    parent_conns = []
    width_part, height_part = parts[0].size
    for index in range(num_parts):
        start = index * part_size
        end = (index + 1) * part_size
        parent_conn, child_conn = multiprocessing.Pipe() # Crear un pipe para la comunicación entre procesos
        parent_conns.append(parent_conn)
        apply_findedges = index < findedges_parts_count
        p = multiprocessing.Process(target=worker, args=(index, start, end, width_part, height_part, shared_array, child_conn, apply_findedges))
        processes.append(p) 
        p.start()
    return processes, parent_conns

