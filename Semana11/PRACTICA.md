# Práctica Semana 11: Cafetería TEC ☕

## Objetivo

Construir un sistema de consola para la cafetería del TEC usando **`questionary`** para toda la entrada del usuario y **`rich`** para toda la salida. No se permite usar `input()`.

La práctica integra lo visto en el curso: variables, decisiones, ciclos, funciones, listas y diccionarios.

- **Modalidad:** parejas
- **Tiempo sugerido:** 2 clases (≈ 3–4 horas) + trabajo en casa
- **Entregable:** un archivo `cafeteria.py` (puede partir de `practica_esqueleto.py`)

---

## Descripción general

Al iniciar, el programa muestra un panel de bienvenida y pregunta el **modo**:

```
? ¿Cómo desea ingresar?
 » Cliente
   Administrador
   Salir
```

### Estructuras de datos

El inventario se guarda en una lista de diccionarios:

```python
productos = [
    {"codigo": "C01", "nombre": "Café negro", "categoria": "Bebidas", "precio": 1000, "stock": 20},
    {"codigo": "C02", "nombre": "Latte",      "categoria": "Bebidas", "precio": 1800, "stock": 15},
    {"codigo": "P01", "nombre": "Empanada",   "categoria": "Comida",  "precio": 1200, "stock": 10},
    ...
]
```

Las ventas realizadas se guardan en otra lista:

```python
ventas = [
    {"cliente": "Ana", "items": [...], "total": 4300, "metodo_pago": "SINPE"},
    ...
]
```

---

## Parte 1: Modo Cliente (40 pts)

| # | Requisito | Herramienta | Pts |
|---|-----------|-------------|-----|
| 1.1 | Pedir el nombre del cliente. No puede estar vacío. | `text` + `validate` | 4 |
| 1.2 | Mostrar el menú en una **tabla** agrupada/ordenada por categoría. Los productos con stock 0 se muestran en rojo como "Agotado". | `Table` | 8 |
| 1.3 | Agregar productos al pedido: elegir categoría → producto (solo con stock > 0) → cantidad (número válido, no mayor al stock disponible). | `select`, `text` + `validate` | 10 |
| 1.4 | Extras para bebidas (leche de almendra +₡300, crema +₡200, shot extra +₡400). Pueden elegir varios o ninguno. | `checkbox` | 6 |
| 1.5 | Ver/quitar productos del pedido actual. | `Table`, `select` | 4 |
| 1.6 | Finalizar compra: elegir método de pago (Efectivo / Tarjeta / SINPE), confirmar, descontar stock y registrar la venta. | `select`, `confirm` | 8 |

**Reglas de negocio:**
- Estudiantes con carné (preguntar con `confirm`) tienen **10 % de descuento**.
- Si paga en efectivo, preguntar con cuánto paga y mostrar el vuelto (el monto debe ser ≥ total).

## Parte 2: Factura (15 pts)

Al confirmar la compra se imprime una factura usando `rich`:

```
╭──────────────── Cafetería TEC ────────────────╮
│ Cliente: Ana              Pago: SINPE         │
╰───────────────────────────────────────────────╯
┏━━━━━━━━━━━━━━━━━━━━┳━━━━━━┳━━━━━━━━┳━━━━━━━━━┓
┃ Producto           ┃ Cant ┃ Precio ┃ Subtotal┃
┡━━━━━━━━━━━━━━━━━━━━╇━━━━━━╇━━━━━━━━╇━━━━━━━━━┩
│ Latte + crema      │    2 │ ₡2000  │  ₡4000  │
│ Empanada           │    1 │ ₡1200  │  ₡1200  │
└────────────────────┴──────┴────────┴─────────┘
  Subtotal:   ₡5200
  Descuento:  -₡520
  TOTAL:      ₡4680
```

| # | Requisito | Pts |
|---|-----------|-----|
| 2.1 | Panel con datos del cliente y método de pago | 4 |
| 2.2 | Tabla con detalle de productos, cantidades y subtotales | 6 |
| 2.3 | Subtotal, descuento y total correctos y con formato | 3 |
| 2.4 | Barra de progreso o spinner "Preparando su pedido..." antes de la factura | 2 |

## Parte 3: Modo Administrador (30 pts)

Acceso protegido por contraseña (`password`). Máximo **3 intentos**; si falla, vuelve al menú principal.

| # | Requisito | Pts |
|---|-----------|-----|
| 3.1 | Login con contraseña y 3 intentos | 4 |
| 3.2 | Ver inventario en tabla. Stock ≤ 5 se resalta en amarillo, 0 en rojo. | 5 |
| 3.3 | Agregar producto nuevo (código único, nombre, categoría con `select`, precio y stock validados) | 7 |
| 3.4 | Reabastecer: elegir producto y sumar stock | 4 |
| 3.5 | Eliminar producto (con `confirm`) | 3 |
| 3.6 | Reporte de ventas: tabla de ventas, total vendido, producto más vendido y cantidad de ventas por método de pago | 7 |

## Parte 4: Calidad del código (15 pts)

| Criterio | Pts |
|----------|-----|
| Código dividido en funciones con nombres claros (una función por opción del menú) | 5 |
| Manejo de `Ctrl+C` / `None` sin que el programa se caiga | 4 |
| No se usa `input()` ni `print()` normal; toda la interfaz es con questionary/rich | 3 |
| Comentarios donde la lógica no es obvia, sin código repetido | 3 |

**Total: 100 pts**

---

## Bonus (hasta +10 pts)

- **+5** Guardar y cargar `productos` y `ventas` en archivos JSON para que no se pierdan al cerrar el programa (adelanto de la Semana 12).
- **+3** Búsqueda de productos usando `questionary.autocomplete`.
- **+2** Mostrar un resumen con `rich.columns.Columns` o `rich.layout` en el reporte de ventas.

---

## Plan sugerido de trabajo

| Sesión | Meta |
|--------|------|
| **Clase 1 (primera hora)** | Leer enunciado, instalar librerías, correr `intro_rich.py`, `intro_questionary.py` y `menu_mejorado.py`. Revisar `practica_esqueleto.py`. |
| **Clase 1 (segunda hora)** | Menú principal + modo cliente: mostrar menú (1.2) y agregar productos (1.3). |
| **Casa** | Extras, descuento, finalizar compra y factura (1.4 – 2.4). |
| **Clase 2 (primera hora)** | Modo administrador: login, inventario, agregar/reabastecer/eliminar (3.1 – 3.5). |
| **Clase 2 (segunda hora)** | Reporte de ventas (3.6), manejo de `None`, pruebas cruzadas entre parejas. |

## Casos de prueba mínimos

Antes de entregar, verifiquen que su programa maneja correctamente:

1. Pedir una cantidad mayor al stock disponible → debe rechazarse.
2. Escribir letras o números negativos en cantidad o precio → debe rechazarse.
3. Comprar todo el stock de un producto → debe aparecer "Agotado" y no poder elegirse.
4. Finalizar compra con el pedido vacío → mensaje de advertencia.
5. Pago en efectivo con monto menor al total → debe rechazarse.
6. Contraseña incorrecta 3 veces → regresa al menú principal.
7. Agregar un producto con un código que ya existe → debe rechazarse.
8. Presionar `Ctrl+C` en cualquier pregunta → el programa no se cae.
9. Reporte de ventas sin ventas registradas → mensaje en lugar de error.
