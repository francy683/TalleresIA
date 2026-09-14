# -*- coding: utf-8 -*-
"""
Taller de Laboratorio: Defuzzificacion
Sesion 5 - Defuzzificacion (Centro de Gravedad)
"""

import numpy as np


# 1. Funcion que implementa la formula del Centroide (COG)
def centroide(x, curva):
    x = np.array(x, dtype=float)
    curva = np.array(curva, dtype=float)

    numerador = np.sum(x * curva)
    denominador = np.sum(curva)

    return numerador / denominador


# 2. Validacion con los datos del Taller Analitico (pagina anterior)
x_descuento = [10, 20, 30, 40]
mu_descuento = [0.2, 0.8, 0.8, 0.0]

resultado_validacion = centroide(x_descuento, mu_descuento)
print("=== Validacion con el Taller Analitico ===")
print(f"x  = {x_descuento}")
print(f"mu = {mu_descuento}")
print(f"COG calculado por Python: {resultado_validacion:.2f}%")
print("(Debe coincidir con el calculo hecho a mano: 23.33%)\n")


# 3. Escenario nuevo: sistema de frenado automatico
# Eje X: fuerza de frenado, de 0 a 100 Newtons, con 100 puntos
x_fuerza = np.linspace(0, 100, 100)

# Curva de campana de Gauss centrada en 70 (formula del PDF de Sesion 3/4)
centro = 70
sigma = 10
curva_frenado = np.exp(-((x_fuerza - centro) ** 2) / (2 * sigma ** 2))

# 4. Defuzzificacion del escenario de frenado
fuerza_exacta = centroide(x_fuerza, curva_frenado)

print("=== Sistema de Frenado Automatico ===")
print(f"Universo: 100 puntos entre 0 y 100 N")
print(f"Curva: campana de Gauss centrada en {centro} N")
print(f"FUERZA DE FRENADO EXACTA (crisp): {fuerza_exacta:.2f} N")