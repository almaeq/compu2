## TP2 - Procesa imágenes

### Requisitos

- Python 3.10
- aiohttp
- Pillow

### Instalación

1. Crear un entorno virtual:

```bash
python3 -m venv env
source env/bin/activate
```

2. Instalar las dependencias:

```bash
pip install -r requirements.txt
```

## Estructura del proyecto

- main.py: Script principal que inicia el servidor
- servidor_http.py: Script que maneja las solicitudes HTTP
- servidor_escalado.py: Script que maneja las solicitudes de escalado
- cliente.py: Script que envía una imagen a la aplicación

### Para ver el diplay de ayuda
```bash
python3 main.py -h
```

### Ejecución
1. Abrir una terminal y ejecutar:

Usando IPv4:
```bash
python3 main.py -i 127.0.0.1 -p 8090 -e 1.5
```
Usando IPv6:
```bash
python3 main.py -i ::1 -p 8090 -e 1.5
```
- `-i`: Dirección de escucha
- `-p`: Puerto de escucha
- `-e`: Factor de escalado

2. Abrir otra terminal y ejecutar el cliente para enviar una imagen a la aplicación:

```bash
python3 cliente.py 
```
El cliente preguntará por la dirección IP y el puerto del servidor HTTP, así como la ruta de la imagen que se desea procesar.

Para IPv4:
```bash
Ingrese la IP del servidor: 127.0.0.1
Ingrese el puerto del servidor: 8090
Ingrese la ruta de la imagen a procesar: imagen.jpg
```

Para IPv6:
```bash
Ingrese la IP del servidor: ::1
Ingrese el puerto del servidor: 8090
Ingrese la ruta de la imagen a procesar: imagen.jpg
```

3. Luego, de haber ejecutado el comando anterior, en la primer terminal abierta va a aparecer el id de la tarea para si se quiere consultar el estado de la tarea.

## Importante
Tener en cuenta si es IPv4 o IPv6 a la hora de completar el cliente

### Para ver el estado de una tarea
En el navegador escribir la siguiente URL y reemplazar el id de tarea con el que se obtuvo:
```bash
hhttp://127.0.0.1:8090/estado/<id_tarea>
```

#### Ejemplo de uso para ver el estado de una tarea
```bash
http://127.0.0.1:8090/estado/34d6916e-49b8-40f5-9940-a2c1a2e0082c
```

```json
{
    "id_tarea": "34d6916e-49b8-40f5-9940-a2c1a2e0082c",
    "estado": "Completada"
}
```
