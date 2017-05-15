# Autómatas y lenguajes formales
## Práctica 2: Algoritmo CYK

### Integrantes
- Casas Monreal Juan

Para la realización de esta práctica se utilizó el lenguaje de programación 
Python en su versión 3.
Se usó una clase para la asbtracción de una gramática y un arreglo 
bidimensional para representar la matriz que se usa en el algoritmo.

### USO
Para el uso del programa se usará el siguiente comando
	
	python3 src/programa.py -g <ARCHIVO DE GRAMÁTICA.cfg> -w <CADENA>

pudiendo usar al último la bandera -v para el modo verbose, el cual imprime la
matriz en tiempo de ejecución.
	
	python3 src/programa.py -g <ARCHIVO DE GRAMÁTICA.cfg> -w <CADENA> -v

Se incluye una gramática para la prueba del programa.
#### Consideraciones
Es necesario que las gramáticas dadas siempre respeten este formato

	2 # El número de símbolos terminales seguido de los mismos.
	(
	)
	4 # El número de símbolos no terminales seguido de los mismos.
	S
	T
	Y
	X
	S # El símbolo inicial
	6 # El número de producciones seguidas de las mismas
	S T Y
	S T X
	S S S
	Y S X
	X )
	T (
El uso de espacios en las producciones es de suma importancia, de lo
contrario, el programa no funcionará.