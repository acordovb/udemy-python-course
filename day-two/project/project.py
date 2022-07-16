nombre = input("Escribe tu nombre: ")
ventas = input("¿Cuál es el valor de sus ventas totales este mes?: ")

comisiones = float(ventas) * 13 / 100
print(f"Ok {nombre}. Este mes ganaste ${round(comisiones, 2)}")