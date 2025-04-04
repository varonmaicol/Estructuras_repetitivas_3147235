# Estructuras repetitivas 3147235
Proyecto para trabajar ciclos for y while en python 
## Conseptos clave apra trabajar en Ciclos 
* **Breackpoint (punto de interrupcion)**:
    para ejecutar una instruccion a la vez (Depuracion - debugger). 
    Permite ver el valor de las variables definidas en un programa a tra vez de la ejecucion del codigo, permitiendo observar el comportamiento del programa a tra vez del programa/codigo a traves del tiempo.

    * **Variable contadora (contador)** variable la cual podemos aumentar (disminuir) su valor en una determinada cantidad constante (de 1 en 1, de 2 en 2, etc). 

    - Una variable contadora se debe iniciar **antes de la estructura repetitiva** con un valor inicial (0)
    
    - Una variable contadora por lo general se nombra con las letras i,j
    
    - Una variable contadora 
     **debe participar en la condicional del ciclo**. 
    
    - Toda variable contadora debe tener lo que denominamos  **una intruccion de incremento**
    para aumentar su valor 
    
    - En ciclo while, la instruccion de incremento se pone al final **del bloque de codigo del ciclo**
    
* **Iteracion**: es un recorrido en la ejecucion de un ciclo 

## Ciclo while 
Estructura que permite ejecutar un bloque de codigo un numero determinado de veces. 

el bloque de codigo dentro del ciclo while se ejecutara sucesivamente 
**mientras la condicional sea evaluada como VERDADERA**. 



### Sintaxis de python: 

```
While condicional: 
   
   instruccion1
   instruccion2
   instruccion3
   ...
   condicional n
```

## Ciclo for 

Se utiliza (Python) para recorrer conjuntos de datos (Estructuras de datos - colecciones de datos) 

* El cicclo recorrera cada dato en la estructura **desde el primero hasta el ultimo**  

* Y el elemento recorrido se asigana a una varieble en el ciclo 

### Sintaxis for 
``` 
    for (variable) in (conjunto de datos)
      instruccion 1
      instruccion 2
      instruccion 3
      ...
      instruccion n
```