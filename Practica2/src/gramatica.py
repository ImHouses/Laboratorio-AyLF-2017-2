# -*- coding: utf-8 -*- 

class Gramatica(object):
	"""Clase para gramáticas libres de contexto en su forma normal de Chomsky"""
	def __init__(self, terminales, variables, inicial, n_producciones, producciones):
		self.terminales = terminales
		self.variables = variables
		self.inicial = inicial
		self.n_producciones = n_producciones
		self.producciones = producciones
	

	def __str__(self):
		"""Regresa una representación en cadena de la gramática libre de contexto

		Returns:
			Una representación en cadena de la gramática.
		"""
		s = "Terminales:\n"
		for t in self.terminales:
			s += t + "\n"
		s += "No terminales:\n"
		for v in self.variables:
			s += v + "\n"
		s += "Símbolo inicial: \n" + self.inicial + "\n"
		s += "Producciones: \n"
		for r in self.producciones:
			parte_derecha = ""
			i = 1
			while i < len(r):
				parte_derecha += r[i]
				i += 1
			s += r[0] + "->" + parte_derecha + "\n"
		return s

	def cyk_verbose(self, cadena):
		"""Algoritmo CYK en modo verbose, imprime la matriz en ejecución.

		Args:
			cadena: La cadena a verificar si pertenece a la GLC o no.
		Returns:
			True si la cadena pertenece a la GLC, False en otro caso.
		"""
		n = len(cadena)
		r = len(self.terminales) + len(self.variables)
		vut = self.terminales + self.variables
		M = self.genera_matriz(n)
		self.imprime_matriz(M)
		i = 0
		while i <= (n - 1):
			for prod in self.producciones:
				if len(prod) == 3:
					if prod[2] == cadena[i]:
						M[i][i] += prod[0]
			i += 1
		l = 0
		while l <= (n-1):
			r = 0
			while r <= (n - l - 1):
				t = 0
				while t <= (l - 1):
					L = M[r][r+t]
					R = M[r+t+1][r+l]
					for prod in self.producciones:
						if len(prod) == 5:
							if prod[2] in L and prod[4] in R:
								M[r][r+l] += prod[0]
								self.imprime_matriz(M) 
					t += 1
				r += 1
			l += 1

		self.imprime_matriz(M)
		if self.inicial in M[0][n-1]:
			return True
		else: return False

	def cyk(self, cadena):
		"""Algoritmo CYK normal, nos dice si la cadena dada pertenece a la GLC
		o no.

		Returns:
			True si la cadena pertenece a la GLC, False en otro caso.
		"""
		n = len(cadena)
		r = len(self.terminales) + len(self.variables)
		vut = self.terminales + self.variables
		M = self.genera_matriz(n)
		i = 0
		while i <= (n - 1):
			for prod in self.producciones:
				if len(prod) == 3:
					if prod[2] == cadena[i]:
						M[i][i] += prod[0]
			i += 1
		l = 0
		while l <= (n-1):
			r = 0
			while r <= (n - l - 1):
				t = 0
				while t <= (l - 1):
					L = M[r][r+t]
					R = M[r+t+1][r+l]
					for prod in self.producciones:
						if len(prod) == 5:
							if prod[2] in L and prod[4] in R:
								M[r][r+l] += prod[0] 
					t += 1
				r += 1
			l += 1
		if self.inicial in M[0][n-1]:
			return True
		else: return False

	def imprime_matriz(self, m):
		"""Imprime la matriz
		
		Args:
			m: La matriz que se va a imprimir.
		"""
		for i in m:
			print(str(i) + "\n")

	def genera_matriz(self, n):
		"""Genera la matriz de nxn donde n es la longitud de una cadena.
		
		Args:
			n: La longitud de una cadena dada.

		Returns: Una matriz de nxn donde n es la longitud de una cadena.
		"""
		a = []
		for x in range(n):
			row = []
			i = 0
			while i < n:
				row.append("")
				i += 1
			a.append(row)
		return a
						
			

