import os
import socketserver,socket
from PIL import Image

class Escalador(socketserver.BaseRequestHandler):
    """
    Clase que maneja las solicitudes de escalado de imágenes.

    Métodos:
        handle(): Procesa una imagen recibida, la escala y la convierte a escala de grises.
    """
    def handle(self):
        """
        Método que procesa la imagen recibida desde un cliente, la escala y la convierte a escala de grises.

        Args:
            None (usa el `self.request` del cliente).

        Returns:
            None (envía la ruta de la imagen procesada o un mensaje de error al cliente).
        """
        try:
            ruta_imagen = self.request.recv(1024).decode().strip()
            if not os.path.exists(ruta_imagen):
                self.request.sendall(b"Error")
                return

            with Image.open(ruta_imagen) as img:
                ancho, alto = img.size
                nuevo_ancho = int(ancho * self.server.factor_escala)
                nuevo_alto = int(alto * self.server.factor_escala)
                img_escalada = img.resize((nuevo_ancho, nuevo_alto))
                img_escalada_gris = img_escalada.convert("L")
                ruta_procesada = f"escalada_gris_{os.path.basename(ruta_imagen)}"
                img_escalada_gris.save(ruta_procesada, format="JPEG")
                self.request.sendall(ruta_procesada.encode())
        except Exception as e:
            print(f"Error en el escalado: {e}")
            self.request.sendall(b"Error")

class TCPServerV6(socketserver.TCPServer):
    """
    Clase que extiende `socketserver.TCPServer` para soportar IPv6.
    """
    address_family = socket.AF_INET6

def iniciar_servidor_escalado(puerto, factor_escala):
    """
    Función que inicia el servidor de escalado de imágenes.

    Args:
        puerto (int): Puerto en el que se ejecutará el servidor de escalado.
        factor_escala (float): Factor de escala para redimensionar la imagen.

    Returns:
        None
    """
    TCPServerV6.factor_escala = factor_escala
    try:
        with TCPServerV6(("::", puerto), Escalador) as server:
            print(f"Servidor de escalado corriendo en puerto {puerto}")
            server.serve_forever()
    except Exception as e:
        print(f"Error al iniciar el servidor de escalado: {e}")
