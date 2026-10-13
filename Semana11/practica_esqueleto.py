import questionary
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

# Práctica Semana 11 - Cafetería TEC
# Completar las funciones marcadas con TODO. Ver PRACTICA.md

console = Console()

CLAVE_ADMIN = "tec2026"
DESCUENTO_ESTUDIANTE = 0.10
EXTRAS = {"Leche de almendra": 300, "Crema": 200, "Shot extra": 400}
CATEGORIAS = ["Bebidas", "Comida", "Postres"]

productos = [
    {"codigo": "C01", "nombre": "Café negro", "categoria": "Bebidas", "precio": 1000, "stock": 20},
    {"codigo": "C02", "nombre": "Latte", "categoria": "Bebidas", "precio": 1800, "stock": 15},
    {"codigo": "C03", "nombre": "Chocolate", "categoria": "Bebidas", "precio": 1500, "stock": 0},
    {"codigo": "P01", "nombre": "Empanada", "categoria": "Comida", "precio": 1200, "stock": 10},
    {"codigo": "P02", "nombre": "Sandwich", "categoria": "Comida", "precio": 2500, "stock": 4},
    {"codigo": "D01", "nombre": "Brownie", "categoria": "Postres", "precio": 1300, "stock": 8},
]

ventas = []


# ---------- Validaciones ----------

def validar_no_vacio(texto):
    if texto.strip() == "":
        return "Este campo no puede estar vacío"
    return True


def validar_entero_positivo(texto):
    # TODO: devolver True si texto es un entero > 0, si no, un mensaje de error
    pass


# ---------- Utilidades ----------

def buscar_producto(codigo):
    for producto in productos:
        if producto["codigo"] == codigo:
            return producto
    return None


def mostrar_menu_productos():
    tabla = Table(title="Menú")
    tabla.add_column("Código", style="dim")
    tabla.add_column("Producto", style="cyan")
    tabla.add_column("Categoría", style="magenta")
    tabla.add_column("Precio", justify="right", style="green")
    tabla.add_column("Disponible", justify="center")
    # TODO: agregar una fila por producto. Si stock == 0 mostrar "[red]Agotado[/red]"
    console.print(tabla)


# ---------- Modo cliente ----------

def agregar_al_pedido(pedido):
    # TODO:
    # 1. select de categoría
    # 2. select de producto (solo los que tienen stock > 0)
    #    Tip: questionary.Choice(f"{p['nombre']} - ₡{p['precio']}", value=p["codigo"])
    # 3. text con validate para la cantidad (no mayor al stock)
    # 4. si es bebida, checkbox de EXTRAS
    # 5. agregar un diccionario al pedido
    pass


def ver_pedido(pedido):
    # TODO: tabla con el pedido actual y opción de quitar un producto
    pass


def imprimir_factura(venta):
    # TODO: Panel + Table + totales (ver PRACTICA.md, Parte 2)
    pass


def finalizar_compra(cliente, pedido):
    # TODO: descuento, método de pago, vuelto, confirmar,
    # descontar stock, guardar en ventas e imprimir factura.
    # Devolver True si la compra se realizó.
    return False


def modo_cliente():
    cliente = questionary.text("Nombre del cliente:", validate=validar_no_vacio).ask()
    if cliente is None:
        return
    pedido = []
    while True:
        opcion = questionary.select(
            f"Pedido de {cliente} ({len(pedido)} productos)",
            choices=["Ver menú", "Agregar producto", "Ver pedido", "Finalizar compra", "Volver"],
        ).ask()
        if opcion == "Ver menú":
            mostrar_menu_productos()
        elif opcion == "Agregar producto":
            agregar_al_pedido(pedido)
        elif opcion == "Ver pedido":
            ver_pedido(pedido)
        elif opcion == "Finalizar compra":
            if finalizar_compra(cliente, pedido):
                break
        else:  # "Volver" o None
            break


# ---------- Modo administrador ----------

def login_admin():
    # TODO: hasta 3 intentos con questionary.password. Devolver True/False
    return False


def ver_inventario():
    # TODO
    pass


def agregar_producto():
    # TODO
    pass


def reabastecer():
    # TODO
    pass


def eliminar_producto():
    # TODO
    pass


def reporte_ventas():
    # TODO
    pass


def modo_admin():
    if not login_admin():
        console.print("[red]Acceso denegado[/red]")
        return
    acciones = {
        "Ver inventario": ver_inventario,
        "Agregar producto": agregar_producto,
        "Reabastecer": reabastecer,
        "Eliminar producto": eliminar_producto,
        "Reporte de ventas": reporte_ventas,
    }
    while True:
        opcion = questionary.select(
            "Administrador",
            choices=list(acciones.keys()) + ["Volver"],
        ).ask()
        if opcion in acciones:
            acciones[opcion]()
        else:
            break


# ---------- Programa principal ----------

def main():
    console.print(Panel.fit("[bold]Cafetería TEC[/bold] ☕", border_style="cyan"))
    while True:
        modo = questionary.select(
            "¿Cómo desea ingresar?",
            choices=["Cliente", "Administrador", "Salir"],
        ).ask()
        if modo == "Cliente":
            modo_cliente()
        elif modo == "Administrador":
            modo_admin()
        else:
            console.print("[cyan]¡Hasta luego![/cyan]")
            break


main()
