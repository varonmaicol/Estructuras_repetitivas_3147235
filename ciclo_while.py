#ejercicio 1
#Imprimir la tabla de multiplicar de 
#un numero que un usuario ingrese 
#por teclado utilizando el ciclo 
#while 

numero = int(input("Ingrese un numero: ")) 
i = 10
while i>=1:
   resultado =  numero * i
   print(numero, "x", i, "=", resultado) 
   i= i - 1
