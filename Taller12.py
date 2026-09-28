# -*- coding: utf-8 -*-
"""
Taller de Laboratorio: Explorando las Matrices
Sesion 12 - Redes Neuronales Densas o Multicapa (MLP)
"""

import numpy as np


# Funcion de activacion: Sigmoide (devuelve un valor entre 0 y 1)
def sigmoide(x):
    return 1 / (1 + np.exp(-x))


# Pesos y sesgos de la red (3 entradas -> 4 neuronas ocultas -> 1 salida)
W1 = np.array([
    [0.1,  0.2, -0.3,  0.4],
    [-0.5, 0.6,  0.7, -0.8],
    [0.9, -0.1,  0.2,  0.3],
])
b1 = np.array([0.1, -0.2, 0.3, -0.4])

W2 = np.array([0.5, -0.6, 0.7, 0.8])
b2 = np.array([-0.1])


# Propagacion hacia adelante (sirve igual para 1 cliente o para un lote)
def forward(X):
    Z1 = np.dot(X, W1) + b1      # capa oculta: combinacion lineal
    A1 = sigmoide(Z1)            # capa oculta: activacion
    Z2 = np.dot(A1, W2) + b2     # capa de salida: combinacion lineal
    salida = sigmoide(Z2)        # capa de salida: activacion
    return Z1, A1, salida


# PARTE 1: un solo cliente (codigo del profesor)
X = np.array([0.5, 0.8, 0.2])
Z1, A1, salida = forward(X)

print("=== PARTE 1: un cliente ===")
print("Z1 (antes de sigmoide):", np.round(Z1, 4))
print("A1 (despues de sigmoide):", np.round(A1, 4))
print("Prediccion de la Red (Probabilidad):", np.round(salida[0], 4))

# PARTE 2: el reto dimensional, 2 clientes al mismo tiempo (lote)
X_lote = np.array([[0.5, 0.8, 0.2],
                   [0.1, 0.9, 0.9]])
Z1, A1, salida = forward(X_lote)

print("\n=== PARTE 2: lote de 2 clientes ===")
print("Z1:\n", np.round(Z1, 4))
print("A1:\n", np.round(A1, 4))
print("Predicciones (una por cliente):", np.round(salida, 4))