## TP1 - Computación

Para poder ejecutar este trabajo, primero debe crear un entorno virtual, con el comando:

$ virtualenv -p python3 venv

y activarlo con el comando:

$ source venv/bin/activate

Luego, se debe instalar las siguientes librerías:

-pillow==10.3.0
-numpy==2.0.0
-scipy==1.14.0

que se pueden instalar con el comando: $ pip3 install -r requirements.txt

Finalmente, se debe ejecutar el archivo main.py con el comando:

$ python3 main.py ruta/a/tu/imagen.jpg --num_parts 4

num_parts es el numero de partes que se desean extraer de la imagen (puede ser 4 o 2)

El programa se ejecutará en la consola y se mostrará la salida en la consola, en formato de imagen (original y con los filtros).

By Alma Quinteros