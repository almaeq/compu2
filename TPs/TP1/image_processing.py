from PIL import Image, ImageFilter
import multiprocessing
import signal
import sys
from image_utils import *

def apply_filter(image, filter_type):
    """
    Aplica un filtro específico a una imagen.

    Args:
        imagen (Image): Objeto de la imagen a la cual se aplicará el filtro.
        filter_type (str): Tipo de filtro a aplicar. Puede ser 'contour', 'edge_enhance_more' o 'emboss'.

    Returns:
        Image: Objeto de la imagen con el filtro aplicado.
    """
    filters = {
        'contour': ImageFilter.CONTOUR,
        'edge_enhance_more': ImageFilter.EDGE_ENHANCE_MORE,
        'emboss': ImageFilter.EMBOSS
    }
    return image.filter(filters[filter_type])


def worker(index, start, end, width_part, height_part, array, pipe, filter_type):
    """
    Función de proceso trabajador que aplica un filtro a una parte de la imagen y guarda el resultado en el array compartido.

    Args:
        index (int): Índice de la parte de la imagen.
        start (int): Índice de inicio en el array compartido.
        end (int): Índice de fin en el array compartido.
        width_part (int): Ancho de la parte de la imagen.
        height_part (int): Alto de la parte de la imagen.
        array (multiprocessing.Array): Array compartido para almacenar la imagen.
        pipe (multiprocessing.Pipe): Pipe para la comunicación entre procesos.
        filter_type (str): Tipo de filtro a aplicar.
    """
    try:
        part = Image.frombytes('RGB', (width_part, height_part), bytes(array[start:end])) # Convertir el array compartido a Image
        filtered_part = apply_filter(part, filter_type)
        array[start:end] = filtered_part.tobytes() # Actualizar el array compartido con el resultado del filtro
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


def manage_processes(parts, part_size, shared_array, num_parts):
    """
    Crea y gestiona los procesos para aplicar filtros a las partes de la imagen.

    Args:
        parts (list): Lista de partes de la imagen.
        part_size (int): Tamaño de cada parte.
        shared_array (multiprocessing.Array): Array compartido para almacenar la imagen.
        num_parts (int): Número de partes en las que dividir la imagen.

    Returns:
        tuple: Tupla que contiene la lista de procesos y la lista de pipes de comunicación.
    """
    processes = []
    parent_conns = []
    width_part, height_part = parts[0].size
    filters = ['contour', 'edge_enhance_more', 'emboss']
    for index in range(num_parts):
        start = index * part_size
        end = (index + 1) * part_size
        parent_conn, child_conn = multiprocessing.Pipe() # Crear un pipe para la comunicación entre procesos
        parent_conns.append(parent_conn)
        filter_type = filters[index % len(filters)]
        p = multiprocessing.Process(target=worker, args=(index, start, end, width_part, height_part, shared_array, child_conn, filter_type)) 
        processes.append(p) 
        p.start()
    return processes, parent_conns

