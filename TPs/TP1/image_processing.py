from PIL import Image, ImageFilter
import multiprocessing
import signal
import sys
from image_utils import *

def apply_filter(image, filter_type):
    filters = {
        'contour': ImageFilter.CONTOUR,
        'edge_enhance_more': ImageFilter.EDGE_ENHANCE_MORE,
        'emboss': ImageFilter.EMBOSS
    }
    return image.filter(filters[filter_type])

def worker(index, start, end, width_part, height_part, array, pipe, filter_type):
    try:
        part = Image.frombytes('RGB', (width_part, height_part), bytes(array[start:end]))
        filtered_part = apply_filter(part, filter_type)
        array[start:end] = filtered_part.tobytes()
        pipe.send(index)
    except Exception as e:
        pipe.send((index, str(e)))
    finally:
        pipe.close()

def signal_handler(sig, frame):
    print('Interrupción recibida. Finalizando...')
    sys.exit(0)
