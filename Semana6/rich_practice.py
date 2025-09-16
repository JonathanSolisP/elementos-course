from rich import print

print("Hello, World!")

# print("Hello, World!", style="bold red")

# print("Hello, World!", style="bold red", end="\n")


print("[bold magenta]Magenta[/bold magenta]")
print("[bold cyan]Cyan[/bold cyan]")
print("[italic yellow]Yellow[/italic yellow]")
print("[bold green]Green[/bold green]")
print("[bold blue]Blue[/bold blue]")
print("[bold red]Red[/bold red]")
print("[bold white on green]White on Green[/bold white on green]")
print("[bold yellow on blue]Yellow on Blue[/bold yellow on blue]")
print("[bold red on yellow]Red on Yellow[/bold red on yellow]")
print("[bold blue on red]Blue on Red[/bold blue on red]")
print("[bold cyan on yellow]Cyan on Yellow[/bold cyan on yellow]")
print("[bold magenta on cyan]Magenta on Cyan[/bold magenta on cyan]")
print("[bold white on red]White on Red[/bold white on red]")
print("[bold white on blue]White on Blue[/bold white on blue]")
print("[bold white on cyan]White on Cyan[/bold white on cyan]")
print("[bold white on magenta]White on Magenta[/bold white on magenta]")


from rich.table import Table

table = Table(show_header=True, show_lines=True)
table.add_column("Name", style="cyan", justify="center")
table.add_column("Age", style="green", justify="center")
table.add_column("City", style="magenta", justify="center")
table.add_row("John", "25", "New York")
table.add_row("Alice", "30", "San Francisco")
table.add_row("Bob", "44", "Paris")
table.add_row("Charlie", "18", "Berlin")
table.add_row("Dave", "29", "Tokyo")
print(table)
