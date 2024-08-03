import argparse
import signal
from image_processing import *
from image_combination import wait_for_results_and_combine

def main():
    """
    Función principal que maneja la ejecución del procesamiento de imágenes.
    """
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

    if image:
        width, height, parts, shared_array, part_size = prepare_image_and_array(image, args.num_parts)
        processes, parent_conns = manage_processes(parts, part_size, shared_array, args.num_parts)
        
        combined_image = wait_for_results_and_combine(width, height, parts[0].size[0], parts[0].size[1], args.num_parts, shared_array, parent_conns)
        
        combined_image.save('result.png')
        combined_image.show()

if __name__ == "__main__":
    main()