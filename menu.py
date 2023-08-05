import funciones.actividad as func

print("""1. Crear un programa que pida al usuario ingresar su nombre y edad y los imprima en pantalla.
2. Escribir una función que calcule el área de un círculo dado su radio.
3. Crear un programa que genere una lista de números aleatorios y los imprima en pantalla.
4. Escribir un programa que determine si un número dado es par o impar.
5. Crear una función que convierta grados Fahrenheit a grados Celsius.
6. Crear un programa que calcule la suma de los números en una lista dada.
7. Escribir un programa que encuentre el número más grande y el más pequeño en una lista dada.
8. Crear una función que invierta el orden de los elementos en una lista dada.
9. Crear un programa que genere una matriz de números y la imprima en pantalla.
10. Escribir una función que calcule el factorial de un número dado.
11. Crear un programa que genere una lista de números pares entre 1 y 100.
12. Crear un programa que imprima los números del 1 al 10 utilizando un ciclo for.
13. Crear un programa que pida al usuario ingresar dos números y calcule su suma, resta, multiplicación y
división.
14. Escribir una función que calcule la media aritmética de una lista de números.
15. Crear un programa que pida al usuario ingresar una cadena de texto y determine si es un palíndromo o no.""")


seleccion=int(input("Que punto quiere realizar: "))

if seleccion==1:
    func.nombre()
if seleccion==2:
    func.area_circulo(int(input("ingrese el radio del circulo: ")))
if seleccion==3:
    print(func.lista_general)
if seleccion==4:
    func.par_o_impar(int(input("ingrese el num a evaluar: ")))
if seleccion==5:
    func.gradosCelsius(int(input("ingrese los grados fahrenheit")))
if seleccion==6:
    print("la suma de los numeros de ", func.lista_general, "es:",func.suma_Lista(func.lista_general))
if seleccion==7:
    func.min_max(func.lista_general)
if seleccion==8:
    print(func.invertir_lista(func.lista_general))
if seleccion==9:
    print("la matriz es: ", func.matriz_Aleatoria_punto(int(input("ingrese el num de filas que desea tenga la matriz: "))))
if seleccion==10:
    print(func.factorial(int(input("ingrese el numero al que desea sacar el factorial: "))))
if seleccion==11:
    func.pares_0_100()
if seleccion==12:
    func.numeros1_a_10()
if seleccion==13: 
    func.operaciones(int(input("ingrese el primer numero a operar: ")), int(input("ingrese el segundo numero a operar: ")))
if seleccion==14:
    print(func.media_aritmetica(func.lista_general))
if seleccion==15:
    texto_usuario=input("ingrese el texto a comparar: " )   
    if func.polindromo(texto_usuario):
        print("el texto es palindromo")
    else:
        print("el texto no es palindromo")
    
