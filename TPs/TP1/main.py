import argparse
import signal
from image_processing import *

def main():
    signal.signal(signal.SIGINT, signal_handler)
    # Crear el objeto parser
    parser = argparse.ArgumentParser(description="Abrir y mostrar una imagen, dividirla en partes iguales, y aplicar un filtro a cada parte en paralelo.")

    # Añadir un argumento para la ruta de la imagen
    parser.add_argument('ruta', type=str, help='Ruta del archivo de imagen.')

    # Añadir un argumento opcional para el número total de partes
    parser.add_argument('--num_parts', type=int, default=1, help='Número total de partes en las que dividir la imagen.')

    # Parsear los argumentos
    args = parser.parse_args()

    image = open_image(args.ruta)


if __name__ == "__main__":
    main()