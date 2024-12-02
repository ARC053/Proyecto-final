import math

#Entrada
print("Calculo de la distancia entre dos puntos en el plano cartesiano.")
x1 = float(input("Ingrese la coordenada x1:"))
y1 = float(input("Ingrese la coordenada y1:"))
x2 = float(input("Ingrese la coordenada x2:"))
y2 = float(input("Ingrese la coordenada y2:"))

#Proceso
distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

#Salida
print(f"La distancia entre los puntos ({x1}, {y1}) y ({x2}, {y2}) es: {distancia:.2f}")