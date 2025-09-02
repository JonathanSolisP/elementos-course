def sumar(a, b):
    print(a + b)

def restar(a, b):
    print(a - b)

def dividir(a, b):
    if (b == 0):
        print('Division entre 0 no es posible')
    else:
        print(a / b)

sumar(5, 10)
restar(10, 5)
dividir(10, 0)
dividir(10, 2)

# == != < > <= >=
def calificar(nota):
    if (nota < 65):
        print('Reprobado')
    elif (nota < 90):
        print('Aprobado')
    else:
        print('Distinguido')

nota = int(input('Ingrese su nota: '))

# 50 -> '50'
# str(50) -> '50'
# int('50') -> 50
calificar( int(nota) )
calificar(50)
calificar(95)