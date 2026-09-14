# -*- coding: utf-8 -*-
"""
Taller de Laboratorio: Motor Logico de Recursos Humanos
Sesion 4 - Inferencia Difusa (Modelo Mamdani)
"""

# 1. Grados de membresia (resultado ya "fuzzificado" de un empleado)
grados = {
    "desempeno_pobre": 0.1,
    "desempeno_promedio": 0.3,
    "desempeno_excelente": 0.85,
    "antiguedad_corta": 0.2,
    "antiguedad_larga": 0.6,
}

# 2. Motor de inferencia: evalua las 3 reglas del taller
def evaluar_bono(grados):

    # R1: SI Desempeño es Pobre O Antigüedad es Corta -> Bono Bajo
    activacion_bajo = max(grados["desempeno_pobre"], grados["antiguedad_corta"])

    # R2: SI Desempeño es Promedio -> Bono Medio
    activacion_medio = grados["desempeno_promedio"]

    # R3: SI Desempeño es Excelente Y Antigüedad es Larga -> Bono Alto
    activacion_alto = min(grados["desempeno_excelente"], grados["antiguedad_larga"])

    return {
        "BAJO": activacion_bajo,
        "MEDIO": activacion_medio,
        "ALTO": activacion_alto,
    }

# 3. Ejecucion
fuerza_bonos = evaluar_bono(grados)
print("Fuerza de activacion para cada conclusion:", fuerza_bonos)

# 4. Pregunta teorica: Agregacion de dos reglas que concluyen en "Bono Alto"
# Si otra regla (por ejemplo R4) tambien concluyera "ALTO" con fuerza 0.7,
# la Agregacion de Mamdani exige usar la T-Conorma (MAX) para unificarlas:
fuerza_r3 = 0.4
fuerza_r4 = 0.7
fuerza_final_alto = max(fuerza_r3, fuerza_r4)
print("Fuerza final para 'Bono Alto' tras agregar R3 y R4:", fuerza_final_alto)