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


