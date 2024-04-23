# AlgoritmosTransformaciones
Implementación de los algoritmos de Transformaciones propuestos en clase 

Asignación: Lenguajes de programación y transducción

Docente: Joaquin F. Sánchez

Trabajo: Algoritmos de Transformaciones

Grupo 02

Integrantes del grupo: Valentina Andrade - Mateo Patiño - Nicolás Ramírez

Pasos para la ejecución de main.py (ejecucion con python):

Descargar los archivos en python nombrearchivo.py
Abrir la línea de consola de la carpeta que contenga el archivo
Si se desea realizar modificaciones en la gramatica o ingresar una distinta, ingrese al código y a partir de la línea 73 hasta la línea que sea necesario, cambie o ingrese la nueva gramática que se desea probar
Ejecutar con el siguiente comandos: $ python3 main.py
Revisar los resultados generados por consola


Gramaticas ANTLR:

Se tomaron en cuenta los tres ejemplos de gramatica de la presentación 10 de Teams. Definimos que:
-gramatica#.g4 contiene la gramatica original
-gramaticasr#.g4 contiene la gramatica sin recursión por la izquierda
-gramaticaf#.g4 contiene la gramatica despues de la factorización por la izquierda

*Para el ejercicio 1 si es una LL(1) ya que desde la gramatica original se mostraba como una gramatica sin ambiguedad ni recursión por la izquierda.
*En el caso del ejercicio 2, la gramatica propuesta no es LL(1) debido a que esta esrecursiva y ambigua ya que desde un terminal se puede llegar a si mismo. Ejemplo: desde S siguiendo sus reglas se llega a si mismo.
*En cuanto al ejercicio 3 la gramatica resultante si es una LL(1), especificamente en este caso tanto la gramatica original como la resultante no son ambiguas y para la recursividad esta se elimino de manera exitosa para la gramatica resultante haciendo que esta sea LL(1)

Pasos para la ejecución de ANTLR (el nombre del archivo .g4 varia, tener eso en cuenta):
$ antlr4 gramatica#.g4
$ ls //verificar que se hayan creado los archivos necesarios
$ java *.java
$ grun gramatica# s -tree
>//para este punto se deberán ingresar las cadenas que quieran ser validadas

Si se desea ver el arbol que genera ANTLR deberá ejecutar los siguientes comandos:
$ grun gramatica# s -gui
>//para este punto se deberán ingresar las cadenas que quieran ser validadas

psp#.png -> esa imagen muestra el conjunto de primeros, siguientes y de predicción
