#Funcion para calcular el numero de segundos  en un  determinado nuemro de dias

def calcular_segundos(dias):
    segundos_por_dia = 24 * 60 *60 #24 horas * 60 minutos * 60 segundos
    return dias * segundos_por_dia

# Solicitar al usuario que ingrese el numero de dias: 
dias = int(input("Ingrese el numero de dias: "))

# Calcular los segundos
segundos = calcular_segundos(dias)

# Mostrar el resultado 
print(f"El numero de segundo en {dias} dias es: {segundos} segundos ")