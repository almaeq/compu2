from PIL import Image
import math

def wait_for_results_and_combine(width, height, width_part, height_part, num_parts, shared_array, parent_conns):
    """
    Espera los resultados de los procesos y combina las partes filtradas en una imagen final.

    Args:
        width (int): Ancho de la imagen.
        height (int): Alto de la imagen.
        width_part (int): Ancho de cada parte de la imagen.
        height_part (int): Alto de cada parte de la imagen.
        num_parts (int): Número de partes en las que dividir la imagen.
        shared_array (multiprocessing.Array): Array compartido para almacenar la imagen.
        parent_conns (list): Lista de pipes de comunicación.

    Returns:
        Image: Objeto de la imagen combinada.
    """
    completed = 0
    while completed < num_parts:
        for parent_conn in parent_conns:
            try:
                result = parent_conn.recv()
                if isinstance(result, tuple):
                    index, error = result
                    print(f"Error en la parte {index}: {error}")
                else:
                    completed += 1
            except EOFError:
                continue

    combined_image = combine_images(width, height, width_part, height_part, num_parts, shared_array)
    return combined_image


def combine_images(width, height, width_part, height_part, num_parts, array):
    """
    Combina las partes de la imagen en una imagen final.

    Args:
        width (int): Ancho de la imagen.
        height (int): Alto de la imagen.
        width_part (int): Ancho de cada parte de la imagen.
        height_part (int): Alto de cada parte de la imagen.
        num_parts (int): Número de partes en las que dividir la imagen.
        array (multiprocessing.Array): Array compartido que contiene las partes de la imagen.

    Returns:
        Image: Objeto de la imagen combinada.
    """
    columns = math.ceil(math.sqrt(num_parts))
    combined_image = Image.new('RGB', (width, height))

    for index in range(num_parts):
        row = index // columns
        col = index % columns
        start = index * width_part * height_part * 3
        end = (index + 1) * width_part * height_part * 3
        part = Image.frombytes('RGB', (width_part, height_part), bytes(array[start:end]))
        combined_image.paste(part, (col * width_part, row * height_part))

    return combined_image
