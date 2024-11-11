import argparse
import asyncio
from multiprocessing import Process
from servidor_http import iniciar_servidor_http
from servidor_escalado import iniciar_servidor_escalado

async def main(ip, puerto, factor_escala):
    """
    Función principal que inicia el servidor HTTP y el servidor de escalado en procesos separados.

    Args:
        ip (str): Dirección IP en la que se escucharán las solicitudes.
        puerto (int): Puerto en el que se ejecutará el servidor HTTP.
        factor_escala (float): Factor de escala para redimensionar la imagen.

    Returns:
        None
    """
    proceso_escalado = Process(target=iniciar_servidor_escalado, args=(8091, factor_escala))
    proceso_escalado.start()

    await iniciar_servidor_http(ip, puerto)

if __name__ == "__main__":
    # Configuración de argparse para manejar los argumentos de línea de comandos.
    parser = argparse.ArgumentParser(description='Tp2 - procesa imágenes')
    parser.add_argument('-i', '--ip', help='Dirección de escucha', required=True)
    parser.add_argument('-p', '--puerto', help='Puerto de escucha', type=int, required=True)
    parser.add_argument('-e', '--escala', help='Factor de escala para redimensionar la imagen', type=float, default=1.0)
    args = parser.parse_args()

    # Ejecución de la función principal utilizando asyncio.run().
    asyncio.run(main(args.ip, args.puerto, args.escala))
