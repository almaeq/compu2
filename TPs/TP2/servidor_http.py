import aiohttp.web as web
import asyncio
import os
import uuid

# Diccionario global para almacenar el estado de las tareas en curso.
tareas = {}

async def manejar_solicitud(request):
    """
    Función que maneja las solicitudes de imágenes de forma asíncrona.

    Args:
        request (aiohttp.web.Request): La solicitud HTTP recibida.

    Returns:
        aiohttp.web.Response: Respuesta con un ID de tarea o un mensaje de error.
    """
    ruta_imagen = request.match_info.get('ruta')
    if not ruta_imagen or not os.path.exists(ruta_imagen):
        return web.Response(status=404, text="Imagen no encontrada")

    # Generar un ID de tarea único
    id_tarea = str(uuid.uuid4())
    tareas[id_tarea] = 'En progreso'
    print(f"Solicitud recibida para procesar: {ruta_imagen}, ID de tarea: {id_tarea}")

    asyncio.create_task(procesar_imagen(ruta_imagen, id_tarea))

    # Responder al cliente con el ID de la tarea
    return web.json_response({'id_tarea': id_tarea})

async def procesar_imagen(ruta_imagen, id_tarea):
    """
    Función asíncrona para manejar la comunicación con el servidor de escalado y actualizar el estado de la tarea.

    Args:
        ruta_imagen (str): Ruta de la imagen a procesar.
        id_tarea (str): Identificador de la tarea.

    Returns:
        None
    """
    try:
        reader, writer = await asyncio.open_connection('::1', 8091)
        writer.write(ruta_imagen.encode())
        await writer.drain()

        respuesta = await reader.read(1024)
        writer.close()
        await writer.wait_closed()

        if respuesta.decode() == "Error":
            tareas[id_tarea] = 'Error al procesar la imagen'
            return

        ruta_procesada = respuesta.decode().strip()
        if os.path.exists(ruta_procesada):
            tareas[id_tarea] = 'Completada'
        else:
            tareas[id_tarea] = 'Error al procesar la imagen'
    except Exception as e:
        print(f"Error en la comunicación con el servidor de escalado: {e}")
        tareas[id_tarea] = 'Error en la comunicación'

async def consultar_estado_tarea(request):
    """
    Función que permite consultar el estado de una tarea por su ID.

    Args:
        request (aiohttp.web.Request): La solicitud HTTP recibida.

    Returns:
        aiohttp.web.Response: Respuesta con el estado de la tarea o un mensaje de error si no se encuentra.
    """
    id_tarea = request.match_info.get('id_tarea')
    estado = tareas.get(id_tarea, 'No encontrado')
    return web.json_response({'id_tarea': id_tarea, 'estado': estado})

async def iniciar_servidor_http(ip, puerto):
    """
    Función que configura y arranca el servidor HTTP.

    Args:
        ip (str): Dirección IP en la que se escucharán las solicitudes.
        puerto (int): Puerto en el que se ejecutará el servidor HTTP.

    Returns:
        None
    """
    app = web.Application()
    app.router.add_get('/{ruta}', manejar_solicitud)
    app.router.add_get('/estado/{id_tarea}', consultar_estado_tarea)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, ip, puerto)
    await site.start()

    print(f"Servidor HTTP corriendo en {ip}:{puerto}")
    await asyncio.Event().wait()
