# Ubicacion: Mansion
llave_roja = False

from os import system

def limpiar():
    system('cls')

def mansion_recibidor():
    limpiar()
    print('Estas en el recibidor')
    print('Hay cuadros antiguos en las paredes y una alfombra roja en el suelo.')
    print('1. Subir las escaleras')
    print('2. Regresar al calle')
    print('3. Entrar a la cocina')
    seleccion = input('Seleccione una opcion: ')
    if (seleccion == '1'):
        print('Subiendo las escaleras...')
    elif (seleccion == '2'):
        calle()
    elif (seleccion == '3'):
        print('Entrando a la cocina...')
    else:
        mansion_recibidor()

def calle():
    limpiar()
    print('Estas en la calle')
    print('Hay una mansion abandonada al frente, la puerta parece entreabierta...')
    print('1. Entrar a la mansion')
    print('2. Darme media vuelta e irme')
    seleccion = input('Seleccione una opcion: ')
    if (seleccion == '1'):
        mansion_recibidor()
    elif (seleccion == '2'):
        print('Te fuiste a tu casa, fin del juego')
    else:
        calle()

calle()

