# -*- coding: utf-8 -*- 

from gramatica import Gramatica
import sys


def arg_correctos():
	if len(sys.argv) == 2:
		print("-g ARCHIVO DE GRAMÁTICA")
		print("-w 'CADENA'")
		print("-v VERBOSE")
	if len(sys.argv) == 5:
		if sys.argv[1] == "-g" and sys.argv[3] == "-w":
			return True
		else: return False
	if len(sys.argv) == 6:
		if sys.argv[1] == "-g" and sys.argv[3] == "-w" and sys.argv[5] == "-v":
			return True
		else: return False

def main():
	if not arg_correctos():
		print("USO: python programa.py -g ARCHIVO DE GRAMÁTICA -w 'CADENA' ('' OPCIONALES)")
		sys.exit()
	if len(sys.argv) == 6:
		main_verbose()
	else: main_normal()

def main_normal():
	entrada = sys.argv[2]
	cadena = sys.argv[4]
	f = open(entrada, "r")
	lineas = f.readlines()
	terminales = []
	variables = []
	inicial = None
	reglas = []
	contador = 0
	i = None
	t = None
	n = None
	r = None
	for linea in lineas:
		if contador == 0:
			t = int(linea.rstrip())
			contador += 1
		elif t > 0:
			terminales.append(linea.rstrip())
			t -= 1
		elif t == 0:
			n = int(linea.rstrip())
			t = -1
		elif n > 0:
			variables.append(linea.rstrip())
			n -= 1
		elif n == 0:
			inicial = linea.rstrip()
			n = -1
		elif n == -1:
			r = int(linea.rstrip())
			n = -2
		elif r > 0:
			reglas.append(linea.rstrip())
			r -= 1

	g = Gramatica(terminales, variables, inicial, len(reglas), reglas)
	print(g)
	res = g.cyk(cadena)
	if res == True:
		print("La cadena " + cadena + " pertenece a la gramática.")
	else: print("La cadena " + cadena + " no pertenece a la gramática.")

def main_verbose():
	entrada = sys.argv[2]
	cadena = sys.argv[4]
	f = open(entrada, "r")
	lineas = f.readlines()
	terminales = []
	variables = []
	inicial = None
	reglas = []
	contador = 0
	i = None
	t = None
	n = None
	r = None
	for linea in lineas:
		if contador == 0:
			t = int(linea.rstrip())
			contador += 1
		elif t > 0:
			terminales.append(linea.rstrip())
			t -= 1
		elif t == 0:
			n = int(linea.rstrip())
			t = -1
		elif n > 0:
			variables.append(linea.rstrip())
			n -= 1
		elif n == 0:
			inicial = linea.rstrip()
			n = -1
		elif n == -1:
			r = int(linea.rstrip())
			n = -2
		elif r > 0:
			reglas.append(linea.rstrip())
			r -= 1

	g = Gramatica(terminales, variables, inicial, len(reglas), reglas)
	print(g)
	res = g.cyk_verbose(cadena)
	if res == True:
		print("La cadena " + cadena + " pertenece a la gramática.")
	else: print("La cadena " + cadena + " no pertenece a la gramática.")

if __name__ == '__main__':
	main()