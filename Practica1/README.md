# Autómatas y lenguajes formales - Práctica 1
# Autómatas finitos y expresiones regulares.

## Integrantes
- Casas Monreal Juan

### Autómatas finitos deterministas y no deterministas
Ejercicio 1: Se tomó un estado donde los números de 1's fueran impares y otro 
donde fueran pares (no finales) y luego, si se tenían 0's, la cadena podía ser par o impar.

Ejercicio 2: Lo que importó en este ejercicio es el cuarto símbolo, cuando llegamos
al estado (del cuarto símbolo) ponemos un ciclo (aquí entra el no determinismo) y luego estados para los últimos 3 símbolos.

Ejercicio 3: El ejercicio requiere que el autómata tenga 5 estados por ser de múltiplos de 5.
Para fines prácticos, se tomaron los múltiplos de 5 (en base 10) y luego se acomodaron las 
transiciones siguiendo los patrones.

Ejercicio 4: Se tomaron estados para las diferentes cadenas "base" están en la expresión
regular: 01, 011 y 0111. Dependiendo de cuáles vinieran en la cadena se va a un estado u otro.

### Expresiones regulares
Ejercicio 1: Primero se tomó una regex para los diferentes tipos de meses; los que tenían
31 días, los que tenían 30 días y un caso específico de días para febrero de la forma
DD/MM y luego, a esa cadena, se le concatenaba los años los cuales no tenían ningún tipo
de reestricción.

Ejercicio 2: Como todos los verbos infinitivos en español terminan en ar, er, ir
se tomó una regex así: (ar|er|ir)$
##### CSV
Ejercicio 1: Para este ejercicio había dos casos, el caso donde teníamos al menos
una de éstas [0-9a-z],+ y el caso donde tenemos "[0-9a-z,/?]"

Ejercicio 2: Tomamos las cadenas que comienzan con http o https y luego cualquier 
cadena alfanumérica (incluyendo símbolos como / y .) y con terminación .net.
Luego, para el reemplazo, se usaron las referencias de sed para obtener lo que sigue de
(http|https) y precede a .net, a esa cadena le "pegamos" nuevo prefijo y sufijo:
https:// y .com.

Ejercicio 3: Para este caso, se usó sed de la forma sed -E "s///";"s///";"s///",
luego, se le pasa a la cadena cada caso que se solicita y se reemplazan los caracteres
que no nos interesan para limpiarla.

###### Archivos
- DATE.jff es el autómata que acompaña al ejercicio 1 de expresiones regulares.
- URL.jff es el autómata que acompaña al ejercicio 2 de los CSV.
- VERBOS.jff es el autómata que acompaña al ejercicio 2 de epxresiones regulares.
- CSV.jff es el autómata que acompaña al ejercicio 1 de los CSV.

