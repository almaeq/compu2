import asyncio
import aiohttp

async def enviar_imagen(ip, puerto, ruta_imagen):
    """
    Envía una solicitud al servidor HTTP para procesar una imagen y descarga la imagen procesada.

    Args:
        ip (str): Dirección IP del servidor HTTP al que se envía la solicitud.
        puerto (int): Puerto en el que el servidor HTTP está escuchando.
        ruta_imagen (str): Ruta de la imagen que se desea procesar, que se utiliza en la solicitud al servidor.

    Returns:
        None. La función descarga la imagen procesada y la guarda en el archivo 'imagen_procesada.jpg'.
    """
    url = f"http://{ip}:{puerto}/{ruta_imagen}"
    
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                # Descargar la imagen procesada directamente
                imagen_procesada = await response.read()
                with open('imagen_procesada.jpg', 'wb') as f:
                    f.write(imagen_procesada)
                print("Imagen procesada guardada como 'imagen_procesada.jpg'.")
                print(url)
            else:
                print(f"Error al procesar la imagen. Código de estado: {response.status}")

if __name__ == "__main__":
    ip_servidor = input("Ingrese la IP del servidor: ")
    puerto_servidor = int(input("Ingrese el puerto del servidor: "))
    ruta_imagen = input("Ingrese la ruta de la imagen a procesar: ")

    asyncio.run(enviar_imagen(ip_servidor, puerto_servidor, ruta_imagen))
