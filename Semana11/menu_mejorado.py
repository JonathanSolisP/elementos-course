import questionary
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

# El menú de Starbucks de la Semana 3, ahora con questionary y rich

console = Console()

MENU = {
    "Café": {"Expresso": 1200, "Americano": 1400, "Latte": 1800},
    "Chocolate": {"Caliente": 1600, "Frío": 1900},
    "Pan": {"Croissant": 1100, "Muffin": 1300},
}

carrito = []


def mostrar_menu():
    tabla = Table(title="Menú")
    tabla.add_column("Categoría", style="magenta")
    tabla.add_column("Producto", style="cyan")
    tabla.add_column("Precio", justify="right", style="green")
    for categoria, productos in MENU.items():
        for producto, precio in productos.items():
            tabla.add_row(categoria, producto, f"₡{precio}")
    console.print(tabla)


def comprar():
    categoria = questionary.select("¿Qué deseas comprar?", choices=list(MENU.keys())).ask()
    if categoria is None:
        return
    producto = questionary.select(
        f"Elige tu {categoria.lower()}:",
        choices=list(MENU[categoria].keys()),
    ).ask()
    if producto is None:
        return
    carrito.append({"producto": producto, "precio": MENU[categoria][producto]})
    console.print(f"[green]✔ {producto} agregado al carrito[/green]")


def ver_carrito():
    if len(carrito) == 0:
        console.print("[yellow]El carrito está vacío[/yellow]")
        return
    tabla = Table(title="Carrito")
    tabla.add_column("#", style="dim")
    tabla.add_column("Producto", style="cyan")
    tabla.add_column("Precio", justify="right", style="green")
    total = 0
    for i, item in enumerate(carrito, start=1):
        tabla.add_row(str(i), item["producto"], f"₡{item['precio']}")
        total += item["precio"]
    console.print(tabla)
    console.print(f"[bold]Total: ₡{total}[/bold]")


def starbucks():
    console.print(Panel.fit("Bienvenidos a Starbucks ☕", border_style="green"))
    while True:
        opcion = questionary.select(
            "Seleccione una opción:",
            choices=["Ver menú", "Comprar", "Ver carrito", "Salir"],
        ).ask()
        if opcion == "Ver menú":
            mostrar_menu()
        elif opcion == "Comprar":
            comprar()
        elif opcion == "Ver carrito":
            ver_carrito()
        else:  # "Salir" o Ctrl+C (None)
            if questionary.confirm("¿Seguro que desea salir?").ask() is not False:
                console.print("[bold cyan]¡Gracias por su visita![/bold cyan]")
                break


starbucks()
