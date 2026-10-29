
# INPUT
# Lista original 
puntajes = [120, 450, 300, 450, 180, 520, 260, 450]

# PROCESS
# a) Cuantos jugadores hay
cantidad_jugadores = len(puntajes)

# b) Puntaje mayor y menor
mayor = max(puntajes)
menor = min(puntajes)

# c) Armar el podio con los 3 puntajes más altos sin modificar la lista original
podio = sorted(puntajes, reverse=True)[:3]

# d) Contar repeticiones del 450 y su primer índice
veces_450 = puntajes.count(450)
indice_450 = puntajes.index(450)

# e) Calcular el promedio para el recorrido final
promedio = sum(puntajes) / cantidad_jugadores


# OUTPUT
print(f"Cantidad de jugadores: {cantidad_jugadores}")
print(f"Puntaje mayor: {mayor}")
print(f"Puntaje menor: {menor}")

print(f"Podio (top 3): {podio}")
print(f"Lista original comprobación: {puntajes}")

print(f"El puntaje 450 se repite {veces_450} veces.")
print(f"El puntaje 450 aparece por primera vez en el índice {indice_450}.")
print(f"Promedio de puntajes: {promedio}")

print("Jugadores que superan el promedio:")
# Recorremos la lista con enumerate empezando en 1
for posicion, puntaje in enumerate(puntajes, 1):
    if puntaje > promedio:
        print(f"Jugador {posicion}: {puntaje}")