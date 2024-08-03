from PIL import Image
import math

def open_image(ruta):
    """
    Abre una imagen desde la ruta especificada y la convierte a formato RGB.

    Args:
        ruta (str): Ruta del archivo de imagen.

    Returns:
        Image: Objeto de la imagen en formato RGB.
    """
    try:
        image = Image.open(ruta).convert('RGB')
        image.show()
        return image
    except Exception as e:
        print(f"Error al abrir la imagen: {e}")
        return None

def split_image(image, num_parts):
    """
    Divide la imagen en un número especificado de partes iguales.

    Args:
        imagen (Image): Objeto de la imagen a dividir.
        num_parts (int): Número de partes en las que dividir la imagen.

    Returns:
        list: Lista de partes de la imagen como objetos Image.
    """
    width, height = image.size
    # Calcular las filas y columnas
    columns = math.ceil(math.sqrt(num_parts))
    rows = math.ceil(num_parts / columns)
    width_part = width // columns
    height_part = height // rows
    parts = []
    for i in range(rows):
        for j in range(columns):
            if len(parts) < num_parts:  # Solo crear partes hasta alcanzar num_parts
                box = (j * width_part, i * height_part, (j + 1) * width_part, (i + 1) * height_part)
                part = image.crop(box)
                parts.append(part)
    return parts
