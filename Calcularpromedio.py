# Funcion para calcular el  promedio de cuatro calificaciones de cada materia
def calcular_promedio(calificaciones):
    return sum(calificaciones) / len(calificaciones)

# Diccionario para almacenar las calificaciones de cada materia
materias = {
    "Matematicas": 0,
    "Quimica": 0,
    "Lengua": 0,
    "Ingles": 0,
}

# Solicitar al usuario que ingrese las calificaciones para cada materia
for materia in materias:
    calificacion = float(input(f"Ingrese la calificacion para {materia}: ")) 
    materias[materia] = calificacion

# Calcular el promedio
promedio = calcular_promedio(list(materias.values()))

# Mostrar el resultado
print("\nCalificaciones ingresadas:")
for materia, calificacion in materias.items():
    print(f"{materia}: {calificacion}")

print(f"\nEl promedio de las calificaciones es: {promedio:.2f}")