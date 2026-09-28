# -*- coding: utf-8 -*-
"""
Taller de Laboratorio: Hackeando los Pesos
Sesion 11 - Redes Neuronales: El Perceptron
"""

import numpy as np


# 1. Funcion de activacion (Escalon)
def funcion_escalon(z):
    if z >= 0:
        return 1
    else:
        return 0


# 2. Estructura de la neurona: Z = X . W + b, luego activacion
def perceptron(X, W, b):
    Z = np.dot(X, W) + b
    return funcion_escalon(Z)


# 3. Compuerta AND (codigo del profesor): pesos y sesgo originales
pesos_and = np.array([0.5, 0.5])
sesgo_and = -0.8

print("=== Compuerta AND (pesos [0.5, 0.5], sesgo -0.8) ===")
for entrada in [[0, 0], [0, 1], [1, 0], [1, 1]]:
    print(f"  {entrada} -> {perceptron(np.array(entrada), pesos_and, sesgo_and)}")

# 4. El reto: pesos y sesgo elegidos a mano para la compuerta OR
pesos_or = np.array([1, 1])
sesgo_or = -0.5

print("\n=== Compuerta OR (pesos [1, 1], sesgo -0.5) ===")
for entrada in [[0, 0], [0, 1], [1, 0], [1, 1]]:
    print(f"  {entrada} -> {perceptron(np.array(entrada), pesos_or, sesgo_or)}")