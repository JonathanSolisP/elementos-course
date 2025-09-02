
# Ejercicio 1
# Escriba una funcion que recibe 2 parametros
# como argumentos y retorna la multiplicacion
# de ambos valores
# para probarlos vamos a hacer 2 inputs,
# 1 por cada valor y los vamos a convertir a int
# al final se muestra el resultado de la funcion

# ctrl + k + c comenta las lineas seleccionadas
# ctrl + k + u descomenta lineas seleccionadas

def multiplicar(multiplicando, multiplicador):
    return multiplicando * multiplicador

# valor1 = int(input('Digite el primer numero: '))
# valor2 = int(input('Digite el segundo numero: '))

# resultado1 = multiplicar(valor1, valor2)
# resultado2 = multiplicar(5, 10)

# print('Resultado 1:', resultado1)
# print('Resultado 2:', resultado2)

# Ejercicio 2
# Escriba una funcion que reciba una palabra
# y una letra y debe retornar True si la letra esta
# en la palabra, de lo contrario debe retornar False
def letra_en_palabra(letra, palabra):
    return letra.lower() in palabra.lower()

palabra1 = input('Digite una palabra: ')
letra1 = input('Digite una letra: ')
print(letra_en_palabra(letra1, palabra1))

# print('C'.lower() in 'casa'.lower())

# Ejercicio 3
# Escriba una funcion que reciba 3 numeros
# como parametros y retorne el mayor de los 3

# mayor_de_los_tres(5, 6, 10) -> 10
# mayor_de_los_tres(5, 80, 10) -> 80
# condition1 and condition2 
# condition1 or condition2 

def mayor_de_los_tres(a, b, c):
    if (a >= b and a >= c):
        return a
    elif (b >= a and b >= c):
        return b
    else:
        return c

print(mayor_de_los_tres(5, 6, 10)) # -> 10
print(mayor_de_los_tres(5, 80, 10)) # -> 80






# Ejercicio 4
# Juego de inputs + mapa
