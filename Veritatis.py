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
# programa hecho para python 2.7.13
#$ chmod +x test.py     # This is to make file executable
#$./test.py

def obtenerLSB(byte):
	return byte[-1]

def obtenerBinario(numero):
	return bin(numero)[2:].zfill(8)

def binDecimal(binario):
	return int(binario, 2)

def asciiStr(valor):
	#convierte el valor que llega por parametro en una letra
	return chr(valor)

def obtenerMensaje(llave, ruta):
	imagen = Image.open(ruta) #abre la imagen de la ruta
	pixeles = imagen.load()

	tamano = imagen.size
	ancho = tamano[0]
	alto = tamano[1]
	
	byte = ""
	criptograma = ""
	indicador = "11111111"

	print("Obteniendo mensaje. . .")
	for x in xrange(ancho):
		for y in xrange(alto):
			pixel = pixeles[x, y]

			rojo = pixel[0]
			verde = pixel[1]
			azul = pixel[2]

			byte += obtenerLSB(obtenerBinario(rojo))
			if len(byte) >= 8:
				if byte == indicador:
					break
				#a la representacion decimal de byte se le resta la llave y se le aplica modulo 255
				#el proceso inverso del cifrado cesar
				criptograma += asciiStr((binDecimal(byte)-llave)%255)
				byte = ""

			byte += obtenerLSB(obtenerBinario(verde))
			if len(byte) >= 8:
				if byte == indicador:
					break
				criptograma += asciiStr((binDecimal(byte)-llave)%255)
				byte = ""

			byte += obtenerLSB(obtenerBinario(azul))
			if len(byte) >= 8:
				if byte == indicador:
					break
				criptograma += asciiStr((binDecimal(byte)-llave)%255)
				byte = ""
		else:
			continue
		break
	print (criptograma)

def ayuda():
	print ('\nPara usar ejecuta:\nVeritatis.py -e <archivo de entrada> -k <llave de tipo entero>\n')
	print ('Otra forma:\nVeritatis.py --entrada <archivo de entrada> --llave <llave de tipo entero>\n')

if __name__ == "__main__":
	if sys.argv[1:] != []:
		try:
			opts, args = getopt.gnu_getopt(sys.argv[1:],"e:k:h",["entrada=","llave="])
		except getopt.GetoptError as e:
			print (e)
			ayuda()
			sys.exit(2)
		for opt, arg in opts:
			if opt == '-h':
				ayuda()
				sys.exit()
			elif opt in ("-e", "--entrada"):
				archivoentrada = arg
			elif opt in  ("-k", "--llave"):
				clave = arg
		obtenerMensaje(int(clave), archivoentrada)
	else:
		ayuda()