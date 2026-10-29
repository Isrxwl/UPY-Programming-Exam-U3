
# INPUT
respuestas = [("Ana", "camion"), ("Luis", "auto"), ("Mia", "camion"),
              ("Beto", "bici"), ("Ana", "camion"), ("Carlos", "auto"),
              ("Sofia", "camion"), ("Luis", "auto")]

tarjeta = {"Ana", "Beto", "Sofia", "Diego"}

# PROCESS
conteo_transporte = {}
alumnos_encuestados = set()

# a) Recorrer la lista desempaquetando la tupla (nombre, transporte)
for nombre, transporte in respuestas:
    # b) Contar cada transporte en un diccionario con .get(clave, 0)
    conteo_transporte[transporte] = conteo_transporte.get(transporte, 0) + 1
    
    # d) Construir un conjunto con los nombres
    alumnos_encuestados.add(nombre)

# c) Encontrar el transporte más usado recorriendo con .items()
transporte_mas_usado = ""
max_votos = 0
for trans, votos in conteo_transporte.items():
    if votos > max_votos:
        max_votos = votos
        transporte_mas_usado = trans

# e) Operaciones de conjuntos
# Intersección: alumnos encuestados que tienen tarjeta
con_tarjeta_y_encuestados = alumnos_encuestados.intersection(tarjeta)

# Diferencia: alumnos con tarjeta que no contestaron
con_tarjeta_sin_encuesta = tarjeta.difference(alumnos_encuestados)


# OUTPUT
print(f"Diccionario completo: {conteo_transporte}")
print(f"El transporte mas usado es {transporte_mas_usado} con {max_votos} respuestas.")
print(f"Contestaron la encuesta {len(alumnos_encuestados)} alumnos distintos.")

print(f"Alumnos con tarjeta y encuestados: {con_tarjeta_y_encuestados}")
print(f"Alumnos con tarjeta sin encuestar: {con_tarjeta_sin_encuesta}")