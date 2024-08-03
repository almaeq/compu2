from PIL import Image
import math

def open_image(ruta):
    try:
        image = Image.open(ruta).convert('RGB')
        image.show()
        return image
    except Exception as e:
        print(f"Error al abrir la imagen: {e}")
        return None

def split_image(image, num_parts):
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
