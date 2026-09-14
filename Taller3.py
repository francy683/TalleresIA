# -*- coding: utf-8 -*-
"""
Taller de Laboratorio: Logica Difusa Comercial
Sesion 3 - Incertidumbre y Logica Difusa
"""

# 1. Funcion de membresia triangular (formula del PDF, punto por punto)
def membresia_triangular(x, a, b, c):
    if x <= a or x >= c:
        return 0.0
    elif a < x <= b:
        return (x - a) / (b - a)
    elif b < x < c:
        return (c - x) / (c - b)


# 2. Definicion de los 3 conjuntos difusos (vertices dados en el taller)
CONJUNTOS = {
    "Novato": (0, 0, 5),
    "Intermedio": (2, 5, 8),
    "Experto": (5, 10, 20),
}

# 3. Conductores a evaluar
conductores = [3, 6, 12]

# 4. Evaluamos cada conductor contra los 3 conjuntos
for anios in conductores:
    print(f"\nConductor con {anios} años de experiencia:")

    grados = {}
    for categoria, (a, b, c) in CONJUNTOS.items():
        grado = membresia_triangular(anios, a, b, c)
        grados[categoria] = grado
        print(f"  - Pertenece a {categoria} en un {grado * 100:.1f}%")

    # Categoria con el mayor grado de verdad (max sobre el diccionario)
    mejor_categoria = max(grados, key=grados.get)
    print(f"  => Categoria mas cercana: {mejor_categoria} "
          f"({grados[mejor_categoria] * 100:.1f}%)")