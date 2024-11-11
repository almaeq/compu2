## TP2 - Procesa imágenes

### Requisitos

- Python 3.10
- aiohttp
- Pillow

### Instalación

```bash
pip install -r requirements.txt
```

### Ejecución
1. Abrir una terminal y ejecutar:

```bash
python3 main.py -i 127.0.0.1 -p 8090 -e 1.5
```
2. Abrir otra terminal y ejecutar:

```bash
curl http://127.0.0.1:8090/imagen.jpg --output salida.jpg
```

- `-i`: Dirección de escucha
- `-p`: Puerto de escucha
- `-e`: Factor de escalado

### Ejemplo de uso para ver la imagen procesada

```bash
curl http://127.0.0.1:8090/imagen.jpg --output salida.jpg
```

### Ejemplo para ver el id de la tarea

```bash
curl http://127.0.0.1:8090/imagen.jpg 
```

### Ejemplo de uso para ver el estado de una tarea

```bash
curl http://127.0.0.1:8090/estado/34d6916e-49b8-40f5-9940-a2c1a2e0082c
```

```json
{
    "id_tarea": "c7a2f9b0-d5a1-4f0e-b2a7-c4c2c3d4e5f6",
    "estado": "Completada"
}
```