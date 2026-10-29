
import csv

# INPUT
datos_prestamos = [
    ["alumno", "libro", "dias_retraso"],
    ["Ana", "Cien anos de soledad", 3],
    ["Luis", "El llano en llamas", 0],
    ["Mia", "Pedro Paramo", 7],
    ["Beto", "Aura", 0],
    ["Sofia", "La region mas transparente", 2]
]

# PROCESS & OUTPUT

# a) y f) Crea prestamos.csv con csv.writer e incluye su encabezado usando with
with open("prestamos.csv", mode="w", newline='', encoding="utf-8") as archivo_prestamos:
    escritor = csv.writer(archivo_prestamos)
    escritor.writerows(datos_prestamos)

# Listas y variables para almacenar el procesamiento
multas_calculadas = []
total_recaudado = 0

# b) y f) Lee el archivo con csv.DictReader accediendo por nombre de columna
with open("prestamos.csv", mode="r", encoding="utf-8") as archivo_lectura:
    lector = csv.DictReader(archivo_lectura)
    
    for fila in lector:
        # Extraer los datos por nombre de columna
        dias_retraso = int(fila["dias_retraso"])
        
        # c) Calcula la multa solo cuando dias_retraso es mayor que 0
        if dias_retraso > 0:
            multa = dias_retraso * 5
            total_recaudado += multa # e) Acumula el total recaudado
            
            # Guardamos un diccionario con el formato para el nuevo CSV
            multas_calculadas.append({
                "alumno": fila["alumno"],
                "libro": fila["libro"],
                "multa": multa
            })

# d) y f) Escribe multas.csv con csv.DictWriter usando writeheader() y with
campos_multas = ["alumno", "libro", "multa"]

with open("multas.csv", mode="w", newline='', encoding="utf-8") as archivo_multas:
    escritor_dict = csv.DictWriter(archivo_multas, fieldnames=campos_multas)
    escritor_dict.writeheader()
    escritor_dict.writerows(multas_calculadas)


# Verificación final impresa en consola
print("Contenido del archivo 'multas.csv' generado:")
with open("multas.csv", mode="r", encoding="utf-8") as archivo_final:
    print(archivo_final.read())

# e) Imprime el total recaudado
print(f"Total recaudado en multas: ${total_recaudado}")