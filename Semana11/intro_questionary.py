import questionary

# Ejecutar en una terminal real: python intro_questionary.py

# 1. text: pide texto libre (siempre devuelve un string)
nombre = questionary.text("¿Cómo te llamas?").ask()
print("Hola,", nombre)

# 2. text con valor por defecto
carrera = questionary.text("¿Qué carrera estudias?", default="Computación").ask()

# 3. password: oculta lo que se escribe
clave = questionary.password("Escribe una contraseña:").ask()
print("Tu contraseña tiene", len(clave), "caracteres")


# 4. validación: la función devuelve True si es válido,
#    o un string con el mensaje de error
def validar_edad(texto):
    if not texto.isdigit():
        return "Escribe solo números"
    if int(texto) < 15 or int(texto) > 99:
        return "La edad debe estar entre 15 y 99"
    return True


edad = int(questionary.text("¿Cuántos años tienes?", validate=validar_edad).ask())
print("En 10 años tendrás", edad + 10)

# 5. select: elegir UNA opción con las flechas (devuelve un string)
lenguaje = questionary.select(
    "¿Cuál es tu lenguaje favorito?",
    choices=["Python", "Java", "C", "JavaScript"],
).ask()
print("Elegiste:", lenguaje)

# 6. checkbox: elegir VARIAS opciones con espacio (devuelve una lista)
cursos = questionary.checkbox(
    "¿Qué cursos llevas este semestre?",
    choices=["Elementos", "Cálculo", "Matemática Discreta", "Inglés"],
).ask()
print("Llevas", len(cursos), "cursos:", cursos)

# 7. confirm: sí / no (devuelve True o False)
if questionary.confirm("¿Te gusta programar?").ask():
    print("¡Excelente!")
else:
    print("Ya te va a gustar :)")

# 8. Choices con valor distinto al texto mostrado
precio = questionary.select(
    "Elige un tamaño:",
    choices=[
        questionary.Choice("Pequeño (₡1200)", value=1200),
        questionary.Choice("Mediano (₡1500)", value=1500),
        questionary.Choice("Grande (₡1800)", value=1800),
    ],
).ask()
print("Vas a pagar ₡", precio)   # precio ya es un int

# 9. Ctrl+C: .ask() devuelve None
respuesta = questionary.text("Presiona Ctrl+C para probar:").ask()
if respuesta is None:
    print("Cancelaste la pregunta")
