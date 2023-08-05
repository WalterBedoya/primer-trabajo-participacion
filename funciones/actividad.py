import random

def lista_aleatoria(longitud, inf, sup):
    lista = [random.randint(inf, sup) for i in range(longitud)]
    return lista
    

lista_general=lista_aleatoria(6,1,20)
#print(lista_general)

def matriz_Aleatoria(filas): #Matriz Fija para los demas ejercicios de matrices
    
    matriz = [lista_aleatoria(6,1,20) for x in range(filas)]
    return matriz

matriz_general=matriz_Aleatoria(3)


def nombre (): #Crear un programa que pida al usuario ingresar su nombre y edad y los imprima en pantalla.
    print("su nombre es",input("ingrese su nombre: "))
    
    print("su apellido es",input("ingrese su apellido: "))

#nombre()

def area_circulo (radio): #Escribir una función que calcule el área de un círculo dado su radio.}
    print( "el area del circulo es:", 3.14*(radio**2))

#area_circulo(int(input("ingrese el radio del circulo: ")))

def par_o_impar (x): #Escribir un programa que determine si un número dado es par o impar
    if x%2 == 0:
        print("el num es par")
    else:
        print("el num es impar")
    
#par_o_impar(int(input("ingrese el num a evaluar: ")))

def gradosCelsius(f): #rear una función que convierta grados Fahrenheit a grados Celsius.
    print("los fahrenheit ingresados son", (f-32)*5/9,"en grados celsius")

#gradosCelsius(int(input("ingrese los grados fahrenheit")))

def suma_Lista(lista): #Crear un programa que calcule la suma de los números en una lista dada
    return sum(lista)

#print("la suma de los nums de ", lista_general, "es:",suma_Lista(lista_general))

def min_max(lista): #Escribir un programa que encuentre el número más grande y el más pequeño en una lista dada

    min=max=lista[0]
    for num in lista:
        if num < min:
            min=num
        if num > max: 
            max=num
    print("De la lista: ",lista)
    print("el num maximo es: ",max)
    print("el num menor es: ",min)

#min_max(lista_general)

def invertir_lista(lista): #Crear una función que invierta el orden de los elementos en una lista dada
    print("la lista sin invertir es: ", lista_general)
    return lista[::-1]

#print(invertir_lista(lista_general))

def matriz_Aleatoria_punto(filas): #Crear un programa que genere una matriz de números y la imprima en pantalla
    
    matriz = [lista_aleatoria(6,1,20) for x in range(filas)]
    return matriz

#print("la matriz es: ", matriz_Aleatoria_punto(int(input("ingrese el num de filas que desea tenga la matriz: "))))
        
def factorial (num):#Escribir una función que calcule el factorial de un número dado

    if num == 0:
        return 1  
    else:
        factorial = 1
        for i in range(1, num + 1):
            factorial *= i
        return factorial

#print(factorial(int(input("ingrese el numero al que desea sacar el factorial: "))))

def pares_0_100(): #Crear un programa que genere una lista de números pares entre 1 y 100
    print("los pares de 0 a 100 son:" ,end=" ")
    for i in range(1,101):
        if i%2==0:
            print(i, end=" ")
        
#pares_0_100()

def numeros1_a_10(): #Crear un programa que imprima los números del 1 al 10 utilizando un ciclo for.
    print("los numeros del 1 al 10 son: ", end=" ")
    for i in range(1,11):
        print(i, end="  ")

#numeros1_a_10()

def operaciones(x,y): #Crear un programa que pida al usuario ingresar dos números y calcule su suma, resta, multiplicación y división.
    print("la suma de ambos numeros es: ", x+y)
    print("la resta de ambos numeros (en el orden que se ingresaron) es: ", x-y)
    print("la division de ambos numeros (en el orden que se ingresaron) es: ", x/y)
    print("la multiplicacion de ambos numeros es: ", x*y)

#operaciones(int(input("ingrese el primer numero a operar: ")), int(input("ingrese el segundo numero a operar: ")))

def media_aritmetica(lista): #Escribir una función que calcule la media aritmética de una lista de números.
    print(lista_general)
    suma=0
    cant=len(lista)
    for i in range(0,len(lista),1):
        suma+=lista[i]
    return suma/cant
            
#print(media_aritmetica(lista_general))
    
def polindromo(texto): #Crear un programa que pida al usuario ingresar una texto de texto y determine si es un palíndromo o no

    texto = texto.replace(" ", "").lower()
    texto_inversa = texto[::-1]
    return texto == texto_inversa

"""texto_usuario=input("ingrese el texto a comparar: " )   
if polindromo(texto_usuario):
    print("el texto es palindromo")
else:
    print("el texto no es palindromo")"""



