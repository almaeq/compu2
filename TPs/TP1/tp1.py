import argparse
from PIL import Image, ImageFilter
import math
import multiprocessing
import signal
import sys


def open_imagen(ruta):
    try:
        # Abre la imagen
        imagen = Image.open(ruta).convert('RGB')
        # Muestra la imagen
        imagen.show()

        # Retorna la imagen
        return imagen
    except Exception as e:
        print(f"Error al abrir la imagen: {e}")
        return None

def split_image(imagen, num_parts):
    width, height = imagen.size
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
                part = imagen.crop(box)
                parts.append(part)
                # print(f"Parte {i}, {j} guardada como parte_{i}_{j}.png")
                # part.save(f"parte_{i}_{j}.png")  # Guardar la parte
    return parts

def apply_filter(filter, imagen):
    filters = [
        ImageFilter.CONTOUR,
        ImageFilter.EDGE_ENHANCE_MORE,
        ImageFilter.EMBOSS
    ]
    return imagen.filter(filter)



if __name__ == "__main__":

    
    # Crear el objeto parser
    parser = argparse.ArgumentParser(description="Abrir y mostrar una imagen, dividirla en partes iguales, y aplicar un filtro aleatorio a cada parte.")

    # Añadir un argumento para la ruta de la imagen
    parser.add_argument('ruta', type=str, help='Ruta del archivo de imagen.')

    # Añadir un argumento opcional para el número total de partes
    parser.add_argument('--num_parts', type=int, default=1, help='Número total de partes en las que dividir la imagen.')

    # Parsear los argumentos
    args = parser.parse_args()

    

    # Llamar a la función open_imagen con la ruta proporcionada
    imagen = open_imagen(args.ruta)

    if imagen:
        # Dividir la imagen en partes iguales
        parts = split_image(imagen, args.num_parts)
    
