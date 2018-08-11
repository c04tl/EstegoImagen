# EstegoImagen
Esteganografía aplicando el cifrado César a un mensaje y después ocultandólo en una imágen. Este repositorio consiste de dos programas: Mendacium.py y Veritatis.py cuyos nombres están en latín y significan Mentira y Verdad respectivamente.

# Cifrado César
Este cifrado consiste en aplicar un desplazamiento al alfabeto del mensaje, por ejemplo, si nuestro mensaje es la letra "a" y el desplazamiento utilizado es 1, el criptograma será igual a la letra "b". En el caso de un mensaje en español el afabeto a desplazar cuenta con 27 carácteres ya que añadimos la letra ñ, si fuera el caso del idioma inglés solo tomariamos en cuenta 26 carácteres. El desplazamiento será considerado la llave con la que nuestro mensaje se podrá recuperar.

# Mendacium.py
Para poder ocultar el mensaje habremos de escribir lo siguiente en la línea de comandos:

![Preview](https://cdn.rawgit.com/whoisML/EstegoImagen/master/imagenes/1.png)

Dónde los parametros -e, -s, -m y -k indican: el nombre de la foto de entrada, el nombre de la foto de salida, el archivo que contiene el mensaje y la llave que será equivalente al desplazamiento del cifrado César.

Presionamos la tecla Intro y nos aparecerá el mensaje original, el criptograma(mensaje con desplazamiento), firma MD5 de la foto original y MD5 de la foto con el mensaje:

![Preview](https://cdn.rawgit.com/whoisML/EstegoImagen/master/imagenes/2.png)

Una vez terminado el proceso, se desplegará una vista previa de la imagen que contiene el mensaje:

![Preview](https://cdn.rawgit.com/whoisML/EstegoImagen/master/imagenes/3.png)

# Veritatis.py
Para poder leer el mensaje habremos de escribir lo siguiente en la línea de comandos:

![Preview](https://cdn.rawgit.com/whoisML/EstegoImagen/master/imagenes/4.png)

Dónde los parametros -e y -k indican: el nombre de la foto con el mensaje y la llave para descifrar el mensaje oculto. Este proceso es más simple, pues solo lee el mensaje y lo imprime en la consola:

![Preview](https://cdn.rawgit.com/whoisML/EstegoImagen/master/imagenes/5.png)

Además, si introducimos una llave incorrecta, el mensaje no tiene sentido:

![Preview](https://cdn.rawgit.com/whoisML/EstegoImagen/master/imagenes/6.png)

# Imagenes
Al termino de la ejecución de Mendacium.py podemos observar que la imagen que contiene el mensaje no es muy diferente a la original, pero se puede apreciar que no son la misma imagen debido a sus firmas de comprobación MD5.

Imagen Original(Hoshi.png):
![Preview](https://cdn.rawgit.com/whoisML/EstegoImagen/master/imagenes/Hoshi.png)

Imagen con mensaje(Hoshi2.png)
![Preview](https://cdn.rawgit.com/whoisML/EstegoImagen/master/imagenes/Hoshi2.png)
