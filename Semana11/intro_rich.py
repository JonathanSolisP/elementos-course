import time

from rich.console import Console
from rich.panel import Panel
from rich.progress import track
from rich.table import Table

console = Console()

# 1. Texto con estilos
console.rule("[bold]1. Estilos de texto")
console.print("Texto normal")
console.print("[bold]Negrita[/bold], [italic]itálica[/italic] y [underline]subrayado[/underline]")
console.print("[red]Error[/red] | [yellow]Advertencia[/yellow] | [green]Éxito[/green]")
console.print("[bold white on blue] Fondo de color [/bold white on blue]")
console.print("También se puede usar style=", style="bold magenta")

# Emojis por nombre
console.print(":coffee: :thumbs_up: :warning: :cross_mark:")

# 2. Paneles
console.rule("[bold]2. Paneles")
console.print(Panel("Bienvenido a Elementos de Computación", title="TEC", border_style="cyan"))
console.print(Panel.fit("[green]Panel ajustado al texto[/green]", border_style="green"))

# 3. Tablas (a partir de una lista de diccionarios)
console.rule("[bold]3. Tablas")
estudiantes = [
    {"nombre": "Ana", "carne": "2025001", "nota": 95},
    {"nombre": "Luis", "carne": "2025002", "nota": 68},
    {"nombre": "María", "carne": "2025003", "nota": 82},
]

tabla = Table(title="Notas del curso", show_lines=True)
tabla.add_column("Carné", style="dim")
tabla.add_column("Nombre", style="cyan")
tabla.add_column("Nota", justify="right")
tabla.add_column("Estado", justify="center")

for est in estudiantes:
    if est["nota"] >= 70:
        estado = "[green]Aprobado[/green]"
    else:
        estado = "[red]Reprobado[/red]"
    # add_row solo acepta strings
    tabla.add_row(est["carne"], est["nombre"], str(est["nota"]), estado)

console.print(tabla)

# 4. Barra de progreso
console.rule("[bold]4. Progreso")
for paso in track(range(20), description="Procesando..."):
    time.sleep(0.05)
console.print("[bold green]¡Listo![/bold green]")

# 5. Spinner de estado
with console.status("Conectando al servidor..."):
    time.sleep(1.5)
console.print(":white_check_mark: Conectado")
