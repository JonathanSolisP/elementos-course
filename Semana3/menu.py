def menuCafe():
    print('Comprando cafe...')
    print('1. Expresso')
    print('2. Americano')
    print('3. Latte')
    seleccion = input('Seleccione una opcion: ')
    if (seleccion == '1'):
        print('Compraste un expresso')
    elif (seleccion == '2'):
        print('Compraste un americano')
    elif (seleccion == '3'):
        print('Compraste un latte')

def menuChocolate():
    print('Comprando chocolate...')
    print('1. Caliente')
    print('2. Frio')
    seleccion = input('Seleccione una opcion: ')
    if (seleccion == '1'):
        print('Compraste un chocolate caliente')
    elif (seleccion == '2'):
        print('Compraste un chocolate frio')

def starbucks():
    print('Bienvenidos a Starbucks ☕')
    print('1. Comprar cafe')
    print('2. Comprar chocolate')
    print('3. Comprar pan')
    print('4. Salir')
    seleccion = input('Seleccione una opcion: ')
    if (seleccion == '1'):
        menuCafe()
    elif (seleccion == '2'):
        menuChocolate()
starbucks()