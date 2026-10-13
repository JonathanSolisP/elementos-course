# Semana 11: Interfaces de Consola con `rich` y `questionary`

Hasta ahora nuestros programas usan `print()` e `input()`. Funcionan, pero el usuario puede escribir cualquier cosa y la salida es texto plano. Esta semana usamos dos librerías que mejoran mucho la experiencia en la terminal:

| Librería      | ¿Para qué sirve?                                         | Reemplaza a... |
|---------------|----------------------------------------------------------|----------------|
| `rich`        | **Mostrar** información bonita: colores, tablas, paneles, barras de progreso | `print()`      |
| `questionary` | **Pedir** información: menús con flechas, checkboxes, confirmaciones, validación | `input()`      |

## Instalación

```bash
pip install rich questionary
```

> `questionary` necesita una terminal real (PowerShell, CMD, Terminal de VS Code). No funciona dentro de la consola "Run" de algunos IDEs ni en IDLE.

> Si aparece `UnicodeEncodeError` al imprimir `₡` o emojis (consolas antiguas de Windows), ejecutar antes en PowerShell: `$env:PYTHONUTF8 = "1"`

## Archivos de esta semana

| Archivo                  | Contenido                                               |
|--------------------------|---------------------------------------------------------|
| `intro_rich.py`          | Colores, estilos, `Console`, `Table`, `Panel`, `track`  |
| `intro_questionary.py`   | `text`, `password`, `select`, `checkbox`, `confirm`, validación |
| `menu_mejorado.py`       | El menú de Starbucks de la Semana 3, rehecho con ambas librerías |
| `PRACTICA.md`            | Enunciado de la práctica: **Cafetería TEC**             |
| `practica_esqueleto.py`  | Código base para iniciar la práctica                    |

---

## 1. `rich` en 5 minutos

```python
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

# Texto con estilos (markup tipo BBCode)
console.print("[bold green]Éxito:[/bold green] archivo guardado")
console.print("Precio total:", 4500, style="bold yellow")

# Panel (un recuadro con título)
console.print(Panel("Bienvenido al sistema", title="TEC", border_style="cyan"))

# Tabla
tabla = Table(title="Productos")
tabla.add_column("Nombre", style="cyan")
tabla.add_column("Precio", justify="right", style="green")
tabla.add_row("Café", "₡1500")
tabla.add_row("Pan", "₡800")
console.print(tabla)
```

Ideas clave:
- `[estilo]texto[/estilo]` aplica colores/estilos: `bold`, `italic`, `underline`, `red`, `white on blue`...
- Todo lo que `rich` dibuja (tablas, paneles) se muestra con `console.print(...)`.
- `add_row` **solo recibe strings**: hay que convertir números con `str()` o f-strings.

## 2. `questionary` en 5 minutos

```python
import questionary

nombre = questionary.text("¿Cómo te llamas?").ask()

opcion = questionary.select(
    "¿Qué deseas hacer?",
    choices=["Comprar", "Ver carrito", "Salir"],
).ask()

extras = questionary.checkbox(
    "Extras:",
    choices=["Leche de almendra", "Crema", "Canela"],
).ask()            # devuelve una LISTA

seguro = questionary.confirm("¿Confirmar pedido?").ask()   # devuelve True/False
```

Ideas clave:
- Siempre se termina con `.ask()`: ahí es donde se muestra la pregunta y se obtiene la respuesta.
- `select` → devuelve **un string**; `checkbox` → devuelve **una lista**; `confirm` → devuelve **un bool**.
- Si el usuario presiona `Ctrl+C`, `.ask()` devuelve `None`. Hay que tomarlo en cuenta.
- `validate=` permite rechazar respuestas inválidas **antes** de que lleguen a nuestro código.

```python
def es_numero_positivo(texto):
    if texto.isdigit() and int(texto) > 0:
        return True
    return "Debe ser un número entero mayor que 0"   # mensaje de error

cantidad = questionary.text("Cantidad:", validate=es_numero_positivo).ask()
cantidad = int(cantidad)   # text() siempre devuelve string
```

## 3. Juntando ambas

El patrón típico de un programa de consola es un **ciclo de menú**:

```python
while True:
    opcion = questionary.select("Menú principal", choices=[...]).ask()
    if opcion == "Salir" or opcion is None:
        break
    elif opcion == "...":
        ...           # cada opción llama a una función
```

- `questionary` → decide **qué hacer**.
- `rich` → **muestra el resultado**.

Ver `menu_mejorado.py` para un ejemplo completo y luego `PRACTICA.md`.

## Referencias

- Documentación de rich: https://rich.readthedocs.io
- Documentación de questionary: https://questionary.readthedocs.io
- Ver todos los estilos/colores: `python -m rich` (demo en la terminal)
