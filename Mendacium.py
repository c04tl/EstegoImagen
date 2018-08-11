"""
MIT License

Copyright (c) 2018 whoisML(GitHub)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the Veritatis), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from PIL import Image
import numpy
import sys, getopt
import math
import os
""" programa hecho para python 2.7.13
$ chmod +x test.py 		Esto hace que el archivo sea ejecutable
$./test.py
"""

#Metodo que se llama princial y recibe argumentos de consola con el nombre argv
def principal(argv):
	#captura las opciones(e,s,m,k) y los argumentos(foto.png,foto2.png,mensaje,llave)
	try:
		"""opts y args capturan las entradas por consola
										reconoce las opciones listadas abajo"""
		opts, args = getopt.gnu_getopt(argv,"e:s:m:k:i:c:h",["entrada=","salida=","mensaje=","llave="])
	#si hay un error este se guarda en e, imprime e, llama al metodo ayuda y sale de la ejecucion
	except getopt.GetoptError as e:
		print (e)
		ayuda()
		sys.exit(2)
	#creaamos e iniciamos la variable control
	control = " "
	#para cada opts se hace una comparacion
	for opt, arg in opts:
		if opt == '-h':
			ayuda()
			sys.exit()
		elif opt in ("-e", "--entrada"):
			#si op = -e o --entrada crea una variable a la que le asigna el valor despues de la opcion -e o --entrada
			archivoentrada = arg
		elif opt in  ("-s", "--salida"):
			#si op = -s o --salida crea una variable a la que le asigna el valor despues de la opcion -s o --salida
			archivosalida = arg
		elif opt in  ("-m", "--mensaje"):
			#si op = -m o --mensaje crea una variable a la que le asigna el valor despues de la opcion -m o --mensaje
			ruta = arg
		elif opt in  ("-k", "--llave"):
			#si op = -k o --llave crea una variable a la que le asigna el valor despues de la opcion -k o --llave
			clave = arg
		elif opt in ("-i", "--imprimirM"):
			#si op = -i o --imprimirM crea una variable a la que le asigna el valor despues de la opcion -i o --imprimirM
			#si la opcion -i esta habilidata su valor debe ser un string = True
			control = arg
	"""llama el metodo con los valores capturados en la entrada por consola
	clave es capturada como string por lo cual se convierte en int al enviarlo como parametro"""
	ocultarMensaje(control, ruta, archivoentrada, archivosalida, int(clave))

def ocultarMensaje(imprime, ruta, entrada, salida, llave):
	"""crea una variable a la que le asigna el archivo de mensaje que llega por parametro,
	lo abre con la opcion "r" = read para leer el contenido"""
	archivo = open(ruta,"r")

	#crea una variable y le asigna la lectura del paso anterior
	linea = archivo.read()

	#cierra el archivo
	archivo.close()

	#crea e inicia una variable para el criptograma
	criptograma = ""

	#imprime la lectura del archivo
	print ("Mensaje: {}".format(linea))

	"""x toma el valor de cada letra en el resultado de la lectura del archivo
	para cada x en el Strin linea haz lo siguiente:"""
	for x in linea:
		#variable que vale lo que el metodo obtenerAscci(x) obtenga con la x o letra
		valorAscii = obtenerAscii(x)

		"""aqui aplicamos el cifrado cesar, el valor de la letra x le sumamos la llave que llego por parametro,
		asi obtenemos el desplazamiento del cifrado cesar, al final obtenemos modulo 255 ya que 255 equivale al alfabeto ASCII"""
		valorAscii = (valorAscii+llave)%255

		#variable que vale lo que el metodo obtenerBinario(valorAscii) obtenga con el valor ASCII con desplazamiento
		valorBin = obtenerBinario(valorAscii)

		#Acumula en cada iteracion la conversion a letra del valor ASCII con desplazamiento
		criptograma += chr(valorAscii)

	#al finalizar el for criptograma tiene el valor de todos los valores ASCII con desplazamiento
	print ("Criptograma: {}".format(criptograma))

	#variable que vale lo que el metodo obtenerLista(criptograma, llave) obtenga con el criptograma y la llave
	lista = obtenerLista(criptograma, llave)

	#variable que abre la imagen en donde "entrada" es lo que se recibio por parametro
	imagen = Image.open(entrada)

	#variable tipo vector que guarda el ancho y alto de la imagen
	tamano = imagen.size

	#variable que vale el primer valor de la variable anterior
	ancho = tamano[0]

	#variable que vale el segundo valor de la variable tamano
	alto = tamano[1]

	#variable que permite acceder a los pixeles de la imagen
	pixeles = imagen.load()

	print("Ocultando mensaje. . .")

	#variable que ayudara a dejar de ocultar el mensaje
	contador = 0

	#TANTO X COMO Y COMIENZAN EN 0
	#para cada x en el rango de la variable ancho haz:
	for x in range(ancho):

		#para cada y en el rango de la variable alto haz:
		for y in range(alto):

			#si contador < longitud de la variable lista haz
			if contador < len(lista):

				#variable tipo vector que guarda los valores obtenidos en las coordenadas x, y de la variable pixeles
				pixel = pixeles[x, y]

				#variable que guarda el primer valor de la variable pixel
				rojo = pixel[0]

				#variable que guarda el segundo valor de la variable pixel
				verde = pixel[1]

				#variable que guarda el tercer valor de la variable pixel
				azul = pixel[2]

				#si contador < longitud de la variable lista
				if contador < len(lista):
					"""variable que vale lo que el metodo cambiaC(rojo,lista[contador]) retorne,
					al metodo cambiarC le enviamos el valor del pixel rojo actual y como contador vale 0
					le estamos enviando el primer valor de la variable tipo vector lista"""
					rojoMod = cambiaC(rojo, lista[contador])

					"""aumentamos el contador en 1 para que la proxima vez que enviemos lista[contador]
					se tome en cuenta el siguiente elemento de la lista"""
					contador += 1

				#en caso que contador > longitud de la variable lista
				else:
					#a la variable rojoMod le asignamos el valor real del pixel rojo
					rojoMod = rojo
				
				"""En los 2 siguientes bloques se repite la misma operacion que la enterior solo que
				cambiamos de pixeles al verde y azul"""
				if contador < len(lista):
					verdeMod = cambiaC(verde, lista[contador])
					contador += 1
				else:
					verdeMod = verde

				if contador < len(lista):
					azulMod = cambiaC(azul, lista[contador])
					contador += 1
				else:
					azulMod = azul
					
				#finalmente, en las coordenadas x, y de la variable pixeles le asignamos el valor de las variables rojoMod, verdeMod, azulMod
				pixeles[x, y] = (rojoMod, verdeMod, azulMod)

			#en caso que contador > longitud de la variable lista se rompe el ciclo
			else:
				break

		#si el ciclo for no se rompe con un break
		else:
			#continua con la siguiente iteracion del ciclo
			continue

		#si y > variable alto rompe el ciclo
		break
		print ("Eureka!")

	#si el ciclo for no se rompe con un break
	else:
		#math.floor baja el valor decimal a entero minimo mas cercano, por ejemplo, 4.56 lo reduce a 4, 7.6 lo reduce a 7
		print ("Sobraron {} caracteres". format(math.floor((len(lista) - contador) / 8) ))

	#guarda la imagen donde salida es el valor que se recibio por parametro
	imagen.save(salida)

	print ("MD5 del archivo: {}".format(entrada))
	#utiliza el comando del systema md5sum para obtener la suma criptografica del archivo de entrada
	print (os.popen('md5sum {}'.format(entrada)).read())


	print ("MD5 del archivo: {}".format(salida))
	#utiliza el comando del systema md5sum para obtener la suma criptografica del archivo de salida
	print (os.popen('md5sum {}'.format(salida)).read())

	#muestra la imagen despues de guardarla
	imagen.show()

	#para convertir cualquier imagen a png
	#imRGB = im.convert('RGBA')

	#si la variable recibida por parametro es igual a True haz:
	if imprime == "True":
		for x in range(ancho):
			for y in range(alto):

				#imprime los valores de los pixeles en las coordenadas x,y
				print (pixeles[x,y])

def obtenerLSB(byte):
	#retorna el ultimo elemento de la lista byte
	return byte[-1]

def cambiaLSB(byte, nuevo):
	"""[:-1] obtiene todos los valores excepto el ultimo,
	de esta manera podriamos decir que falta un elemento en la lista byte
	pero es recupero al hacer + str(nuevo) --- str convierte en string
	"""
	return byte[:-1] + str(nuevo)

def binDecimal(binario):
	#int convierte en entero lo que venga por patametro pero indicamos con 2 que se trata de un numero en base 2 o un numero binario
	return int(binario, 2)

def cambiaC(original, nuevo):
	#variable que almacena lo obtenido por el metodo obtenerBinario(original)
	colorBin = obtenerBinario(original)

	#variable que almacena lo obtenido por el metodo cambiaLSB(colorBin, nuevo)
	colorMod = cambiaLSB(colorBin, nuevo)

	#retorna
	return binDecimal(colorMod)

def obtenerAscii(letra):
	#retorna el valor ascii del character o letra que viene por parametro
	return ord(letra)

def obtenerBinario(numero):
	"""
	bin(numero) obtiene el valor binario de numero
	[2:] obtiene los elementos de del binario anterior excepto los primeros 2, por ejemplo 11000000[2:] regresa 000000
	zfill(8) rellena con ceros a la izquiera el valor anterior hasta que este tenga longitud 8, por ejemplo 111111 regresa 00111111
	"""
	return bin(numero)[2:].zfill(8)

def obtenerLista(texto,llave):
	#variable que indicara el final del mensaje en la imagen
	caracterF = [1, 1, 1, 1, 1, 1, 1, 1]

	#variable tipo vector
	lista = []

	#para cada letra en texto haz:
	for letra in texto:
		#obtiene el valor ascii
		valorAscii = obtenerAscii(letra)

		#obtiene el valor binario
		valorBin = obtenerBinario(valorAscii)

		#para cada bit del valor binario haz:
		for bit in valorBin:
			#agrega al dinal de la lista el valor de bit
			lista.append(bit)

	#para cada bit en caracterF haz:
	for bit in caracterF:

		#agrega al final de la lista el valor de bit
		lista.append(bit)
	return lista

def ayuda():
	#imprime la forma de utilizar la herramienta
	print ('\nPara usar ejecuta:\nleer.py -e <archivo de entrada> -s <archivo de salida> -m <archivo con el mensaje> -k <llave de tipo entero> -i True <imprime las matrices> \n')
	print ('Otra forma:\nleer.py --entrada <archivo de entrada> --salida <archivo de salida> --mensaje <archivo con el mensaje> --llave <llave de tipo entero> --imprimeM True<imprime las matrices>\n')

#verifica si Mendacium.py(este programa) ha sido importado y se esta ejecutando como modulo de otro programa
if __name__ == "__main__":

	"""
	sys.argv reconoce la ejecucion del programa en consola tomando el nombre del programa(Mendacium.py] como sys.argv[0],
	por lo tanto, sys.argv[1:] equivaldria a las opciones que ponemos en consola: -e, -s, -m, -k, etc
	este if comprueba si lo que viene despues de sys.argv[0] es diferente de argumentos vacios
	"""
	if sys.argv[1:] != []:
		principal(sys.argv[1:]) # sys.argv[1:] obtiene los parametros que se pasan por consola
	else:
		ayuda()