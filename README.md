# EstegoImagen
Esteganografía aplicando el cifrado César a un mensaje y después ocultandólo en una imágen

# Introducción

Este repositorio consiste de dos programas: Mendacium.py y Veritatis.py cuyos nombres están en latín y significan Mentira y Verdad respectivamente.

# Cifrado César
Este cifrado consiste en aplicar un desplazamiento al alfabeto del mensaje, es decir, en el caso de un mensaje en español el afabeto a desplazar cuenta con 27 carácteres ya que añadimos la letra ñ, si fuera el caso del idioma inglés solo tomariamos en cuenta 26 carácteres. El desplazamiento será considerado la llave para nuestro mensaje para guardarlo como para leerlo de una imagen.

# Mendacium.py
Para poder ocultar el mensaje habremos de escribir lo siguiente en la línea de comandos:

>>> python Mendacium.py -e foto.png -s fotoSalida.png -m mensaje.txt -k 8

Dónde los parametros -e, -s, -m y -k indican: el nombre de la foto de entrada, el nombre de la foto de salida, el archivo que contiene el mensaje y la llave que será equivalente al desplazamiento del cifrado César.

# Veritatis.py
Para poder leer el mensaje habremos de escribir lo siguiente en la línea de comandos:

https://cdn.rawgit.com/whoisML/EstegoImagen/master/imagenes/1.png

Dónde los parametros -e, -s, -m y -k indican: el nombre de la foto de entrada, el nombre de la foto de salida, el archivo que contiene el mensaje y la llave que será equivalente al desplazamiento del cifrado César.
